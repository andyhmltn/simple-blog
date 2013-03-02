# Imports
import sqlite3
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

if __name__ == '__main__':
	app.run()