import sqlite3
import random


def get_random_excuse():
    connection = sqlite3.connect('db/excuses.db')
    cursor = connection.cursor()
    cursor.execute('SELECT excuse FROM excuses ORDER BY RANDOM() LIMIT 1')
    excuse = cursor.fetchone()[0]
    connection.close()
    
    return excuse
