import tmdbsimple as tmdb
from flask import url_for
from datetime import datetime
from filmood.models import *
from filmood import db

'''https://www.pydoc.io/pypi/tmdbsimple-1.8.0/'''
'''OMDB'''

api_key = '765b0d1f4ca8757f641c2f8e9c95c05f'
tmdb.API_KEY = api_key

with open('filmood/parser/last_id_on_tmdb.txt', 'r') as file:
    last_id = int(file.read())
cur_id = last_id
# cur_id = 1
amount_of_films = len(Film.query.all())

while amount_of_films < 10000:
    try:
        movie_info = tmdb.Movies(cur_id).info()
        film = Film(
            title = movie_info['title'],
            release_date = datetime.strptime(movie_info['release_date'], '%Y-%m-%d'),
            runtime = movie_info['runtime'],
            backdrop_path = movie_info['backdrop_path'],
            poster_path = movie_info['poster_path'],
            imdb_id = movie_info['imdb_id'],
            overview = movie_info['overview'],
            vote_average = movie_info['vote_average']
        )

        for genre in movie_info['genres']:
            find_genre = Genre.query.filter_by(name=genre['name']).first()
            if find_genre:
                film.genres.append(find_genre)
            else:
                new_genre = Genre(name=genre['name'])exit
                film.genres.append(new_genre)
        db.session.add(film)
        db.session.commit()
        amount_of_films += 1

    except Exception as err:
        print(err)

    print(cur_id, amount_of_films)
    cur_id += 1
    with open('filmood/parser/last_id_on_tmdb.txt', 'w') as file:
        file.write(str(cur_id))

