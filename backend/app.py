""" Main file for the Flask application """

from flask import Flask, g
from flask_cors import CORS
import sqlite3


app = Flask(__name__)
CORS(app)
app.config['DATABASE'] = 'db/excuses.db'

# Function to get a SQLite connection
def get_db():
    """ Open a new database connection if there is none yet """
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row

    return g.db


# Function to close the SQLite connection
@app.teardown_appcontext
def close_db(error):
    """ Close the database at the end of the request """
    db = g.pop('db', None)
    if db is not None:
        db.close()


from routes import *


if __name__ == '__main__':
    # app.run(debug=False, host='0.0.0.0')
    app.run(debug=True)
