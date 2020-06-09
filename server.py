"""Server for recipe app."""

from flask import (Flask, render_template, request, 
				   flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/') 
def homepage():
    """Show the homepage."""
    recipes = crud.all_recipes()
    ingredients = crud.all_ingredients_by_name()
    return render_template("homepage.html", recipes = recipes, ingredients = ingredients)

@app.route('/login') 
def login():
    """Show the login page."""
    return render_template("login.html")


@app.route('/<recipe_id>')
def recipe_details(recipe_id):
	recipe =crud.get_recipe_by_id(recipe_id)
	return render_template("recipe_details.html", recipe = recipe)

if __name__ == '__main__':
	connect_to_db(app)
	app.run(host='0.0.0.0', debug=True)