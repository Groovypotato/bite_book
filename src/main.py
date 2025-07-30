from recipe import Recipe
from search_manager import SearchType,search_recipes
from data_manager import load_recipes_from_json
file_path = "./static/recipes.json"

def create_recipe(title,ingredients,instructions,tags,url=None):
   new_recipe = Recipe(title=title,url=url)
   new_recipe.set_ingredients(ingredients)
   new_recipe.set_instructions(instructions)
   new_recipe.set_recipe_tags(tags)
   return new_recipe


def main():
  user_search_type_question = input("What Type of Search do you want?: Title, Ingredient, Tag, or ID:    ")
  try:
     search_type = SearchType[user_search_type_question.upper()]
  except KeyError:
     print("Invalid search type.")
  print(search_type)
  user_search_search_term = input("Enter Search Term:   ")
  results = search_recipes(load_recipes_from_json(file_path),search_type,user_search_search_term)
  print(f"Here are your results: {results}")













if __name__ == "__main__":
    main()