from filmood import app
from filmood import db
from filmood.models import User, Film, Genre, Mood
from flask import request, abort

@app.route('/api/1.0/film/<int:film_id>', methods=['GET'])
def get_film(film_id):
    film = Film.query.filter_by(id=film_id).first()
    if film:
        return film.to_json(film.moods)
    abort(404)

@app.route('/api/1.0/film/<int:film_id>', methods=['DELETE'])
def delete_film(film_id):
    film = Film.query.filter_by(id=film_id).first()
    if film:
        db.session.delete(film)
        db.session.commit()
        return film.to_json(film.moods)
    abort(404)

@app.route('/api/1.0/film', methods=['POST'])
def insert_film():
    params = request.args
    if not params and ('name' in params and 'description' in params) :
        abort(400)
    for param in params:
        if param not in Film.__mapper__.c:
            abort(400)

    film = Film(**params)
    db.session.add(film)
    db.session.commit()
    return film.to_json()


@app.route('/api/1.0/film/<int:film_id>', methods=['PUT'])
def update_film(film_id):
    params = request.args
    film = Film.query.filter_by(id=film_id)
    if not film or not params:
        abort(400)

    for param in params:
        if param not in Film.__mapper__.c:
            abort(400)

    Film.query.filter_by(id=film_id).update(params)
    film = Film.query.filter_by(id=film_id).first()
    db.session.commit()
    return film.to_json()