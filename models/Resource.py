from BasicModel import BasicModel


class Resource(BasicModel):
    _FIELDS_MAPPING = {
        "id": int,
        "url": str,
        "name": str
    }