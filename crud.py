"""CRUD operations."""

from model import db, User, Recipe, Fave_recipes, Ingredient, Recipe_ingredients, User_no_goes, connect_to_db

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
#connects to the database ^

def create_user(email, password, first_name, last_name):
    """Create and return a new user."""

    user = User(email=email, password=password, first_name = first_name, last_name = last_name)

    db.session.add(user)
    db.session.commit()

    return user


def add_new_ingredient(ingredient_name,dairy_free = True, gluten_free = True,
                        vegetarian = True, vegan = True, paleo = True):
    """Add new ingredient to db"""
    current_ingredient = Ingredient(ingredient_name = ingredient_name, 
                        dairy_free = dairy_free, gluten_free = gluten_free,
                        vegetarian = vegetarian, vegan = vegan, paleo = paleo)

    # float the metric amount

    db.session.add(current_ingredient)
    db.session.commit()

    return current_ingredient

def all_ingredients():
    """Return all ingredients."""

    return Ingredient.query.all()

def get_ingredient_id(ingredient_name):
    """Returns an ingredient id given the ingredient name"""

    current_ingredient = Ingredient.query.filter_by(ingredient_name = ingredient_name).one()
    current_id = current_ingredient.ingredient_id
    
    return current_id


def get_ingredient_name(ingredient_id):
    """Returns an ingredient name given the ingredient id"""

    current_ingredient = Ingredient.query.get(ingredient_id)
    current_name = current_ingredient.ingredient_name
    
    return current_name

def all_ingredients_by_name():
    """Return all ingredients by name in a list"""

    existing_ingredients = []
    ingredients = all_ingredients() # a list of objects
    for ingredient in ingredients:
        name = ingredient.ingredient_name
        existing_ingredients.append(name)

    return existing_ingredients


def add_needed_ingredient(recipe_id, ingredient_id, amount, metric = None, preparation = None):
    """Add ingredient in recipe to db"""
    current_needed_ingredient = Recipe_ingredients(recipe_id = recipe_id, ingredient_id = ingredient_id, 
                                                   amount = amount, metric = metric, preparation = preparation)
    # CAN CHANGE ID TO RECIPE AND INGREDIENT OBJECTS
    db.session.add(current_needed_ingredient)
    db.session.commit()

    return current_needed_ingredient


def create_new_recipe(recipe_name, source_name, website, directions, image, servings, ingredients): 
    """Create and return new recipes, add ingredients to database if not there, and add associated 
    ingredients in recipes where ingredients is a list of dictionary objects."""

    # Add recipe to db
    current_recipe = Recipe(recipe_name = recipe_name, source_name = source_name,
        website = website, directions = directions, image = image, servings = servings)
    db.session.add(current_recipe)
    db.session.commit()

    # get a list of existing ingredients in db and commit ingredients from recipe to db if not already in.
    existing_ingredients = all_ingredients_by_name() # REVISIT?
    current_ingredient_objects = all_ingredients()
    current_recipe_id = current_recipe.recipe_id

    for ingredient in ingredients: #ingredient is a dictionary
        name = ingredient.get('ingredient_name') #access key-value pair
        if name not in existing_ingredients:
            ingredient_id = add_new_ingredient(name).ingredient_id

        else:
            ingredient_obj = Ingredient.query.filter_by(ingredient_name = name).first() # QUERYING EVERYTIME. REVISIT
            ingredient_id = ingredient_obj.ingredient_id 
          ##### Doesn't account for any attributes of the ingredient nor ensure case consistency
        amount = ingredient.get('amount', None)
        metric = ingredient.get('metric', None) 
        preparation = ingredient.get('preparation', None)
        add_needed_ingredient(current_recipe_id, ingredient_id, amount, metric, preparation)


    return current_recipe


def all_users():
    """Returns all users."""

    return User.query.all()

def all_recipes():
    """Returns all recipes."""

    return Recipe.query.all()


def get_user_by_id(user_id):
    """Returns user object given a user_id"""
    user = User.query.get(user_id)
    return user

def get_user_by_email(email):
    user = User.query.filter_by(email = email).first()
    return user

def get_recipe_by_id(recipe_id):
    """Returns a recipe object given a recipe_id"""
    recipe = Recipe.query.get(recipe_id)
    
    return recipe


def get_user_faves(user_id):
    """Get favorated recipes associated with a user_id"""
    # user_faves = Fave_recipes.query.filter_by(user_id = user.user_id)
    user_faves = Fave_recipes.query.filter_by(user_id = user_id)

    return user_faves

def fave_recipe(user, recipe):
    """Save a favorite recipe to the db"""
    fave_recipe = Fave_recipes(user_id = user.user_id, recipe_id = recipe.recipe_id)

    db.session.add(fave_recipe)
    db.session.commit()

    return fave_recipe

def no_go(user, ingredient):
    """Save a favorite recipe to the db"""
    no_go = User_no_goes(user_id = user.user_id, ingredient_id = ingredient.ingredient_id)

    db.session.add(no_go)
    db.session.commit()

    return no_go