"""Models for Ubermelon Bites."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class StorageSpace(db.Model):
    """A storage space."""

    __tablename__ = "storage_spaces"

    storage_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    capacity = db.Column(db.Integer)
    # melons = a list of Melon objects

    def __repr__(self):
        return f"<StorageSpace storage_id={self.storage_id} capacity={self.capacity}>"

class MelonType(db.Model):
    """A melon type."""

    __tablename__ = "melon_types"

    type_code = db.Column(db.String, primary_key=True)
    type_name = db.Column(db.String)
    max_slices = db.Column(db.Integer)
    # melons = a list of Melon objects

    def __repr__(self):
        return f"<MelonType type_code={self.type_code} max_slices={self.max_slices}>"

class Melon(db.Model):
    """A melon."""

    __tablename__ = "melons"

    melon_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    type_code = db.Column(db.String, db.ForeignKey("melon_types.type_code"))
    arrived_at = db.Column(db.DateTime)
    storage_id = db.Column(db.Integer, db.ForeignKey("storage_spaces.storage_id"))
    slices_in = db.Column(db.Integer)

    melon_type = db.relationship("MelonType", backref="melons")
    storage_space = db.relationship("StorageSpace", backref="melons")
    # slices = a list of SliceOrder objects

    def __repr__(self):
        return f"<Melon melon_id={self.melon_id} slices_in={self.slices_in}>"

class Customer(db.Model):
    """A customer."""

    __tablename__ = "customers"

    customer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    phone = db.Column(db.String)
    # orders = A list of Order objects

    def __repr__(self):
        return f"<Customer customer_id={self.customer_id} name={self.name}>"

class Order(db.Model):
    """An order."""

    __tablename__ = "orders"

    order_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ordered_at = db.Column(db.DateTime)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.customer_id"))

    customer = db.relationship("Customer", backref="orders")
    # slices = a list of SliceOrder objects

    def __repr__(self):
        return f"<Order order_id={self.order_id} customer_id={self.customer_id}>"

class SliceOrder(db.Model):
    """An association table between Melons and Orders."""

    __tablename__ = "slices"

    slice_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    melon_id = db.Column(db.Integer, db.ForeignKey("melons.melon_id"))
    order_id = db.Column(db.Integer, db.ForeignKey("orders.order_id"))
    quantity = db.Column(db.Integer)

    melon = db.relationship("Melon", backref="slices")
    order = db.relationship("Order", backref="slices")

    def __repr__(self):
        return f"<SliceOrder slice_id={self.slice_id} quantity={self.quantity} order_id={self.order_id}"

def get_biggest_customer():
    customers = Customer.query.all()
    customer_slices = {}
    for c in customers:
        orders = Order.query.filter(Customer.customer_id==c.customer_id).all()
        total_slices = 0
        for o in orders:
            slices = db.session.query( \
                db.func.sum(SliceOrder.quantity)) \
                .filter(SliceOrder.order_id==o.order_id)
            total_slices += slices.one()[0]          
        customer_slices[c] = total_slices
    print(customer_slices)
    # q = db.session.query(Customer.name, db.func.sum(SliceOrder.quantity)).group_by(Customer.name)

def connect_to_db(flask_app, db_uri="postgresql:///ubermelon", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
