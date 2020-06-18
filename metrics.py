import os
import requests


# https://api.spoonacular.com/recipes/convert?ingredientName=flour&sourceAmount=2.5&sourceUnit=cups&targetUnit=grams&apiKey=18397f4a11fc4b80b43dbd6453eba646

def convert_metrics(ingredientName, sourceAmount, sourceUnit, targetUnit):
	url = 'https://api.spoonacular.com/recipes/convert?'
	SPOONACULAR_KEY = os.environ.get("SPOONACULAR")

	payload = {'ingredientName': ingredientName,
				'sourceAmount': sourceAmount,
				'soureUnit': sourceUnit,
				'targetUnit': targetUnit,
				'apiKey': SPOONACULAR_KEY}

	
	response = requests.get(url, params=payload)
	print(response.url)

	conversion = response.json()
	print(conversion)





# if response.status_code == 200:
#     print('Success!')
# elif response.status_code == 404:
#     print('Not Found.')

# if response:
#     print('Success!')
# else:
#     print('An error has occurred.')






# for ingredient in list:
	#if ingredient in dictionary:
		#if metrics don't match:
			#do some conversion, TBD:
		# add amounts together and change amount value 
	#else:
		# append to list as dictionary object {plain ingredient object:[{amount: }{metric: }]}

#??? What about where metric = none. Change none = unit as default?

#converion function:
# function(amt1, metric1, amt2, metric2)
# return 




