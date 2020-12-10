from flask import  Flask, render_template

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/blog')
def Blog():
    return render_template('blog.html')

@app.route('/contact')
def Contact():
    return render_template('contact.html')

@app.route('/projects')
def Projects():
    return render_template('projects.html')

@app.route('/', subdomain = "api")
def Resume():
    return '{"name": "Andrew Sembatya", "Title": "Head of development"}'