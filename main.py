from flask import Flask, render_template, url_for
app = Flask(
    __name__,
    static_url_path='',
    static_folder='web/static',
    template_folder='web/templates'
)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/contact')
def catdog():
    return 'catdog'