from imdb import IMDb, IMDbDataAccessError
from filmood.models import *
from filmood import db
from filmood.crud import *
import json

with open('last_id_imdb.txt', 'r') as file:
    last_id = int(file.readline())

filmImdbInfo = IMDb()
for id in range(last_id + 1, 10000):
    film = Film.query.filter_by(id=id).first()
    filmFromDb = Film.get(id)
    imdb_id = film.imdb_id
    try:
        movie = filmImdbInfo.get_movie_reviews(imdb_id[2:])
        counter = 0
        if 'reviews' in movie['data']:
            count = Comment.query.filter_by(id_film=film.id).count()
            if count == 0:
                for review in movie['data']['reviews']:
                    print(f"{review['content']} \n {20*'_'}")
                    # print(json_imdbFilmId['id'])
                    comment = Comment()
                    comment.id_film = film.id
                    comment.text = review['content']
                    db.session.add(comment)
                    db.session.commit()

            print(f"amount of comments {len(movie['data']['reviews'])} and this film id")
    except IMDbDataAccessError:
        print('error access IMDB')

    print('film_id', id)
    with open('last_id_imdb.txt', 'w') as file:
        file.write(str(id))
