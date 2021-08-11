from flask import Flask, request
from random import choice, randint


COMPLIMENTS = ['smart', 'clever', 'tenacious', 'awesome', 'Pythonic']

app = Flask(__name__)

@app.route('/')
def index():
    """Show homepage"""

    return """
    <html>
    <body>
      <h1>I am the landing page</h1>
    </body>
    </html>
    """

@app.route('/form')
def show_form():
    """Greet user and ask for name."""

    return """
    <!doctype html>
    <html>
    <head>
      <title>Hi There!</title>
    </head>
    <body>
      <h1>Hi There!</h1>
      <form action="/greet">
        What's your name?
        <input type="text" name="person">
        <input type="submit">
      </form>
    </body>
    </html>
    """

@app.route('/greet')
def offer_greeting():
    """Greet user with a random compliment."""

    player = request.args.get('person')
    nice_thing = choice(COMPLIMENTS)

    return f"""
    <!doctype html>
    <html>
    <head>
      <title>A Compliment</title>
    </head>
    <body>
      Hi {player} I think you're {nice_thing}!
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')