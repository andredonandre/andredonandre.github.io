from flask import  Flask, render_template

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/blog')
def Blog():
    return '<h1>blog page</h2>'

@app.route('/contact')
def Contact():
    return '<h1>Contact page</h2>'

@app.route('/projects')
def Projects():
    return '<h1>Welcome the projects page</h2>'