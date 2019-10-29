from flask import Flask, render_template
import http_const
import json
from models import film
app = Flask(__name__,
            template_folder='templates',
            static_url_path='',
            static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/film/<int:id>', methods=['GET', 'PUT' 'POST'])
def handleFilm(id):

    return ''

app.run()
