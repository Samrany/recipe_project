import os
import requests


def spoonacular_metric_conversion(ingredientName, sourceAmount, sourceUnit, targetUnit):
	"""Uses Spoonacular API to convert the amount of an ingredient given a different measuring unit
	and returns converted amount"""

	url = 'https://api.spoonacular.com/recipes/convert?'
	SPOONACULAR_KEY = os.environ.get("SPOONACULAR")

	payload = {'ingredientName': ingredientName,
				'sourceAmount': sourceAmount,
				'soureUnit': sourceUnit,
				'targetUnit': targetUnit,
				'apiKey': SPOONACULAR_KEY}

	
	response = requests.get(url, params=payload)
	conversion = response.json()
	print(response.url)
	output_amount = conversion['targetAmount']
	print(conversion)
	print(output_amount)
	# NEED TO HANDLE SITUATIONS WHERE OUTPUT IS NONE

	return output_amount



def check_if_same_unit(unit1, unit2):
	"""Checks if unit1 and unit2 are plural and singular versions of same metric"""
	#ADD in functionality to comapre singular to plural
	return (unit1 == unit2)



def create_shopping_list(recipes_to_cook):
	"""Takes in a list of recipe objects and returns a shopping list"""

	shopping_list_dict = {}

	#looping over each recipe object and acessing each recipe's recipe_ingredients
	for fave_recipe in recipes_to_cook:
		recipe_ingredients = fave_recipe.recipe.recipe_ingredients
		
		#looping over list of recipe_ingredients to access the ingredient object related to each
		for recipe_ingredient in recipe_ingredients:
			
			#check if ingredient already in shopping list and evaluate if metrics need conversion then add amounts
			if recipe_ingredient.ingredient in shopping_list_dict:
				existing_amount_in_dict= shopping_list_dict[recipe_ingredient.ingredient]['amount']
				existing_metric_in_dict = shopping_list_dict[recipe_ingredient.ingredient]['metric']

				current_metric_evaluated = recipe_ingredient.metric
				current_amount_to_add = recipe_ingredient.amount

				print(f"{recipe_ingredient.ingredient} already in list")
				print(f"amount was: {existing_amount_in_dict}")
				if check_if_same_unit(existing_metric_in_dict, current_metric_evaluated):
					existing_amount_in_dict += current_amount_to_add		

		
				# Add amounts for ingredient where metric is same
				else:
					converted_amount_to_add = spoonacular_metric_conversion(recipe_ingredient.ingredient,
																	        current_amount_to_add,
																	        current_metric_evaluated,
																	        existing_metric_in_dict
																	        )

					existing_amount_in_dict += converted_amount_to_add

				print(f"amount now is: {existing_amount_in_dict}")

			else:
				#add ingredient to shopping list if not existing
				shopping_list_dict[recipe_ingredient.ingredient] = {'amount': recipe_ingredient.amount, 'metric': recipe_ingredient.metric}
				print(f"{recipe_ingredient.ingredient} added")


	return shopping_list_dict			



