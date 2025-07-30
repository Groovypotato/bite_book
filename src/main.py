from recipe import Recipe
from data_manager import add_recipe_to_book
file_path = "./static/recipes.json"
def create_recipe(title,ingredients,instructions,tags,url=None):
   new_recipe = Recipe(title=title,url=url)
   new_recipe.set_ingredients(ingredients)
   new_recipe.set_instructions(instructions)
   new_recipe.set_recipe_tags(tags)
   return new_recipe


def main():
    print("yes")




if __name__ == "__main__":
    main()