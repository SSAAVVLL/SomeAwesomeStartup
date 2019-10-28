from BasicModel import BasicModel

class films_user(BasicModel):
    _FIELDS_MAPPING = {
        "id": int,
        "user_id": int,
        "film_id": int
    }
    _TABLE = "watched_films"


something = films_user("BUBA")

something.fill_data({"id": 1235, "user_id": 564, "film_id": 465})
print(something.__dict__)
pk = getattr(something, "id")
print(pk)
something._delite_record(pk)
something._create_record(pk)
something._update_record(pk, {"user_id": 6666})
print(something.__dict__)
something._read_record(pk)

