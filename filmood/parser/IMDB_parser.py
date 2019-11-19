from imdb import IMDb
from filmood.models import *
from filmood import db
from filmood.crud import *
import json

filmImdbInfo = IMDb()
for id in range(1, 10000):
    filmFromDb = Film.get(id)
    json_imdbFilmId = json.loads(filmFromDb)
    json_imdbFilmId = json_imdbFilmId['imdb_id']
    print(json_imdbFilmId)
    movie = filmImdbInfo.get_movie_reviews(json_imdbFilmId[2:])
    counter = 0
    for review in movie['data']['reviews']:
        print(f"{review['content']} \n {20*'_'}")
        counter += 1
    print(f"amount of comments {counter} and this film id {json_imdbFilmId}")