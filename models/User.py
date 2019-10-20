from BasicModel import BasicModel


class User(BasicModel):
    _FIELDS_MAPPING = {
        "id": int,
        "email": str,
        "username": str,
        "password": str
    }
    _TABLE = "Regular_User"
