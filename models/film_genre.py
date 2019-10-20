from BasicModel import BasicModel


class film_genre(BasicModel):
    _FIELDS_MAPPING = {
        "id_genre": int,
        "id_film": int
    }
    _TABLE = "film_genre"