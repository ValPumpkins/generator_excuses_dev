""" UnitTest for Flask app """

import unittest
from app import app, get_db, close_db


class TestFlaskApp(unittest.TestCase):
    """ Class to test the Flask app """
    def setUp(self):
        """ Set up the test environment """
        app.testing = True
        self.app = app.test_client()

    def test_get_db(self):
        """ Test the get_db function """
        with app.app_context():
            db = get_db()
            self.assertIsNotNone(db)
            self.assertTrue(hasattr(db, 'execute'))
            self.assertTrue(hasattr(db, 'commit'))

    def test_close_db(self):
        """ Test the close_db function """
        with app.app_context():
            db = get_db()
            close_db(None)
            self.assertFalse(hasattr(app, 'db'))


if __name__ == '__main__':
    unittest.main()
