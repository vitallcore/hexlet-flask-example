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


@app.route('/foo')
def foo():
    response = make_response('foo')
    # Устанавливаем заголовок
    response.headers['X-Parachutes'] = 'parachutes are cool'
    # Меняем тип ответа
    response.mimetype = 'text/plain'
    # Задаем статус
    response.status_code = 418
    # Устанавливаем cookie
    response.set_cookie('foo', 'bar')
    return response


@app.post('/users')
def users():
    return 'Users', 302


@app.route('/courses/<id>')
def courses_show(id):
    return f'Course id: {id}'
