from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension


db = SQLAlchemy()

app = Flask(__name__)

app.secret_key = "SECRET!"

@app.route("/")
def index():
    """Query database and return all melons, ordered by price."""

    sql = "SELECT id, type, name, price FROM melons ORDER BY price"

    cursor = db.session.execute(sql)
    melons = cursor.fetchall()

    return render_template("index.html", melons=melons)


@app.route("/search")
def find_melons():
    """Find melons with cost between min and max."""

    min_price = float(request.args.get('min'))
    max_price = float(request.args.get('max'))

    sql = """SELECT id, type, name, price
             FROM melons
             WHERE price BETWEEN :minimum AND :maximum
             ORDER BY price
          """

    cursor = db.session.execute(sql,
                                {'minimum': min_price,
                                 'maximum': max_price})
    melons = cursor.fetchall()

    return render_template("index.html", melons=melons)


@app.route("/melon-add", methods=["POST"])
def add_melon():
    """Add a melon and redirect to home page."""

    name = request.form.get("melon-name")
    melon_type = request.form.get("melon-type")
    price = request.form.get("melon-price")

    sql = """INSERT INTO melons (type, name, price)
             VALUES (:type, :name, :price)
          """

    db.session.execute(sql,
                       {'type': melon_type,
                        'name': name,
                        'price': price})

    db.session.commit()

    return redirect("/")


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect to database."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///melondb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    connect_to_db(app)
    app.debug = True
    DebugToolbarExtension(app)
    app.run(host="0.0.0.0")
