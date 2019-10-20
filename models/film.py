from BasicModel import BasicModel


class film(BasicModel):
    _FIELDS_MAPPING = {
        "film_id": int,
        "film_name": str,
        "description": str,
    }
    _TABLE = "FILMS_BLACKHOLE"

something = film

print(something._FIELDS_MAPPING)
