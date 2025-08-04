from recipe import Recipe
from search_manager import SearchType,search_recipes
from data_manager import load_recipes_from_json,add_recipe_to_book,update_recipe_in_book
file_path = "./static/recipes.json"

def create_recipe(title,ingredients,instructions,tags,url=None, id=None):
   new_recipe = Recipe(title=title,url=url,id=id)
   new_recipe.set_ingredients(ingredients)
   new_recipe.set_instructions(instructions)
   new_recipe.set_recipe_tags(tags)
   return new_recipe


def dictionary_to_recipe(dictionary):
  recipe = create_recipe(
    dictionary["title"],
    dictionary["ingredients"],
    dictionary["instructions"],
    dictionary["tags"],
    dictionary["url"],
    dictionary["id"]
  )
  return recipe

def dictoinaries_to_recipes(list_of_dictionaries):
  list = []
  for dictionary in list_of_dictionaries:
    list.append(dictionary_to_recipe(dictionary))
  return list

def run_search(file_path: str):
  user_search_type_question = input("What Type of Search do you want?: Title, Ingredient, Tag, or ID:\n")
  try:
     search_type = SearchType[user_search_type_question.upper()]
  except KeyError:
     print("Invalid search type.")
  user_search_search_term = input("Enter Search Term:\n")
  results = search_recipes(load_recipes_from_json(file_path),search_type,user_search_search_term)
  if len(results) > 1:
    print(f"There were {len(results)} results!:")
    list_of_recipies = dictoinaries_to_recipes(results)
    i = 1
    for recipie in list_of_recipies:
      print(f"{i}. {recipie.title}")
      i = i + 1
    user_multi_recipe_choice = input(f"Which number would you like to select 1 - {len(list_of_recipies)} or {len(list_of_recipies) + 1} to cancel the search.\n")
    if int(user_multi_recipe_choice) <= len(list_of_recipies):
      print("- " + list_of_recipies[int(user_multi_recipe_choice)-1].title)
      user_print_card = input(f"Would you like to see the recipe card for {list_of_recipies[int(user_multi_recipe_choice)-1].title}? 'Yes' or 'No'\n")
      if user_print_card.lower() == "yes":
        list_of_recipies[int(user_multi_recipe_choice)-1].print_recipe_card()
        user_search_again = input("Would you like to make another search?   'Yes' or 'No'\n")
        if user_search_again.lower() == "yes":
          print("Starting New Search")
          run_search(file_path)
        elif user_search_again.lower() == "no":
          pass
      elif user_print_card.lower() == "no":
        user_search_again = input("Would you like to make another search?   'Yes' or 'No'\n")
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
    user_print_card = input(f"Would you like to see the recipe card for {recipe_result.title}? 'Yes' or 'No'\n")
    if user_print_card.lower() == "yes":
      recipe_result.print_recipe_card()
      user_search_again = input("Would you like to make another search?   'Yes' or 'No'\n")
      if user_search_again.lower() == "yes":
        print("Starting New Search")
        run_search(file_path)
      elif user_search_again.lower() == "no":
        print("Exiting to main menu...")
    elif user_print_card.lower() == "no":
      user_search_again = input("Would you like to make another search?   'Yes' or 'No'\n")
      if user_search_again.lower() == "yes":
         print("Starting New Search")
         run_search(file_path)
      elif user_search_again.lower() == "no":
        print("Exiting to main menu...")
        
    else:
       print("Incorrect Choice!")
  else:
    print(f"0 recipes were found that match '{user_search_search_term}'")
    user_search_again = input("Would you like to make another search?   'Yes' or 'No'\n")
    if user_search_again.lower() == "yes":
        print("Starting New Search")
        run_search(file_path)
    elif user_search_again.lower() == "no":
      print("Exiting to main menu...")

