from flask import jsonify, g
from app import app
import sqlite3


# Fonction pour obtenir une connexion SQLite
def get_db():
    return sqlite3.connect(app.config['DATABASE'])

# Route API pour récupérer toutes les excuses
@app.route('/api/excuses')
def all_excuses():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM excuses')
    excuses = cursor.fetchall()
    # Crée une liste de dictionnaires pour chaque excuse avec les noms de colonnes comme clés
    excuses_list = [
        {
            'id': row[0],
            'http_code': row[1],
            'tag': row[2],
            'message': row[3]}
        for row in excuses
    ]

    return jsonify(excuses=excuses_list)
