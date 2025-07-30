from recipe import Recipe
from data_manager import save_recipes_to_json

def create_recipe(title):
   new_recipe = Recipe(title)
   new_recipe.set_ingredients(test_ingredients)
   new_recipe.set_instructions(test_instructions)
   new_recipe.set_recipe_tags(test_tags)
   return new_recipe

test_title = "3-Ingredient Stovetop Mac and Cheese Recipe"
test_ingredients = """6 ounces (170 g) elbow macaroni
Salt 
6 ounces (180 ml) evaporated milk\n6 ounces (170 g) grated mild or medium cheddar cheese, or any good melting cheese, such as Fontina, Gruyère, or Jack"""
test_instructions = """Place macaroni in a medium saucepan or skillet and add just enough cold water to cover.Add a pinch of salt and bring to a boil over high heat, stirring frequently.
Continue to cook, stirring, until water has been almost completely absorbed and macaroni is just shy of al dente, about 6 minutes.
Immediately add evaporated milk and bring to a boil.
Add cheese.
Reduce heat to low and cook, stirring continuously, until cheese is melted and liquid has reduced to a creamy sauce, about 2 minutes longer.
Season to taste with more salt and serve immediately."""
test_tags = """Kenji
Cheese"""

def main():
  test_recipe = create_recipe(test_title)
  test_recipe.print_recipe_card()
  test_recipe.recipe_to_dictionary()
  recipe_dict = test_recipe.recipe_to_dictionary()
  save_data = { "recipes": [recipe_dict] }
  save_recipes_to_json(save_data)




if __name__ == "__main__":
    main()