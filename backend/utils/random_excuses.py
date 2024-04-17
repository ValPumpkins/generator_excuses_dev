""" Module to get a random excuse from the db """

from app import get_db


def get_random_excuse():
    """ Get a random excuse from the db """
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT message FROM excuses ORDER BY RANDOM() LIMIT 1')
    row = cursor.fetchone()

    if row:
        # Retrieve only the message column
        message = row['message']
        return message
    else:
        return None
