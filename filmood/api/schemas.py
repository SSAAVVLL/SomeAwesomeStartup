from marshmallow import Schema, fields, ValidationError


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

class MoodSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

class FilmSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    overview = fields.Str(required=True)
    release_date = fields.Date(required=True)
    runtime = fields.Str()
    backdrop_path = fields.Str()
    poster_path = fields.Str()
    imdb_id = fields.Str()
    vote_average = fields.Str()
    genres = fields.Nested(GenreSchema(many=True))
    moods = fields.Nested(MoodSchema(many=True))

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    films = fields.Nested(FilmSchema(many=True))

class CommentSchema(Schema):
    id = fields.Int(dump_only=True)
    film = fields.Nested(FilmSchema())
    content = fields.Str(required=True)
