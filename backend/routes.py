""" All api routes are defined here """

from flask import jsonify, request
from app import app, get_db
from utils.random_excuses import get_random_excuse
import sqlite3


# Retrieve all excuses from the db
@app.route('/api/excuses', methods=['GET'])
def all_excuses():
    """ API route to get the list of all excuses in db """
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM excuses')
    excuses = cursor.fetchall()

    # Create a list of dictionaries with the data
    excuses_list = [
        {
            'id': row[0],
            'http_code': row[1],
            'tag': row[2],
            'message': row[3]
        }
        for row in excuses
    ]

    return jsonify(excuses_list)


# Create a new excuse
@app.route('/api/create', methods=['POST'])
def create_excuse():
    """ API route to add a new excuse to the db """
    data = request.json
    tag = data.get('tag')
    message = data.get('message')

    http_code = 100

    # Check if all datas are present
    if tag is None or message is None:
        return jsonify({'Error': 'Missing datas'}), 400

    db = get_db()
    cursor = db.cursor()

    try:
        # Check if the tag is already used
        while True:
            cursor.execute(
                'SELECT * FROM excuses WHERE http_code = ?', (http_code,))
            existing_excuse = cursor.fetchone()

            # If http_code is already used, increment it
            if existing_excuse:
                http_code += 1
            else:
                # Insert the new excuse in the db using a parametrized query
                cursor.execute('INSERT INTO excuses (http_code, tag, message) VALUES (?, ?, ?)',
                               (http_code, tag, message))
                db.commit()

                return jsonify({'http_code': http_code, 'message': 'Success !'}), 201
    except sqlite3.IntegrityError:
        # Handle the case where tag or message violates integrity constraints
        return jsonify({'Error': 'Integrity constraint violation'}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({'Error': str(e)}), 500


# Get a random excuse
@app.route('/api/random', methods=['GET'])
def random_excuse():
    """ API route to get a random excuse """
    excuse = get_random_excuse()

    if excuse:
        return jsonify(excuse), 200
    else:
        return jsonify({'error': 'No excuses available'}), 404
