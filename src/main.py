from recipe import Recipe


test_recipe = Recipe("3-Ingredient Stovetop Mac and Cheese Recipe",
                     "Kenji 3 ingredient Mac&Cheese",
                     "some ingredients",
                     "some instructions",
                     "some tags")

test_ingredients = "6 ounces (170 g) elbow macaroni\nSalt\n6 ounces (180 ml) evaporated milk\n6 ounces (170 g) grated mild or medium cheddar cheese, or any good melting cheese, such as Fontina, Gruyère, or Jack"
test_instructions = "1Place macaroni in a medium saucepan or skillet and add just enough cold water to cover.\n Add a pinch of salt and bring to a boil over high heat, stirring frequently.\n Continue to cook, stirring, until water has been almost completely absorbed and macaroni is just shy of al dente, about 6 minutes. \n Immediately add evaporated milk and bring to a boil. \nAdd cheese. \nReduce heat to low and cook, stirring continuously, until cheese is melted and liquid has reduced to a creamy sauce, about 2 minutes longer.\n Season to taste with more salt and serve immediately. "
test_tags = "Kenji\nCheese"


def main():
  test_recipe.set_ingredients(test_ingredients)
  test_recipe.set_instructions(test_instructions)
  test_recipe.set_recipe_tags(test_tags)
  print(repr(test_recipe))
  print(test_recipe)





if __name__ == "__main__":
    main()