def run_add_recipes(file_path):
  user_recipe_title_confirm = "no"
  while user_recipe_title_confirm == "no".lower():
    user_recipe_title = input("\nPlease enter the 'Title' of the recipe:\n")
    print(f"\n{user_recipe_title}")
    user_recipe_title_confirm = input("\nDoes the title above look correct? 'Yes' or 'No':\n")
    if user_recipe_title_confirm.lower() == "no".lower():
      print("\nRetype your title.")
  if user_recipe_title_confirm.lower() == "yes".lower():
    print("\nLet's add some ingredients")
  else:
    print("\nInvalid Response")
    return
  user_recipe_ingredients_confirm = "no"
  while user_recipe_ingredients_confirm == "no":
    user_recipe_ingredients = input("\nEnter your ingredients on one line seperated by /n:\n").split('/n')
    print(f"\n{user_recipe_ingredients}")
    user_recipe_ingredients_confirm = input("\nDo these ingredients look correct?  'Yes' or 'No':\n")
    if user_recipe_ingredients_confirm.lower() == "no":
      print("\nRetype your ingredients")
  if user_recipe_ingredients_confirm.lower() == "yes":
    print("\nLets add some instructions")
  else:
    print("\nInvalid Response")
    return
  user_recipe_instructions_confirm = "no"
  while user_recipe_instructions_confirm == "no":
    user_recipe_instructions = input("\nEnter your instructions on one line seperated by /n:\n").split('/n')
    print(f"\n{user_recipe_instructions}")
    user_recipe_instructions_confirm = input("\nDo these instructions look correct?  'Yes' or 'No':\n")
    if user_recipe_instructions_confirm.lower() == "no":
      print("\nRetype your instructions")
  if user_recipe_instructions_confirm.lower() == "yes":
    print("\nLets add some tags")
  else:
    print("\nInvalid Response")
    return
  user_recipe_tags_confirm = "no"
  while user_recipe_tags_confirm == "no":
    user_recipe_tags = input("\nEnter your tags on one line seperated by /n:\n").split('/n')
    print(user_recipe_tags)
    user_recipe_tags_confirm = input("\nDo these tag(s) look correct?  'Yes' or 'No':\n")
    if user_recipe_tags_confirm.lower() == "no":
      print("\nRetype your Tag(s)")
  if user_recipe_tags_confirm.lower() == "yes":
    print("\nLets add a URL")
  else:
    print("\nInvalid Response")
    return
  user_recipe_url_confirm = "no"
  while user_recipe_url_confirm == "no":
    user_recipe_url = input("\nEnter your URL or 'None' is there isn't one:\n")
    print(f"\n{user_recipe_url}")
    user_recipe_url_confirm = input("\nDo the URL look correct?  'Yes' or 'No':\n")
    if user_recipe_url_confirm.lower() == "no":
      print("\nRetype your URL")
  if user_recipe_url_confirm.lower() == "yes":
    print(f"Creating Recipe {user_recipe_title}")
    new_recipe = create_recipe(user_recipe_title,user_recipe_ingredients,user_recipe_instructions,user_recipe_tags,user_recipe_url)
  else:
    print("Invalid Response")
    return
  add_recipe_to_book(new_recipe,file_path)
  print(f"\nRecipe:'{user_recipe_title}' added")
  user_add_another_confirm = input("\nWould you like to add another recipe?  'Yes' or 'No'\n")
  if user_add_another_confirm.lower() == "yes":
    run_add_recipes(file_path)
  elif user_add_another_confirm.lower() == "no":
    print("Exiting to Menu")
  else:
    print("Invalid Response")

