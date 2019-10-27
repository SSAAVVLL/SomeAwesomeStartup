from BasicModel import BasicModel


class Comment(BasicModel):
    _FIELDS_MAPPING = {
        "id_resource": int,
        "id_film": int,
        "text": str
    }


