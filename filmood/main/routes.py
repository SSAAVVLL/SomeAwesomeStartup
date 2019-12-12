from flask import render_template, url_for, request
from filmood import app
from filmood.models import *
from marshmallow import ValidationError
import json


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/films', methods=['GET'])
def films():
    min_value = 0.2
    mood_emoji = ['😊', '😢', '😱', '😲', '😍', '😰', '🤔']
    params = request.args
    if params.get('moods'):
        mood_id = int(params.get('moods'))
        page = 12
        page_num = int(params.get('page')) if params.get('page') else 1
        try:
            mood = Mood.get(mood_id)
        except ValidationError:
            return render_template('index.html')
        val_c = film_moods.c.value
        mood_c = film_moods.c.mood_id
        films = Film.query.join(film_moods).filter(mood_c==mood.id).filter(
            val_c > min_value).order_by(val_c.desc()).all()[page*(page_num - 1):page*page_num]
        films_moods = {}
        films_emojis = {}
        film_ids = []
        for film in films:
            film_ids.append(film.id)
        moods = db.session.execute(film_moods.select().where(
            film_moods.c.film_id.in_(film_ids)).order_by(
                film_moods.c.film_id.asc()).order_by(film_moods.c.value.desc())).fetchall()
        i = 0
        for i in range(len(moods)):
            if not films_moods.get(moods[i][0]):
                films_moods[moods[i][0]] = moods[i:i+3]
                emoji = {}
                for mood in moods[i:i+3]:
                    emoji[mood[1]] = mood_emoji[mood[1] - 1]
                films_emojis[moods[i][0]] = emoji
                i += 3
            else:
                i += 1
            
            
            
            

        return render_template('index.html', films=films, 
            films_moods=films_moods, films_emojis=films_emojis, cur_emoji=mood_emoji[mood_id - 1]) 
    return render_template('index.html')





# @app.route('/auth/register', methods=['POST'])
# def register():
#     if request.method == 'POST':
#         params = request.json
#         print(params)

#         return '123123'


# @app.route('/auth/signin', methods=['POST'])
# def sign_in():
#     if request.method == 'POST':
#         params = request.json
#         print(params)
#         login = params['login']
#         password = params['password']
#         return answer(login, password)

