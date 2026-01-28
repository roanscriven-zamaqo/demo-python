from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Codecapsules")

@app.route('/greeting')
def greeting():
    return "Hello there, thank you for visiting my new route"

# End of file: app/routes.py
