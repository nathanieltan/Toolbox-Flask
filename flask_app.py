"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/test')
def test():
    return 'test'
@app.route('/login', methods = ['POST'])
def login():
    return render_template('profile.html', firstName=request.form['firstName'],age=request.form['age'],favoriteNinja='Patrick Huston')
if __name__ == '__main__':
    app.debug = True
    app.run()
