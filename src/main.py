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


def dictionary_to_recipe(dictionary):
  recipe = create_recipe(dictionary["title"],dictionary["ingredients"],dictionary["instructions"],dictionary["tags"],dictionary["url"])
  return recipe

def dictoinaries_to_recipes(list_of_dictionaries):
  list = []
  for dictionary in list_of_dictionaries:
    list.append(dictionary_to_recipe(dictionary))
  return list

def main():
  user_search_type_question = input("What Type of Search do you want?: Title, Ingredient, Tag, or ID:    ")
  try:
     search_type = SearchType[user_search_type_question.upper()]
  except KeyError:
     print("Invalid search type.")
  print(search_type)
  user_search_search_term = input("Enter Search Term:    ")
  results = search_recipes(load_recipes_from_json(file_path),search_type,user_search_search_term)
  if len(results) > 1:
     print(f"There were {len(results)} results!:")
     list_of_recipies = dictoinaries_to_recipes(results)
     i = 1
     for recipie in list_of_recipies:
        print(f"{i}. {recipie.title}")
        i = i + 1
  elif len(results) == 1:
    i =1
    print(f"There was {i} Result:")
    found_recipe = results[0]
    stripped_recipe = found_recipe
    recipe_result = dictionary_to_recipe(stripped_recipe)
    print("- " + recipe_result.title)
    user_print_card = input(f"Would you like to see the recipe card for {recipe_result.title}? 'Yes' or 'No'    ")
    if user_print_card.lower() == "yes":
      recipe_result.print_recipe_card()
      user_search_again = input("Would you like to make another search?   'Yes' or 'No'    ")
      if user_search_again.lower() == "yes":
        print("Starting New Search")
      elif user_search_again.lower() == "no":
        print("Goodbye!")
        exit()
    elif user_print_card.lower() == "no":
      user_search_again = input("Would you like to make another search?   'Yes' or 'No'    ")
      if user_search_again.lower() == "yes":
         print("Starting New Search")
      elif user_search_again.lower() == "no":
        print("Goodbye!")
        exit()
    else:
       print("Incorrect Choice!")
  else:
    print(f"0 recipes were found that match '{user_search_search_term}'")













if __name__ == "__main__":
    main()