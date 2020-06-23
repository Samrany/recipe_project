""" Script to seed datatase."""
import os
import json
from random import choice, randint  
import crud
import model
import server



os.system('dropdb recipes')
os.system('createdb recipes')

# Enable loading data from JSON file
model.connect_to_db(server.app) 
model.db.create_all()


# Load recipe info from JSON file
with open('data/recipes.json') as f:
    recipes = json.loads(f.read())

recipes_in_db = []


for recipe in recipes:

	recipe_name, source_name, website, directions, image, servings, ingredients = (
		recipe['recipe_name'],
		recipe['source_name'],
		recipe['website'],
		recipe['directions'],
		recipe['image'],
		recipe['servings'],
		recipe['ingredients'])


	db_recipe = crud.create_new_recipe(recipe_name, source_name, website, 
									   directions, image, servings, ingredients)
	recipes_in_db.append(db_recipe)


# Create Test Users
users_in_db = []
ingredients_in_db = crud.all_ingredients()
for n in range(1,10):
	email = f'user{n}@test.com'
	password = 'test'
	first_name = f'first{n}'
	last_name = f'last{n}'
	user = crud.create_user(email, password, first_name, last_name)
	users_in_db.append(user)
	
	#create user_faves
	# for i in range(3):
	# 	random_recipe = choice(recipes_in_db)
	# 	random_user = choice(users_in_db)
	# 	random_ingredient = choice(ingredients_in_db)
	# 	crud.fave_recipe(random_user, random_recipe)
	# 	crud.no_go(random_user, random_ingredient)

