#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    max_batches = -1
    for key in recipe:
        if key in ingredients:
            if ingredients[key] // recipe[key] < max_batches or max_batches == -1:
                max_batches = ingredients[key] // recipe[key]
        else:
            max_batches = 0
    return max_batches



if __name__ == '__main__':
    # Change the entries of these dictionaries to test 
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))