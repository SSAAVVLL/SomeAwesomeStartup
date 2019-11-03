import tmdbsimple as tmdb

"""https://www.pydoc.io/pypi/tmdbsimple-1.8.0/"""
"""OMDB"""

api_key = "765b0d1f4ca8757f641c2f8e9c95c05f"

tmdb.API_KEY = api_key

i=1
while i < 1000000:
    try:
        movie = tmdb.Movies(i)
        print(movie.info())
    except Exception:
        pass
    i +=1
