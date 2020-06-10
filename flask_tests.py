from unittest import TestCase
from server import app
from model import connect_to_db, db #,example_data
from flask import session

class FlaskTestBasics(TestCase):
	"""Flask tests."""

	def setUp(self):
		"""Executed before every test."""

		#Get Flask test client
		self.client = app.test_client()

		#Show Flask errors that happen during tests
		app.config['TESTING'] = True

	def test_homepage(self):
		"""Test homepage."""

		result = self.client.get("/") 
		self.assertIn(b"")
		#coverage metrics. coverage.py
		#could cover if empty field in form or email incorrect