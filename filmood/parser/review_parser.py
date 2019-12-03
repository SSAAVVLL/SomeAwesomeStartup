from imdb import IMDb
import json
from filmood import db
from filmood.models import *

IMDB = IMDb()
for id in range(10000):
    try:
        film = Film.get(id)
        imdb_id = film.imdb_id[2:]
        if imdb_id:
            reviews = IMDB.get_movie_reviews(imdb_id).get('data').get('reviews')
            if reviews and len(reviews) >= 10:
                for review in reviews:
                    comment = Comment(content=review['content'], film=film)
                    db.session.add(comment)
                print(f"film_id: {film.id} - {len(reviews)}")
            else:
                db.session.delete(film)
                len_rev = len(reviews) if reviews else 0
                print(f"film_id: {film.id} - {len_rev} REMOVED")

            db.session.commit()

    except Exception as err:
        print(err)