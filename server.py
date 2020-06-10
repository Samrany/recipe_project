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



@app.route('/<recipe_id>')
def recipe_details(recipe_id):
	recipe =crud.get_recipe_by_id(recipe_id)
	return render_template("recipe_details.html", recipe = recipe)

@app.route('/login') 
def login():
    """Show the login page."""
    return render_template("login.html")

@app.route('/create_login')
def create_login():
	return render_template("create_login.html")

@app.route('/users', methods = ['POST'])
def register_user():
	"""Create a new user."""
	email = request.form["email"] #work with a dict
	Assert e-mail is not None # works with other objects/formats as well
	password = request.form.get("password")
	first_name = request.form.get("f_name")
	last_name = request.form.get("l_name")
	user = crud.get_user_by_email(email)
	print(user)

	if user:
		flash('User already has an account. Login instead')
		return redirect("/login")
	else:
		crud.create_user(email, password, first_name, last_name)
		flash('Success!')
		return redirect("/")

if __name__ == '__main__':
	connect_to_db(app)
	app.run(host='0.0.0.0', debug=True)