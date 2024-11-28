from flask import Flask, request, make_response, render_template, redirect, flash, url_for, get_flashed_messages

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


@app.route('/users/<int:id>')
def get_user(id):
    filtered_users = filter(lambda user: user['id'] == id, users)
    user = next(filtered_users, None)

    if user is None:
        return 'Page not found', 404

    return render_template('users/show.html', user=user)


@app.route('/users')
def get_users():
    return render_template('users/index.html', users=users)


app = Flask(__name__)
# устанавливаем секретный ключ для работы с сессиями
app.secret_key = "secret_key"


@app.post('/foo')
def foo_post():
    # Добавление флеш-сообщения.
    # Оно станет доступным только на следующий HTTP-запрос.
    # 'success' — тип флеш-сообщения. Используется при выводе для форматирования.
    # Например, можно ввести тип success и отражать его зеленым цветом. На Хекслете такого много.
    flash('This is a message', 'success')
    return redirect('/bar')


@app.get('/bar')
def bar_index():
    # Извлечение flash-сообщений, которые установлены на предыдущем запросе
    messages = get_flashed_messages(with_categories=True)
    print(messages)  # => [('success', 'This is a message')]
    return render_template(
        'bar.html',
        messages=messages,
    )
