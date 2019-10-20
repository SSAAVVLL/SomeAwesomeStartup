from BasicModel import BasicModel


class Comment(BasicModel):
    _FIELDS_MAPPING = {
        "id_resourse": int,
        "id_film": int,
        "text": str
    }


something = Comment("Baba")
something.fill_data({"id_resource": 123 , "id_film": 151, "text":"woobster"})
print(something.__dict__)
print(something._DATABASE)