def run_edit_recipes(file_path:str):
  print("\nLet's find the recipe to edit.\n")
  user_search_type_question = input("What Type of Search do you want?: Title, Ingredient, Tag, or ID:\n")
  try:
     search_type = SearchType[user_search_type_question.upper()]
  except KeyError:
     print("Invalid search type.")
  user_search_search_term = input("\nEnter Search Term:\n")
  results = search_recipes(load_recipes_from_json(file_path),search_type,user_search_search_term)
  if len(results) > 1:
    print(f"There were {len(results)} results!:")
    list_of_recipies = dictoinaries_to_recipes(results)
    i = 1
    for recipie in list_of_recipies:
      print(f"{i}. {recipie.title}")
      i = i + 1
    user_multi_recipe_choice = input(f"Which number would you like to select 1 - {len(list_of_recipies)} or {len(list_of_recipies) + 1} to cancel the search.\n")
    if int(user_multi_recipe_choice) <= len(list_of_recipies):
      print("- " + list_of_recipies[int(user_multi_recipe_choice)-1].title)
      
    elif int(user_multi_recipe_choice) == len(list_of_recipies)+1:
      pass
    else:
      print("Invalid Response!")
  elif len(results) == 1:
    i =1
    print(f"\nThere was {i} Result:\n")
    found_recipe = results[0]
    stripped_recipe = found_recipe
    print(f"- {found_recipe["title"]}\n")
    user_edit_recipe_confirm = input("Is this the recipe that you want to edit.   'Yes' or 'No'\n")
    if user_edit_recipe_confirm.lower() == "yes":
      print("\nWhat field do you want to edit?\n")
      recipe_to_edit = create_recipe(
        found_recipe["title"],
        found_recipe["ingredients"],
        found_recipe["instructions"],
        found_recipe["tags"],
        found_recipe["url"],
        found_recipe["id"]
      )
      for name,value in recipe_to_edit.__dict__.items():
        if name == "id" or name == "max_length":
          pass
        else:
          print(f"- {name}")
          i = i + 1
      user_item_to_edit = input("\nSelection:  ")
      edit_while = 0
      if user_item_to_edit.lower() == "title":
        recipe_to_edit_title = recipe_to_edit.title
        edit_while = 1
        while edit_while == 1:
          user_new_title = input("\nEnter the new recipe 'title'\n")
          user_new_title_confirm = input(f"\nDoes '{user_new_title}' look correct?\n")
          if user_new_title_confirm.lower() == "no":
            print("\nLet's try again then...\n")
          elif user_new_title_confirm.lower() == "yes":
            edit_while = 0
            recipe_to_edit.title = user_new_title
            updated_recipe_complete_confirm = update_recipe_in_book(recipe_to_edit,file_path)
            if updated_recipe_complete_confirm == True:
              print(f"\nRecipe title '{recipe_to_edit_title} has been updated to {user_new_title}\n")
            elif updated_recipe_complete_confirm == False:
              print("\nRecipe was not updated, yell at the programmer!")
        user_additional_edit_confirm = input("\nWould you like to edit another recipe?   'Yes' or 'No'\n")
        if user_additional_edit_confirm.lower() == "yes":
          run_edit_recipes(file_path)
        elif user_additional_edit_confirm.lower() == "no":
          print("Exiting to main menu")
        else:
          print("Invalid Option\n")
          print("Returning you to the Menu")
      elif user_item_to_edit.lower() == "ingredients":
        #update with updating ingredients
        pass
      elif user_item_to_edit.lower() == "instructions":
        #update with updating instructions
        pass
      elif user_item_to_edit.lower() == "recipe_tags":
        #update with updating reipe tags
        pass
      elif user_item_to_edit.lower() == "url":
        #update with updating url
        pass
      else:
        #update what happens if they fuckup when choosing what to edit in the recipe
        pass

  else:
    print(f"0 recipes were found that match '{user_search_search_term}'")
    user_search_again = input("Would you like to make another search?   'Yes' or 'No'\n")
    if user_search_again.lower() == "yes":
        print("Starting New Search")
        run_edit_recipes(file_path)
    elif user_search_again.lower() == "no":
      print("Exiting to main menu...")


def main():
  while True:
    print("\nWelome to BiteBook, All your best recipes, byte-sized! ")
    print("1. Search for recipe(s)")
    print("2. Add a new recipe(s)")
    print("3. Edit recipe(s)")
    print("4. Exit program")
    user_feautre_choice = input("Choose an option:    ")
    if int(user_feautre_choice) == 1:
      run_search(file_path)
    elif int(user_feautre_choice) == 2:
      run_add_recipes(file_path)
    elif int(user_feautre_choice) == 3:
      run_edit_recipes(file_path)
    elif int(user_feautre_choice) == 4:
      print("Goodbye")
      exit()
    













if __name__ == "__main__":
    main()