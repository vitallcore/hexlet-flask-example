from flask import Flask, render_template, request
from repository import PostsRepository

app = Flask(__name__)

repo = PostsRepository(50)


@app.route('/')
def index():
    return render_template('index.html')


@app.get('/posts')
def posts():
    per = 5
    page = request.args.get('page', 1, type=int)
    offset = (page - 1) * per
    all_posts = repo.content()
    posts_at_page = all_posts[offset:page * per]
    return render_template(
        'posts/index.html',
        page=page,
        posts=posts_at_page,
    )


@app.get('/posts/<slug>')
def get_post(slug):
    post = repo.find(slug)
    if not post:
        return 'Page not found', 404
    return render_template('posts/show.html', post=post)
