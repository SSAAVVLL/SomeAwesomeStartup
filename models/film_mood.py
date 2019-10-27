from BasicModel import BasicModel


class film_mood(BasicModel):
    _FIELDS_MAPPING = {
        "id": int,
        "mood_id": int,
        "film_id": int
    }
    _TABLE = "film_mood"