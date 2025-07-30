from recipe import Recipe


test_recipe = Recipe("3-Ingredient Stovetop Mac and Cheese Recipe",
                     "some ingredients",
                     "some instructions",
                     "some tags")

test_ingredients = "6 ounces (170 g) elbow macaroni\nSalt\n6 ounces (180 ml) evaporated milk\n6 ounces (170 g) grated mild or medium cheddar cheese, or any good melting cheese, such as Fontina, Gruyère, or Jack"
test_instructions = "Place macaroni in a medium saucepan or skillet and add just enough cold water to cover.\nAdd a pinch of salt and bring to a boil over high heat, stirring frequently.\nContinue to cook, stirring, until water has been almost completely absorbed and macaroni is just shy of al dente, about 6 minutes.\nImmediately add evaporated milk and bring to a boil.\nAdd cheese.\nReduce heat to low and cook, stirring continuously, until cheese is melted and liquid has reduced to a creamy sauce, about 2 minutes longer.\nSeason to taste with more salt and serve immediately. "
test_tags = "Kenji\nCheese"

def main():
  test_recipe.set_ingredients(test_ingredients)
  test_recipe.set_instructions(test_instructions)
  test_recipe.set_recipe_tags(test_tags)
  test_recipe.print_recipe_card()





if __name__ == "__main__":
    main()