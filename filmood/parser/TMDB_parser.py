import tmdbsimple as tmdb
from filmood.models import *
from filmood import db

"""https://www.pydoc.io/pypi/tmdbsimple-1.8.0/"""
"""OMDB"""

api_key = "765b0d1f4ca8757f641c2f8e9c95c05f"

tmdb.API_KEY = api_key

id=1
successful_request = 1
while successful_request < 10000:
    try:
        movie = tmdb.Movies(id)
        movie_dict = movie.info()
        if movie_dict.get("vote_average") > 5:
            moment_film = Film(
                title = movie_dict.get("title"),
                release_date =movie_dict.get("release_date"),
                runtime =movie_dict.get("runtime"),
                backdrop_path =movie_dict.get("backdrop_path"),
                poster_path =movie_dict.get("poster_path"),
                imdb_id =movie_dict.get("imdb_id"),
                overview =movie_dict.get("overview"),
                vote_average =movie_dict.get("vote_average"),
            )

            for genre_name in movie_dict.get("genres"):
                answer_for_query = Genre.query.filtr_by(name=genre_name["name"]).first()
                if answer_for_query :
                    moment_film.genres.append(answer_for_query)
                else :
                    genre = Genre(name = genre_name["name"])
                    moment_film.genres.append(genre)
            db.session.add(moment_film)
            db.session.commit()
            successful_request += 1
            print(moment_film)

    except Exception:
        pass
    with open("last_id_on_tmdb.txt", "w") as txt_file:
        txt_file.write(str(id))
    id +=1

