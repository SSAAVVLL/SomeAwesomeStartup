from BasicModel import BasicModel


class mood(BasicModel):
    _FIELDS_MAPPING = {
        "id": int,
        "name": str
    }
    _TABLE = "mood"