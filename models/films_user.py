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
something._create_record(getattr(something,"id"))