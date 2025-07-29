from recipe import Recipe


test_recipe = Recipe("3-Ingredient Stovetop Mac and Cheese Recipe",
                     "Kenji 3 ingredient Mac&Cheese",
                     "some ingredients",
                     "some instructions",
                     "some tags")

test_ingredients = ["6 ounces (170 g) elbow macaroni ","Salt","6 ounces (180 ml) evaporated milk ","6 ounces (170 g) grated mild or medium cheddar cheese, or any good melting cheese, such as Fontina, Gruyère, or Jack "]


def main():
  test_recipe.set_ingredients(test_ingredients)
  print(repr(test_recipe))
  print(test_recipe)





if __name__ == "__main__":
    main()