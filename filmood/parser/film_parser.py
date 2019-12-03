import tmdbsimple as tmdb
from datetime import datetime
from filmood.models import *
from filmood import db
import json


tmdb.API_KEY = '765b0d1f4ca8757f641c2f8e9c95c05f'

# cur_id = json.load(open('filmood/parser/last_film_id.json', 'r'))["last_id"]
cur_id = 1
valid_film_ids = [json.loads(line)["id"] for line in open(
    'filmood/parser/movie_ids_11_26_2019.json', 'r',  encoding='utf-8')]

amount_of_films = 0
# amount_of_films = len(Film.query.all())

while amount_of_films < 50000:
    try:
        movie_info = tmdb.Movies(valid_film_ids[cur_id]).info()
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
                new_genre = Genre(name=genre['name'])
                film.genres.append(new_genre)

        db.session.add(film)
        db.session.commit()

        amount_of_films += 1

    except Exception as err:
        print(err)

    print(cur_id)
    cur_id += 1
    # with open('filmood/parser/last_film_id.json', 'w') as file:
    #     file.write(json.dumps({"last_id": cur_id}))
