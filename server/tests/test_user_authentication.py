import unittest
import unittest
import os
import json
from server.app import create_app, DB

class UserAuthenticationTests(unittest.TestCase):
    """This class represents user authentication test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            DB.create_all()

    def test_user_signup(self):
        """Test user can create account"""
        user_details = {
            'username': 'name',
            'full_name': 'full name',
            'email': 'email',
            'password': 'password'
        }
        res = self.client().post('/api/user/signup', data=user_details)
        self.assertEqual(res.status_code, 200)

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            DB.session.remove()
            DB.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
