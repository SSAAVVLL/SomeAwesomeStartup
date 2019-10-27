from BasicModel import BasicModel


class film(BasicModel):
    _FIELDS_MAPPING = {
        "id": int,
        "film_id": int,
        "film_name": str,
        "description": str,
    }
    _TABLE = "FILMS_BLACKHOLE"

# something = film()
# something.fill_data({"film_id": 12132, "film_name": "Forrest_Gump", "description":"it is cool film"})
# print(something.__dict__)
# print(something._DATABASE)
# print(something._FIELDS_MAPPING.keys())
# print(something._TABLE)
# something._create_mapping (getattr(something,"film_id"))
