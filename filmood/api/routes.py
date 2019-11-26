import json
from datetime import datetime
from flask import request
from filmood import app
from marshmallow import ValidationError
from filmood.models import *
from filmood.api.schemas import *


def handle_request(id, request, schema, entity):
    """Handle GET, DELETE and PUT requests.

    Args:
        id (int): id of the instance of the given entity.
        requset: received request.
        schema: entity's schema.
        entity: entity's class.

    Returns:
        str: JSON formated answer.

    Raises:
        ValidationError: If given data was invalid.
    """
    try:
        if request.method == 'GET':
            return schema().dump(entity.get(id))
        elif request.method == 'DELETE':
            return schema().dump(entity.delete(id))
        elif request.method == 'PUT':
            if not request.args:
                return {'error_messages': "No input data provided"}, 400
            params = request.args
            return schema().dump(entity.update(id, **params))
    except ValidationError as err:
        return {'error_messages': json.dumps(err.messages)}, 422

def handle_insert_request(request, schema, entity):
    """Handle POST requests.

    Args:
        requset: received request.
        schema: entity's schema.
        entity: entity's class.

    Returns:
        str: JSON formated answer.

    Raises:
        ValidationError: If given data was invalid.
    """
    if not request.args:
        return {'error_messages': "No input data provided"}, 400
    try:
        params = request.args
        schema().load(params)
        return schema().dump(entity.insert(**params))
    except ValidationError as err:
        return {'error_messages': json.dumps(err.messages)}, 400


@app.route('/api/user/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def handle_request_user(id):
    return handle_request(id, request, UserSchema, User)


@app.route('/api/film/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def handle_request_film(id):
    if request.method == 'PUT':
        if not request.args:
            return {'error_messages': "No input data provided"}, 400
        
        params = request.args.copy()
        if (params.get("release_date")):
            params["release_date"] = datetime.strptime(params["release_date"], "%Y-%m-%d")
        try:
            return FilmSchema().dump(Film.update(id, **params))
        except ValidationError as err:
            return {'error_messages': json.dumps(err.messages)}, 422

    return handle_request(id, request, FilmSchema, Film)

@app.route('/api/film', methods=['POST'])
def insert_film():
    if not request.args:
        return {'error_messages': "No input data provided"}, 400
    try:
        params = request.args.copy()
        FilmSchema().load(params)
        params["release_date"] = datetime.strptime(params["release_date"], "%Y-%m-%d")
        return FilmSchema().dump(Film.insert(**params))
    except ValidationError as err:
        return {'error_messages': json.dumps(err.messages)}, 400


@app.route('/api/genre/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def handle_request_genre(id):
    return handle_request(id, request, GenreSchema, Genre)

@app.route('/api/genre', methods=['POST'])
def insert_genre():
    return handle_insert_request(request, GenreSchema, Genre)


@app.route('/api/mood/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def handle_request_mood(id):
    return handle_request(id, request, MoodSchema, Mood)

@app.route('/api/mood', methods=['POST'])
def insert_mood():
    return handle_insert_request(request, MoodSchema, Mood)


@app.route('/api/comment/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def handle_request_comment(id):
    return handle_request(id, request, CommentSchema, Comment)

@app.route('/api/comment', methods=['POST'])
def insert_comment():
    return handle_insert_request(request, CommentSchema, Comment)
