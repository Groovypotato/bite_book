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

def run_search(file_path: str):
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
    user_multi_recipe_choice = input(f"Which number would you like to select 1 - {len(list_of_recipies)} or {len(list_of_recipies) + 1} to cancel the search.     ")
    if int(user_multi_recipe_choice) <= len(list_of_recipies):
      print("- " + list_of_recipies[int(user_multi_recipe_choice)-1].title)
      user_print_card = input(f"Would you like to see the recipe card for {list_of_recipies[int(user_multi_recipe_choice)-1].title}? 'Yes' or 'No'    ")
      if user_print_card.lower() == "yes":
        list_of_recipies[int(user_multi_recipe_choice)-1].print_recipe_card()
        user_search_again = input("Would you like to make another search?   'Yes' or 'No'    ")
        if user_search_again.lower() == "yes":
          print("Starting New Search")
          run_search(file_path)
        elif user_search_again.lower() == "no":
          pass
      elif user_print_card.lower() == "no":
        user_search_again = input("Would you like to make another search?   'Yes' or 'No'    ")
        if user_search_again.lower() == "yes":
          print("Starting New Search")
          run_search(file_path)
        elif user_search_again.lower() == "no":
          pass
      else:
        print("Incorrect Choice!")
    elif int(user_multi_recipe_choice) == len(list_of_recipies)+1:
      print("Canceling Search")
    else:
      print("Invalid Response!")
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
        run_search(file_path)
      elif user_search_again.lower() == "no":
        print("Exiting to main menu...")
    elif user_print_card.lower() == "no":
      user_search_again = input("Would you like to make another search?   'Yes' or 'No'    ")
      if user_search_again.lower() == "yes":
         print("Starting New Search")
         run_search(file_path)
      elif user_search_again.lower() == "no":
        print("Exiting to main menu...")
        
    else:
       print("Incorrect Choice!")
  else:
    print(f"0 recipes were found that match '{user_search_search_term}'")
    user_search_again = input("Would you like to make another search?   'Yes' or 'No'    ")
    if user_search_again.lower() == "yes":
        print("Starting New Search")
        run_search(file_path)
    elif user_search_again.lower() == "no":
      print("Exiting to main menu...")

def main():
  while True:
    print("\nWelome to BiteBook, All your best recipes, byte-sized! ")
    print("1. Search for recipe")
    print("2. Add a new recipe")
    print("3. Exit program")
    user_feautre_choice = input("Choose an option:    ")
    if int(user_feautre_choice) == 1:
      run_search(file_path)
    elif int(user_feautre_choice) == 2:
      print("'Add recipe' feature coming soon!")
    elif int(user_feautre_choice) == 3:
      print("Goodbye")
      exit()
    













if __name__ == "__main__":
    main()