from basicmodel import BasicModel


class Film(BasicModel):
    _TABLE = "films"
    _FIELDS_MAPPING = {
        'id': int,
        'filmname': str,
        'description': str,
        'release_year': int
        }
    _PK = 'id'
