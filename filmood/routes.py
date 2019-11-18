from flask import render_template, url_for, request
from filmood import app
from filmood.models import User, Film, Genre, Mood
import hashlib
from sqlalchemy import inspect

import jwt
import json

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html', title="Our Team")


@app.route('/api/user/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def process_request_user(id):
    if request.method == 'GET':
        return User.get(id)
    elif request.method == 'DELETE':
        return User.delete(id)
    else:
        params = request.args
        return User.update(id, params)

@app.route('/api/user', methods=['POST'])
def insert_user():
    params = request.args
    return User.insert(params)


@app.route('/api/film/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def process_request_film(id):
    if request.method == 'GET':
        return Film.get(id)
    elif request.method == 'DELETE':
        return Film.delete(id)
    else:
        params = request.args
        return Film.update(id, params)

@app.route('/api/film', methods=['POST'])
def insert_film():
    params = request.args
    return Film.insert(params)



@app.route('/api/genre/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def process_request_genre(id):
    if request.method == 'GET':
        return Genre.get(id)
    elif request.method == 'DELETE':
        return Genre.delete(id)
    else:
        params = request.args
        return Genre.update(id, params)

@app.route('/api/genre', methods=['POST'])
def insert_genre():
    params = request.args
    return Genre.insert(params)



@app.route('/api/mood/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def process_request_mood(id):
    if request.method == 'GET':
        return Mood.get(id)
    elif request.method == 'DELETE':
        return Mood.delete(id)
    else:
        params = request.args
        return Mood.update(id, params)

@app.route('/api/mood', methods=['POST'])
def insert_mood():
    params = request.args
    return Mood.insert(params)


@app.route('/auth/register', methods=['POST'])
def register():
    if request.method == 'POST':
        params = request.json
        print(params)

        return '123123'


@app.route('/auth/signin', methods=['POST'])
def sign_in():
    if request.method == 'POST':
        params = request.json
        print(params)
        login = params['login']
        password = params['password']
        return answer(login, password)


def answer(login, password) -> str:
    if password is None or login is None:
        return error('login and password required')
    else:
        return make_jwt(login, password)


def make_jwt(login, password) -> str:
    return compare([get_data(login), hash_pwd(password)])


def get_data(login) -> dict:
    data = User().query.filter_by(username=login).first()
    if data is None:
        return json.load(error())
    return object_as_dict(data)


def hash_pwd(password) -> str:
    return hashlib.md5(password.encode('UTF-8')).hexdigest()


def compare(data) -> str:
    if data[0]['error'] is not None and data[0]['password'] == data[1]:
        return create_jwt(data[0])
    else:
        return error()


def create_jwt(user) -> str:
    return jwt.encode(user, 'secret', algorithm='HS256')


def error(msg='Аутизм') -> str:
    return json.dumps({'error': {
        'message': msg
    }})
