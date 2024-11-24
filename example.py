from flask import Flask, request, make_response, render_template

# Это callable WSGI-приложение
app = Flask(__name__)


@app.route('/')
def hello_world():
    print(request.headers)  # Выводит все заголовки
    return 'Welcome to Flask!'


@app.get('/users')
def users_get():
    return 'GET /users'


@app.post('/users')
def users_post():
    return 'POST /users'


@app.route('/json/')
def json():
    return {'json': 42}  # Возвращает тип application/json


@app.route('/html/')
def html():
    return render_template('index.html')  # Возвращает тип text/html


@app.errorhandler(404)
def not_found(error):
    return 'Oops!', 404
