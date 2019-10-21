from basicmodel import BasicModel


class User(BasicModel):
    _TABLE = "users"
    _FIELDS_MAPPING = {
        'id': int,
        'uesr_name': str,
        'email': str,
        'pass': str
        }
    _PK = 'id'
