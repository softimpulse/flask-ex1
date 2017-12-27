from flask import Flask, request, url_for, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = ';lae4c'

toolbar = DebugToolbarExtension(app)


@app.route('/')
def index():
    return render_template('start.html')


@app.route('/hello/')
def hello_world():
    return render_template('hello.html')


@app.route('/hello/<name>')
def hello_world_name(name):
    return render_template('hello.html', name=name)


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
    return 'The about page <img src="%s">' % url_for('static', filename='test.jpg')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'POST'
    else:
        return 'GET'
