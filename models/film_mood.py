from BasicModel import BasicModel


class film_mood(BasicModel):
    _FIELDS_MAPPING = {
        "id_mood": int,
        "id_film": int
    }
    _TABLE = "film_mood"