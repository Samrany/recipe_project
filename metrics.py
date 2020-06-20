import os
import requests


def spoonacular_metric_conversion(ingredientName, sourceAmount, sourceUnit, targetUnit):
	"""Uses Spoonacular API to convert the amount of an ingredient given a different measuring unit
	and returns converted amount"""

	url = 'https://api.spoonacular.com/recipes/convert?'
	SPOONACULAR_KEY = os.environ.get("SPOONACULAR")

	payload = {'ingredientName': ingredientName,
				'sourceAmount': sourceAmount,
				'sourceUnit': sourceUnit,
				'targetUnit': targetUnit,
				'apiKey': SPOONACULAR_KEY}

	try:
		response = requests.get(url, params=payload)
		conversion = response.json()
		output_amount = conversion['targetAmount']
		print(response.url)
		print(conversion)
		print(output_amount)
		return output_amount
	
	except:
		#Technically this means the ingredient amount won't be added to the shopping list
		return 0
	



def check_if_same_unit(unit1, unit2):
	"""Checks if strings unit1 and unit2 are the same metric or plural/singular versions of same metric"""

	if unit1 == unit2 or unit1 == unit2 + "s" or unit2 == unit1 + "s":
		return True



def create_shopping_list(recipes_to_cook):
	"""Takes in a list of recipe objects and returns a shopping list"""

	shopping_list_dict = {}


	[1,2,3,4,5]
	lst = []
	for i in range(5):
		lst.append(i + 1)

	lst = [i + 1 for i in range(5)]

	recipe_ingredients = [fave_recipe.recipe.recipe_ingredients for fave_recipe in recipes_to_cook]

	#looping over each recipe object and acessing each recipe's recipe_ingredients
	for fave_recipe in recipes_to_cook:
		# recipe_ingredients = fave_recipe.recipe.recipe_ingredients
		
		#looping over list of recipe_ingredients to access the ingredient object related to each
		for recipe_ingredient in fave_recipe.recipe.recipe_ingredients:
			ingredient = recipe_ingredient.ingredient
			
			#check if ingredient already in shopping list 
			if ingredient not in shopping_list_dict:
				#add ingredient to shopping list if not existing
				shopping_list_dict[ingredient] = {'amount': recipe_ingredient.amount, 'metric': recipe_ingredient.metric}

			else:
				# evaluate if metrics need conversion then add amounts
				existing_amount_in_dict= shopping_list_dict[ingredient]['amount']
				existing_metric_in_dict = shopping_list_dict[ingredient]['metric']
				current_metric_evaluated = recipe_ingredient.metric
				current_amount_to_add = recipe_ingredient.amount

				print(f"{ingredient} already in list")
				print(f"amount was: {existing_amount_in_dict}")
				
				if check_if_same_unit(existing_metric_in_dict, current_metric_evaluated):
					existing_amount_in_dict += current_amount_to_add		
		
				# Add amounts for ingredient where metric is same
				else:
					converted_amount_to_add = spoonacular_metric_conversion(ingredient,
																	        current_amount_to_add,
																	        current_metric_evaluated,
																	        existing_metric_in_dict
																	        )

					existing_amount_in_dict += converted_amount_to_add

				print(f"amount now is: {existing_amount_in_dict}")




	return shopping_list_dict			



