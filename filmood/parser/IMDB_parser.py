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
    movie = filmImdbInfo.get_movie_external_reviews(movieID=json_imdbFilmId)
    print(movie)