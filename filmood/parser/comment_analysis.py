import json
import re
from filmood import *
from filmood.models import *


with open('filmood/parser/moods.json') as file:
    mood_words = json.loads(file.read())['words']

sep = '\. |\.|, |,|; |;| |\n|\(|\)|"|\?|!'
films = Film.query.all()#[20000:21425]#21425
for film in films:
    cur_film_moods = {}
    sum = 0
    for comment in film.comments:
        comment_words = re.split(sep, comment.content)
        for word in comment_words:
            if mood_words.get(word):
                mood = mood_words.get(word)
                sum += 1
                if cur_film_moods.get(mood):
                    cur_film_moods[mood] += 1
                else:
                    cur_film_moods[mood] = 1
    if sum != 0:
        for cur_film_mood in cur_film_moods:
            mood = Mood.query.filter_by(name=cur_film_mood).first()
            value = cur_film_moods[cur_film_mood] / sum
            db.session.execute(
                film_moods.insert().values(film_id=film.id, mood_id=mood.id, value=value)
            )
            db.session.commit()

    print(film.id)