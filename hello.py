from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Main page'


@app.route('/hello/')
def hello_world():
    return 'Hello world'


@app.route('/hello/<name>')
def hello_world_name(name):
    return 'Hello %s' % name


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'
