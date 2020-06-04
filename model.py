from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

    fave_recipes = db.relationship("Fave_recipes")
    user_no_goes = db.relationship("User_no_goes")

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

class Recipe(db.Model):
	"""A recipe."""

	__tablename__ = 'recipes'

    recipe_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    recipe_name = db.Column(db.String, nullable=False)
    source_name = db.Column(db.String)
    website = db.Column(db.String)
    directions = db.Column(db.Text)
    image = db.Column(db.String)
    servings = db.Column(db.Integer)

    fave_recipes = db.relationship("Fave_recipes")
    recipe_ingredients = db.relationship("Recipe_ingredients")

    def __repr__(self):
        return f'<recipe id={self.recipe_id} name={self.recipe_name}>'

class Fave_recipes(db.Model):
	"""Users favorite recipes."""

	__tablename__ = 'fave_recipes'

    fave_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))

    user = db.relationship("User")
    recipe = db.relationship("Recipe")


    def __repr__(self):
        return f'<recipe={self.recipe_id.recipe_name} user={self.user.email}>'


class Ingredient(db.Model):
	"""Ingredients and their attributes"""

	__tablename__ = 'ingredients'

    ingredient_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)	
    ingredient_name = db.Column(db.Boolean, db.default = True)
    dairy_free = db.Column(db.Boolean, db.default = True)
    gluten_free = db.Column(db.Boolean, db.default = True)
    vegetarian = db.Column(db.Boolean, db.default = True)
    vegan = db.Column(db.Boolean, db.default = True)
    paleo = db.Column(db.Boolean, db.default = True)

    recipe_ingredients = db.relationship("Recipe_ingredients")
    user_no_goes = db.relationship("User_no_goes")

    def __repr__(self):
        return f'<id={self.ingredient_id} ingredient={self.ingredient_name}>'

class Recipe_ingredients(db.Model):
	"""Ingredients with measurements as listed in recipes. """

	__tablename__ = 'recipe_ingredients'

    key = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.ingredient_id'))
    amount = db.Column(db.Float, nullable = False)
    metric = db.Column(db.String) # should Metric be another table?
    preparation = db.Column(db.String)

    ingredient = db.relationship("Ingredient")
    recipe = db.relationship("Recipe")


class User_no_goes(db.Model):
	"""User ingredient preferences to exclude. """

	__tablename__ = 'user_no_goes'

    user_pref_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.ingredient_id'))
    ##### might add dietary preferences or relate dietary preferences to more ingredients here

    user = db.relationship("User")
    ingredient = db.relationship("Ingredient") 


def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    # flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app


    connect_to_db(app)
