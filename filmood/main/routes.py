from flask import render_template, url_for, request
from filmood import app


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html', title="Our Team")



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

