from flask import Flask, render_template
app = Flask(__name__,
            template_folder='templates',
            static_url_path='',
            static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')


app.run()
