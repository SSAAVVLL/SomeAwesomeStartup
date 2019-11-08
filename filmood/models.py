from datetime import datetime
from filmood import db
from filmood.serialization import OutputMixin
from filmood.crud import CRUD


watched_films = db.Table(
    'watched_films',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('film_id', db.Integer, db.ForeignKey('film.id'), primary_key=True)
)
film_moods = db.Table(
    'film_moods',
    db.Column('film_id', db.Integer, db.ForeignKey('film.id'), primary_key=True),
    db.Column('mood_id', db.Integer, db.ForeignKey('mood.id'), primary_key=True)
)
film_genres = db.Table(
    'film_genres',
    db.Column('film_id', db.Integer, db.ForeignKey('film.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'), primary_key=True)
)


class User(db.Model, OutputMixin, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    films = db.relationship('Film', secondary=watched_films, lazy='subquery',
                            backref=db.backref('users', lazy=True))

    def __repr__(self):
        return f"User({self.username}, {self.email})"

class Film(db.Model, OutputMixin, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    overview = db.Column(db.String(2000), nullable=False)
    release_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    moods = db.relationship('Mood', secondary=film_moods, lazy='subquery',
                            backref=db.backref('films', lazy=True))
    genres = db.relationship('Genre', secondary=film_genres, lazy='subquery',
                            backref=db.backref('films', lazy=True))
    runtime = db.Column(db.String(5), nullable=False)
    backdrop_path = db.Column(db.String(100), nullable=True)
    poster_path = db.Column(db.String(100), nullable=True)
    imdb_id = db.Column(db.String(100), nullable=True)
    vote_average = db.Column(db.String(5), nullable=True)

    def __repr__(self):
        return f"Film({self.name})"


class Genre(db.Model, OutputMixin, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    
    def __repr__(self):
        return f"Genre({self.name})"

class Mood(db.Model, OutputMixin, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    
    def __repr__(self):
        return f"Mood({self.name})"