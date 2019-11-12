from flask import url_for, request
from filmood import app
from filmood.models import User, Film, Genre, Mood
from filmood.crud import CRUD
from filmood import db, ma
from sqlalchemy.exc import IntegrityError




@app.route('/api/user/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def handle_request_user(id):
    if request.method == 'GET':
        return CRUD(User).get(id)
    elif request.method == 'DELETE':
        return CRUD(User).delete(id)
    else:
        params = request.args
        return CRUD(User).update(id, params)

@app.route('/api/user', methods=['POST'])
def insert_user():
    params = request.args
    return CRUD(User).insert(params)



@app.route('/api/film/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def handle_request_film(id):
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
def handle_request_genre(id):
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
def handle_request_mood(id):
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