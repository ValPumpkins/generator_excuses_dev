from flask import Flask, g


app = Flask(__name__)
app.config['DATABASE'] = 'db/excuses.db'

# Fonction pour ouvrir une connexion SQLite
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()


from routes import *


if __name__ == '__main__':
    app.run(debug=True)
