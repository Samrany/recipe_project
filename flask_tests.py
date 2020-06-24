from unittest import TestCase
from server import app
from model import connect_to_db, db #,example_data
from flask import session
import crud

class FlaskTestBasics(TestCase):
    """Flask tests."""

    def setUp(self):
        """Executed before every test."""

        #Get Flask test client
        self.client = app.test_client()

        #Show Flask errors that happen during tests
        app.config['TESTING'] = True



    # def test_homepage(self):
    #   """Test homepage."""

    #   result = self.client.get("/") 
    #   self.assertIn(b"Explore New Recipes")
    #     #coverage metrics. coverage.py
    #     #could cover if empty field in form or email incorrect

    def test_login(self):
        """Test login page."""

        result = self.client.get("/login") 
        self.assertIn(b"Login", result.data)
        #coverage metrics. coverage.py
        #could cover if empty field in form or email incorrect


class FlaskTestsDatabase(TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        # os.system('createdb testdb')
        connect_to_db(app, "postgresql:///testdb")

        # Create tables and add sample data
        db.create_all()
        # example_data()



    def tearDown(self):
        """Do at end of every test."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()



    def test_create_user(self):
        """Test create_login page."""

        result = self.client.post("/users",
                                  data={"f_name": "Bob", "l_name":"Jones","e-mail": "bob.jones@gmail.com", "password": "test"},
                                  follow_redirects=True)
        self.assertIn(b"Hi, Bob", result.data)

    

if __name__ == "__main__":
    import unittest

    unittest.main()