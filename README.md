# flask-ex1

Before doing anything set up a virtual environment:
```
cd A_NICE_NEW_FOLDER
python3 -m venv .
. bin/activate # activates new env, adds also envname to prompt ...
pip install flask
```

Simple Flask example, starts with 

```
export FLASK_APP=hello.py
export FLASK_DEBUG=1
flask run 
```
and visit http://127.0.0.1:5000/

you can add `--host=0.0.0.0` to make server accessibe from other computers. 

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

## For debugging use also flask-debugtoolbar

https://flask-debugtoolbar.readthedocs.io/en/latest/

```
pip install flask-debugtoolbar
```

and in the code add 

```
from flask_debugtoolbar import DebugToolbarExtension

....

app.config['SECRET_KEY'] = ';lae4c'
toolbar = DebugToolbarExtension(app)
```

which does nothing if app.debug==False but otherwise adds a nice toolbar

