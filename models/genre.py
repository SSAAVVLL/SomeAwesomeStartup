from BasicModel import BasicModel

class genre(BasicModel):
    _FIELDS_MAPPING = {
        "id": int,
        "name": str
    }
    _TABLE = "genre"