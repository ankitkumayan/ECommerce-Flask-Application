import unittest
import sys
import os

# Add the parent directory of the app module to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route_invalid_method(self):
        response = self.app.post('/')
        self.assertEqual(response.status_code, 405)

if __name__ == '__main__':
    unittest.main()
