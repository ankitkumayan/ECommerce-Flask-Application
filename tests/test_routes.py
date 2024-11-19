import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True  # Enable testing mode

    def test_home_route_invalid_method(self):
      #Test if an invalid HTTP method on the home route returns a 405 error.
        response = self.app.post('/')
        self.assertEqual(response.status_code, 405)

if __name__ == '__main__':   #main
    unittest.main()
