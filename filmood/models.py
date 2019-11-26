from filmood import db
from filmood.api.crud import CRUD


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


class User(db.Model, CRUD):
    """
    This entity represent table which contain users

    Attributes:
    ----------
    id: this user id
    username: login of this user
    email: user's email address
    password: user's password
    films: contain relationship between user and watched films
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    films = db.relationship('Film', secondary=watched_films, lazy='subquery',
                            backref=db.backref('user', lazy=True))

    def __repr__(self):
        return f"User({self.username}, {self.email})"

class Film(db.Model, CRUD):
    """
    This entity represent table which contain films

    Attributes:
    ----------
    id: this film id
    title: title of this film
    overview: is a brief description of the film
    release_date: film release date
    moods: contain relationship between film and his moods
    genres: contain relationship between film and his genres
    runtime: information abouts film runtime
    backdrop_path : idk
    poster_path: contain path to films poster on TMDB.com
    imdb_id: contain path to this film on IMDB.com
    vote_average: something useless statistic from TMDB.com
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    overview = db.Column(db.String(2000), nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)
    runtime = db.Column(db.String(10))
    backdrop_path = db.Column(db.String(100))
    poster_path = db.Column(db.String(100))
    imdb_id = db.Column(db.String(100))
    vote_average = db.Column(db.String(5))
    moods = db.relationship('Mood', secondary=film_moods, lazy='subquery',
                            backref=db.backref('films', lazy=True))
    genres = db.relationship('Genre', secondary=film_genres, lazy='subquery',
                            backref=db.backref('films', lazy=True))
    

    def __repr__(self):
        return f"Film({self.title}, {self.release_date}, {self.genres}, {self.moods}, {self.vote_average})"


class Genre(db.Model, CRUD):
    """
    This entity represent table which contain film's genres

    Attributes:
    ----------
    id: this genre id
    name: title of this genre
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    
    def __repr__(self):
        return f"Genre({self.name})"

class Mood(db.Model, CRUD):
    """
    This entity represent table which contain moods

    Attributes:
    ----------
    id: this mood id
    name: title of this mood
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    
    def __repr__(self):
        return f"Mood({self.name})"

class Comment(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey("film.id"))
    film = db.relationship("Film", backref=db.backref("comments", lazy=True))
    content = db.Column(db.String(2500))

    def __repr__(self):
        return f"Comment({self.content}, {self.film_id})"