"""Server for recipe app."""

from flask import (Flask, render_template, request, 
				   flash, session, redirect, jsonify)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
from random import sample
import send_email



app = Flask(__name__)
app.secret_key = "Shira"
app.jinja_env.undefined = StrictUndefined

@app.route('/') 
def homepage():
    """Show the homepage."""
    recipes = crud.all_recipes()
    ingredients = crud.all_ingredients_by_name()
    return render_template("homepage.html", recipes = recipes, ingredients = ingredients)

@app.route('/<int:recipe_id>')
def recipe_details(recipe_id):
	recipe = crud.get_recipe_by_id(recipe_id)
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
	email = request.form["e-mail"] #work with a dict
	# Assert e-mail is not None # works with other objects/formats as well
	password = request.form.get("password") ################
	first_name = request.form.get("f_name")
	last_name = request.form.get("l_name")
	user = crud.get_user_by_email(email)


	if user:
		flash('User already has an account. Login instead')
		return redirect("/login")

	else:
		user = crud.create_user(email, password, first_name, last_name)
		session['logged_in'] = True
		session['name'] = user.first_name.title()
		session['user_id'] = user.user_id
		session['email'] = user.email

		return redirect("/")


@app.route('/log_in_form', methods = ['POST'])
def check_login():
	"""Log in User"""
	email = request.form["e-mail"]
	password = request.form["password"]
	user = crud.get_user_by_email(email)
	
	if user and user.password == password: #THIS WHOLE SET IS A REPEAT. PUT IN A SEPARATE FUNCTION?
		session['logged_in'] = True
		session['name'] = user.first_name.title()
		session['user_id'] = user.user_id
		session['email'] = user.email
	
		return redirect("/")
	
	else:
		flash("Wrong password. Try again.")
		
		return redirect("/login")		



@app.route('/faves')
def show_favorites():
	user_id = session.get('user_id')
	favorites = crud.get_user_faves(user_id)
	user = crud.get_user_by_id(user_id) # SHOULDNT I BE ABLE TO ACCESS object VIA SESSION?
	name = user.first_name.title() 
	return render_template("user_favorites.html", favorites = favorites, name = name)

@app.route('/log_out')
def log_out():
	# print(session.keys)
	session.clear()
	# print()
	# print(session.keys)
	return redirect("/")


@app.route('/user_fave', methods = ['POST','GET'])
def user_fave():
	recipe_id = request.form.get('recipe_id') 
	user_id = session['user_id']

	# if Fave_recipes.query.filter_by(user_id=user_id, recipe_id = recipe_id).all:
	# 	print("RETURNING FALSE")
	# 	return jsonify({'status': False })

	# else:
	#(Above functionality was giving me issues so reverted back for now. May instead filter recipes
	# on homepage that user can like by showing those that aren't in user favorites yet)
	crud.fave_recipe(user_id, recipe_id)
	print("RETURNING TRUE")
	return jsonify({'status': True })


@app.route('/faves/get_shopping_list', methods = ['POST', 'GET'])
def get_shopping_list():
	
	num_recipes = int(request.form["num_recipes"])
	user_id = session['user_id'] 
	all_faves = crud.get_user_faves(user_id)
	recipes_to_cook = sample(all_faves,num_recipes)
	
	ingredients_needed = [] 
	for fave_recipe in recipes_to_cook:
		ingredients = fave_recipe.recipe.recipe_ingredients
		for ingredient in ingredients:
			ingredients_needed.append(ingredient)

	send_email.send_email(session['email'], session['name'], recipes_to_cook, ingredients_needed)
	return render_template("shopping_list.html", recipes_to_cook = recipes_to_cook, ingredients_needed = ingredients_needed)


if __name__ == '__main__':
	connect_to_db(app)
	app.run(host='0.0.0.0', debug=True)