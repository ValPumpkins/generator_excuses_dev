""" Test the API routes """

import unittest
from app import app, get_db
import os


class TestAPIRoutes(unittest.TestCase):
    """ Class to test the API routes """
    def setUp(self):
        """ Set up the test """
        app.testing = True
        self.app = app.test_client()

        app.config['DATABASE'] = 'test_excuses.db'

        with app.app_context():
            db = get_db()
            db.execute('''
                CREATE TABLE IF NOT EXISTS excuses (
                    id INTEGER PRIMARY KEY,
                    http_code INTEGER NOT NULL,
                    tag TEXT NOT NULL,
                    message TEXT NOT NULL
                )
            ''')
            db.execute(
                "INSERT INTO excuses (http_code, tag, message) VALUES (200, 'test_tag', 'test_message')")
            db.commit()

    def tearDown(self):
        """ Tear down the test """
        with app.app_context():
            db = get_db()
            db.execute('DELETE FROM excuses')
            db.commit()

        if os.path.exists('test_excuses.db'):
            os.remove('test_excuses.db')

    def test_all_excuses_route(self):
        """ Test the /api/excuses route """
        response = self.app.get('/api/excuses')
        self.assertEqual(response.status_code, 200)

    def test_create_excuse_route(self):
        """ Test the /api/create route """
        new_excuse = {'tag': 'test_tag', 'message': 'test_message'}
        response = self.app.post('/api/create', json=new_excuse)
        self.assertEqual(response.status_code, 201)

    def test_create_excuse_route_missing_data(self):
        """ Test the /api/create route with missing data """
        missing_data = {'tag': 'test_tag'}
        response = self.app.post('/api/create', json=missing_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Missing datas', response.data)

    def test_random_route(self):
        """ Test the /api/random route """
        response = self.app.get('/api/random')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
