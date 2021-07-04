from schema.user import UserCreate
from schema.recipe import RecipeCreate


def get_user():
    user = UserCreate(
                        email='hello@fresh.com',
                        name='hellofresh',
                        password='hello')

    return user


def get_recipe():
    ingredients = {
        'apple': '34gm',
        'banana': '0.4 kg'
    }

    nutrition = {
        'sugar': '34gm',
        'Energy': '345Kcal'
    }
    preptime = 45
    name = 'fruits'
    difficulty = 'easy'
    notincluded = ['tomato souce', 'mayo']
    instruction = ['chop fruit', 'mix fruit']
    recipe = RecipeCreate(
        ingredients=ingredients,
        preptime=preptime,
        name=name,
        difficulty=difficulty,
        notincluded=notincluded,
        instruction=instruction,
        nutrition=nutrition)

    return recipe
