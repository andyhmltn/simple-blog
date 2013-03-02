# Imports
import sqlite3
from contextlib  import closing
from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash

# Configuration
DATABASE = '/tmp/simple-blog.db'
DEBUG = True
SECRET_KEY = 'arandomstringyoushouldchange'
USERNAME = 'admin'
PASSWORD = 'admin'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('db/schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
	g.db.close()

if __name__ == '__main__':
	app.run()