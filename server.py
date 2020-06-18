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
	"""Show full recipe details for a specific recipe."""
	recipe = crud.get_recipe_by_id(recipe_id)
	return render_template("recipe_details.html", recipe = recipe)

@app.route('/login') 
def login():
    """Show the login page."""
    return render_template("login.html")


@app.route('/create_login')
def create_login():
	"""Show create login page."""

	return render_template("create_login.html")


@app.route('/users', methods = ['POST'])
def register_user():
	"""Create a new user."""

	email = request.form["e-mail"] #work with a dict
	# Assert e-mail is not None # works with other objects/formats as well
	password = request.form["password"]
	first_name = request.form["f_name"]
	last_name = request.form["l_name"]
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
	"""Log in User if account previously created"""
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
	"""Show a user's favorite recipes"""
	user_id = session.get('user_id')
	favorites = crud.get_user_faves(user_id)
	user = crud.get_user_by_id(user_id) 
	name = user.first_name.title() 

	return render_template("user_favorites.html", favorites = favorites, name = name)

@app.route('/log_out')
def log_out():
	"""Log out a user and clear session"""

	session.clear()

	return redirect("/")


@app.route('/user_fave', methods = ['POST','GET'])
def user_fave():
	"""Allow user to favorite a recipe"""
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
	"""Show and email shopping list based on number of recipes chosen"""
	
	num_recipes = int(request.form["num_recipes"])
	user_id = session['user_id'] 
	user_name = session['name']
	all_faves = crud.get_user_faves(user_id)

	#Ensure a user can't try to create a shopping list for more recipes than in favorites
	if num_recipes > len(all_faves):
		flash(f"You haven't favorited that many recipes yet! Choose {len(all_faves)} or lower, or add more favorites! ")
		return redirect ("/faves")
		# change from html flash to JS Alert?
	
	#If ok, output recipe links and ingredient shopping list 
	else:
		recipes_to_cook = sample(all_faves,num_recipes)
		ingredients_needed = []
		shopping_list_dict = {}

		for fave_recipe in recipes_to_cook:

			recipe_ingredients = fave_recipe.recipe.recipe_ingredients
	
			for recipe_ingredient in recipe_ingredients:
				
				# #ADDING TO LIST TO OUTPUT - OLD
				# ingredients_needed.append(recipe_ingredient)

				#REFACTORING INTO DICTIONARY INSTEAD OF LIST
				if recipe_ingredient.ingredient in shopping_list_dict:
					if shopping_list_dict[recipe_ingredient.ingredient]['metric'] != recipe_ingredient.metric:
						print("They don't match")
						#DO METRIC CONVERSION

					# Add amounts
					print(f"{recipe_ingredient.ingredient} already in list")
					print(f"amount was: {shopping_list_dict[recipe_ingredient.ingredient]['amount']}")
					print(f"adding {recipe_ingredient.amount}")
					shopping_list_dict[recipe_ingredient.ingredient]['amount'] += recipe_ingredient.amount
					print(f"amount now is: {shopping_list_dict[recipe_ingredient.ingredient]['amount']}")
				else:
					shopping_list_dict[recipe_ingredient.ingredient] = {'amount': recipe_ingredient.amount, 'metric': recipe_ingredient.metric}
					print(f"{recipe_ingredient.ingredient} added")

		print(shopping_list_dict)
		for item in shopping_list_dict:
			print(item.ingredient_name)
			print(shopping_list_dict[item]['amount'])
			print(shopping_list_dict[item]['metric'])



		# temporarily passing my e-mail instead of session['email'].
		
		#Calling send e-mail function
		# send_email.send_email('shira.amrany@gmail.com', session['name'], recipes_to_cook, ingredients_needed)
		
		#Returning same info to shopping list page
		# return render_template("shopping_list.html", recipes_to_cook = recipes_to_cook, ingredients_needed = ingredients_needed)
		return render_template("shopping_list.html", recipes_to_cook = recipes_to_cook, shopping_list_dict = shopping_list_dict)

if __name__ == '__main__':
	connect_to_db(app)
	app.run(host='0.0.0.0', debug=True)