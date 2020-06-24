from unittest import TestCase
from server import app
from model import connect_to_db, db 
from flask import session
import crud
from seed_testdb import populate_example_data

class FlaskTestBasics(TestCase):
    """Flask tests."""

    def setUp(self):
        """Executed before every test."""

        #Get Flask test client
        self.client = app.test_client()

        #Show Flask errors that happen during tests
        app.config['TESTING'] = True


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
        connect_to_db(app, "postgresql:///testdb")

        # Create tables and add sample data
        db.create_all()
        populate_example_data()


    def tearDown(self):
        """Do at end of every test."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()


    def test_home_page(self):
        """Test recipes load on homepage"""

        result = self.client.get("/")

        self.assertIn(b"The Defined Dish", result.data)    


    def test_login(self):
        """Test create_login page."""

        result = self.client.post("/log_in_form",
                                  data={"e-mail": "user1@test.com", "password": "test"},
                                  follow_redirects=True)
        self.assertIn(b"Hi, First1", result.data)

    
    def test_create_user(self):
        """Test create_login page."""

        result = self.client.post("/users",
                                  data={"f_name": "Bob", "l_name":"Jones","e-mail": "bob.jones@gmail.com", "password": "test"},
                                  follow_redirects=True)
        self.assertIn(b"Hi, Bob", result.data)


    def test_recipe_details(self):
        """Test recipe details page"""

        result = self.client.get("/1")

        self.assertIn(b"When the oil starts to shimmer and the pot is hot", result.data)

    # def test_faves_page(self):
    #     """Test favorites page"""

    #     result = self.client.get("/faves")

    #     self.assertIn(b"TBD", result.data)


    # def test_logout(self):
    #     """Test logout"""

    #     result = self.client.get("/log_out", follow_redirects=True)

    #     self.assertIn(b"TBD", result.data)


    # def test_user_favorite_action(self):
    #     """Test user favoriting recipe"""

    #     result = self.client.post("/user_fave", data=)#NOT SURE WHAT TO DO FOR THIS ONE


    # def test_get_shopping_list(self):
    #     """Test shopping list feature"""
    #     result = self.client.post("/faves/get_shopping_list", data={"num_recipes":2}, 
    #                               follow_redirects=True)
    #     ##ADD SESSION DATA
    #     self.assertIn(b"TBD shopping list items", result.data)


if __name__ == "__main__":
    import unittest

    unittest.main()