import flask
from flask import app

# Create the app
app = flask.Flask(__name__)


# Main route is a static file in static/index.html
@app.route('/')
def index():
    return flask.render_template('index.html')


# Route: Show a random example website with an injeciton from the examples folder
@app.route('/example')
def example():
    # list directory content in examples folder
    import os
    examples = os.listdir('static/examples')
    # choose a random example
    import random
    e = random.choice(examples)
    # redirect to the example folder/index.html
    return flask.redirect('/static/examples/' + e + '/index.html')


# Route: receive exfiltrated infos
@app.route('/we93rurkd')
def exfiltrate():
    return flask.render_template('exfiltrate.html')


if __name__ == '__main__':
    app.run()
