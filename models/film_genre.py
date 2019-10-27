from BasicModel import BasicModel


class film_genre(BasicModel):
    _FIELDS_MAPPING = {
        "id": int,
        "genre_id": int,
        "film+id": int
    }
    _TABLE = "film_genre"