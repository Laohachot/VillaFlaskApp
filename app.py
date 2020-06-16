from flask import Flask, render_template, url_for
import os 
import sys
from funcs import sort_regex, read

app = Flask(
    __name__,
    static_url_path='',
    static_folder=os.path.join('web','static'),
    template_folder=os.path.join('web','templates')
)

app.jinja_env.globals.update(zip=zip, len=len, range=range)
        
extensions = {'.jpg','.png','.jpeg'}
static_dir = os.path.join('web','static')
PATHS = sort_regex('\d+', [path for path in os.listdir(static_dir) if os.path.splitext(path)[1] in extensions])
CAPTIONS = [read(os.path.join(static_dir,f)).strip() for f in [os.path.splitext(path)[0]+'.txt' for path in PATHS]]

def read(f):
    with open(f, 'r') as f:
        return f.read()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', PATHS=PATHS, CAPTIONS=CAPTIONS)

@app.route('/contact')
def contact():
    return render_template('home.html', PATHS=PATHS, CAPTIONS=CAPTIONS)

@app.route('/about')
def about():
    return render_template('home.html', PATHS=PATHS, CAPTIONS=CAPTIONS)