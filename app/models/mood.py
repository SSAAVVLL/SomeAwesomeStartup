from basicmodel import BasicModel


class Mood(BasicModel):
    _TABLE = "moods"
    _FIELDS_MAPPING = {
        'id': int,
        'moodname': str
        }
    _PK = 'id'
    