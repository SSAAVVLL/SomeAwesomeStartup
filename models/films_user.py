from BasicModel import BasicModel

class films_user(BasicModel):
    _FIELDS_MAPPING = {
        "user_id": int,
        "film_id": int
    }
    _TABLE = "watched_films"