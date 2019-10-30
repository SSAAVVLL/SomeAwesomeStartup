
from flask import render_template, url_for
from filmood import app
from filmood.models import User, Film, Genre, Mood


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html', title="Our Team")