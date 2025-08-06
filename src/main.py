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
  user_search_type_question = input("\nWhat Type of Search do you want?: Title, Ingredient, Tag, or ID:\n")
  try:
     search_type = SearchType[user_search_type_question.upper()]
  except KeyError:
     print("Invalid search type.")
  user_search_search_term = input("Enter Search Term:\n")
  results = search_recipes(load_recipes_from_json(file_path),search_type,user_search_search_term)
  if len(results) > 1:
    print(f"\nThere were {len(results)} results!:\n")
    list_of_recipies = dictoinaries_to_recipes(results)
    i = 1
    for recipie in list_of_recipies:
      print(f"{i}. {recipie.title}")
      i = i + 1
    try:
      user_multi_recipe_choice = int(input(f"Which number would you like to select 1 - {len(list_of_recipies)} or {len(list_of_recipies) + 1} to cancel the search.\n"))
    except ValueError:
      print("Invalid input. Please enter a number.")
    if int(user_multi_recipe_choice) <= len(list_of_recipies):
      print("- " + list_of_recipies[int(user_multi_recipe_choice)-1].title)
      user_print_card = input(f"\nWould you like to see the recipe card for {list_of_recipies[int(user_multi_recipe_choice)-1].title}? 'Yes' or 'No'\n")
      if user_print_card.lower() == "yes":
        list_of_recipies[int(user_multi_recipe_choice)-1].print_recipe_card()
        user_search_again = input("\nWould you like to make another search?   'Yes' or 'No'\n")
        if user_search_again.lower() == "yes":
          print("\nStarting New Search\n")
          run_search(file_path)
        elif user_search_again.lower() == "no":
          pass
      elif user_print_card.lower() == "no":
        user_search_again = input("\nWould you like to make another search?   'Yes' or 'No'\n")
        if user_search_again.lower() == "yes":
          print("\nStarting New Search\n")
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
    print(f"\nThere was {i} Result:\n")
    found_recipe = results[0]
    stripped_recipe = found_recipe
    recipe_result = dictionary_to_recipe(stripped_recipe)
    print("- " + recipe_result.title)
    user_print_card = input(f"\nWould you like to see the recipe card for {recipe_result.title}? 'Yes' or 'No'\n")
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
  run_edit_while = 1
  while run_edit_while == 1:
    user_search_type_question = input("\nWhat Type of Search do you want?: Title, Ingredient, Tag, or ID:\n")
    try:
      search_type = SearchType[user_search_type_question.upper()]
    except KeyError:
      print("\nInvalid search type! It can only be Title, Ingredient, Tag, or ID\n")
      run_edit_while = 0
      run_edit_recipes(file_path)
    user_search_search_term = input("\nEnter Search Term:\n")
    results = search_recipes(load_recipes_from_json(file_path),search_type,user_search_search_term)
    if len(results) == 0:
      print(f"0 recipes were found that match '{user_search_search_term}'")
      user_search_again = input("Would you like to make another search?   'Yes' or 'No'\n")
      if user_search_again.lower() == "yes":
          print("Starting New Search")
          run_edit_recipes(file_path)
      elif user_search_again.lower() == "no":
        print("Exiting to main menu...")
        main()
    elif len(results) > 1:
      print(f"There were {len(results)} results!:")
      list_of_recipies = dictoinaries_to_recipes(results)
      i = 1
      for recipie in list_of_recipies:
        print(f"{i}. {recipie.title}")
        i = i + 1
      choice_while = 1
      while choice_while == 1:
        try:
          user_multi_recipe_choice = int(input(f"Which number would you like to select 1 - {len(list_of_recipies)} or {len(list_of_recipies) + 1} to cancel the search.\n"))
        except ValueError:
          print("Invalid input. Please enter a number.")
        if int(user_multi_recipe_choice) <= len(list_of_recipies):
          choice_while = 0
          print("- " + list_of_recipies[int(user_multi_recipe_choice)-1].title)
          
        elif int(user_multi_recipe_choice) == len(list_of_recipies)+1:
          choice_while = 0
        else:
          print("Invalid Response!")
    elif len(results) == 1:
      i =1
      print(f"\nThere was {i} Result:\n")
      found_recipe = results[0]
      stripped_recipe = found_recipe
      print(f"- {found_recipe["title"]}\n")
      user_edit_recipe_confirm = input("Is this the recipe that you want to edit.   'Yes' or 'No'\n")
      run_edit_while_no_search = 1
      while run_edit_while_no_search == 1:
        choice_while = 1
        while choice_while == 1:
          if user_edit_recipe_confirm.lower() == "yes":
            choice_while = 0
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
                choice_while = 0
                print("Invalid Option\n")
            elif user_item_to_edit.lower() == "ingredients":
              print(f"\nHow would you like to edit the ingredients of '{recipe_to_edit.title}'\n")
              print("1. Add an ingredient")
              print("2. Remove an ingredient.")
              print("3. Edit one of the ingredients in the recipe")
              print("4. Replace all ingredients with new ones.\n")
              try:
                user_ingredient_edit_type = int(input("Which would you like to do?\n"))
              except ValueError:
                print("Invalid input. Please enter a number.")
              if int(user_ingredient_edit_type) == 1:
                user_ingredient_edit_type_1_while = 1
                while user_ingredient_edit_type_1_while == 1:
                  new_ingredient_while = 1
                  while new_ingredient_while == 1:
                    user_new_ingredient = input("Enter your new ingredient.\n")
                    user_new_ingredient_confirm = input(f"Is '{user_new_ingredient}' correct?   'Yes' or 'No'\n")
                    if user_new_ingredient_confirm.lower() == "no":
                      print("\nOk, let's try this again.\n")
                    elif user_new_ingredient_confirm.lower() == "yes":
                      new_ingredient_while = 0
                    else:
                      print("Invalid Response! Choose a number in the list.")
                  print("Here is the list of the current ingredients:\n")
                  ingredient_idx = 1
                  ingredient_replacement_while = 1
                  while ingredient_replacement_while == 1:
                    for ingredient in recipe_to_edit.ingredients:
                      print(f"{ingredient_idx}. {ingredient}\n")
                      ingredient_idx = ingredient_idx + 1
                    ingredient_idx = 1
                    try:
                      user_ingredient_add_placement = int(input(f"\nWhich ingredient do you want to move down in the list and replace with the new one?    1-{len(recipe_to_edit.ingredients)} or {len(recipe_to_edit.ingredients)+1} to place it at the end.\n"))
                    except ValueError:
                      print("Invalid input. Please enter a number.")
                    if int(user_ingredient_add_placement) <= len(recipe_to_edit.ingredients):
                      recipe_to_edit.ingredients.insert(int(user_ingredient_add_placement) -1,user_new_ingredient)
                      update_recipe_in_book(recipe_to_edit,file_path)
                      print(f"'{user_new_ingredient}' added to '{recipe_to_edit.title}'.\n")
                    elif int(user_ingredient_add_placement) == len(recipe_to_edit.ingredients) + 1:
                      recipe_to_edit.ingredients.insert(int(user_ingredient_add_placement) -1,user_new_ingredient)
                      update_recipe_in_book(recipe_to_edit,file_path)
                      print(f"'{user_new_ingredient}' added to '{recipe_to_edit.title}'.\n")
                    else:
                      print("\nInvalid Response\n")
                    user_add_ingredient_again_confirm = input("Do you want to add another ingredient?    'Yes' or 'No'\n")
                    if user_add_ingredient_again_confirm.lower() == "yes":
                      ingredient_replacement_while = 0
                      print("\nOk lets add another!\n")
                    elif user_add_ingredient_again_confirm.lower() == "no":
                      print("\nExiting to Menu\n")
                      main()
                    else:
                      print("\nInvalid Response! Choose a number in the list.\n")
                      print("\nExiting to Menu\n")
                      main()
              elif int(user_ingredient_edit_type) == 2:
                user_ingredient_edit_type_2_while = 1
                while user_ingredient_edit_type_2_while == 1:
                  print(f"\nHere is a list of ingredients for '{recipe_to_edit.title}'\n")
                  ingredient_replacement_while = 1
                  ingredient_idx = 1
                  for ingredient in recipe_to_edit.ingredients:
                    print(f"{ingredient_idx}. {ingredient}\n")
                    ingredient_idx = ingredient_idx + 1
                  ingredient_idx = 1
                  confirm_while = 1
                  while confirm_while == 1:
                    user_ingredient_remove_selection = input(f"\nWhich ingredient do you want to remove?    1-{len(recipe_to_edit.ingredients)}.\n")
                    if int(user_ingredient_remove_selection) <= len(recipe_to_edit.ingredients):
                      confirm_while = 0
                      removed_ingredient = recipe_to_edit.ingredients.pop(int(user_ingredient_remove_selection)-1)
                      update_recipe_in_book(recipe_to_edit,file_path)
                      print(f"\nRemoved '{removed_ingredient}' from '{recipe_to_edit.title}'.\n")
                      user_edit_delete_another = input("\nWould you like to delete another ingredient?    'Yes' or 'No'\n")
                      if user_edit_delete_another.lower() == "yes":
                        print("\nOK, Let's go.\n")
                      elif user_edit_delete_another.lower() == "no":
                        user_ingredient_edit_type_2_while = 0
                        print("Exiting to menu")
                        main()
                    else:
                      print("Invalid Response!")
              elif int(user_ingredient_edit_type) == 3:
                user_ingredient_edit_type_3_while = 1
                while user_ingredient_edit_type_3_while == 1:
                  print(f"\nHere is a list of ingredients for '{recipe_to_edit.title}'\n")
                  ingredient_replacement_while = 1
                  ingredient_idx = 1
                  for ingredient in recipe_to_edit.ingredients:
                    print(f"{ingredient_idx}. {ingredient}\n")
                    ingredient_idx = ingredient_idx + 1
                  ingredient_idx = 1
                  confirm_while = 1
                  while confirm_while == 1:
                    try:
                      user_ingredient_edit_selection = int(input(f"\nWhich ingredient do you want to edit?    1-{len(recipe_to_edit.ingredients)}.\n"))
                    except ValueError:
                       print("Invalid input. Please enter a number.")
                    if int(user_ingredient_edit_selection) <= len(recipe_to_edit.ingredients):
                      confirm_while = 0
                      edit_ingredient = recipe_to_edit.ingredients.pop(int(user_ingredient_edit_selection)-1)
                      edit_ingredient_while = 1
                      while edit_ingredient_while == 1:
                        edited_ingredient = input(f"\nWhat would you like to change '{edit_ingredient}' to?\n")
                        edited_ingredient_confirm = input(f"\nIs '{edited_ingredient}' correct?\n")
                        if edited_ingredient_confirm.lower() == "no":
                          print("\nLet's try again.\n")
                        elif edited_ingredient_confirm.lower() == "yes":
                          edit_ingredient_while = 0
                          recipe_to_edit.ingredients.insert(int(user_ingredient_edit_selection)-1,edited_ingredient)
                          update_recipe_in_book(recipe_to_edit,file_path)
                          print(f"\nUpdated ingredient from'{edit_ingredient}' to '{edited_ingredient}'.\n")
                          user_edit_delete_another = input("\nWould you like to edit another ingredient?    'Yes' or 'No'\n")
                          if user_edit_delete_another.lower() == "yes":
                            print("\nOK, Let's go.\n")
                          elif user_edit_delete_another.lower() == "no":
                            user_ingredient_edit_type_3_while = 0
                            print("Exiting to menu")
                            main()
                          else:
                            print("Invalid Response! Choose a number in the list.")
              elif int(user_ingredient_edit_type) == 4:
                user_ingredient_edit_type_4_while = 1
                while user_ingredient_edit_type_4_while == 1:
                  user_new_ingredient_list = input(f"\nPlease either type or paste the ingredients below sperated by '<i>'.\n").split("<i>")
                  recipe_to_edit.set_ingredients(user_new_ingredient_list)
                  print(f"\n'{recipe_to_edit.title}'s ingredients have been updated to.\n")
                  for ingredient in recipe_to_edit.ingredients:
                    print(f"- {ingredient}")
                  user_new_ingredient_list_confirm = input(f"\nIs this new list correct?    'Yes' or 'No'\n")
                  if user_new_ingredient_list_confirm.lower() == "yes":
                    update_recipe_in_book(recipe_to_edit,file_path)
                    print("\nGreat, returning to menu.\n")
                    main()
                  elif user_new_ingredient_list_confirm.lower() == "no":
                    print("\nOK, Let's try again.\n")
                  else:
                    print("\nInvalid Option!\n")
            elif user_item_to_edit.lower() == "instructions":
              print(f"\nHow would you like to edit the instructions of '{recipe_to_edit.title}'\n")
              print("1. Add an instruction")
              print("2. Remove an instruction.")
              print("3. Edit one of the instructions in the recipe")
              print("4. Replace all instructions with new ones.\n")
              try:
                user_instruction_edit_type = int(input("Which would you like to do?\n"))
              except ValueError:
                print("Invalid input. Please enter a number.")
              if int(user_instruction_edit_type) == 1:
                user_instruction_edit_type_1_while = 1
                while user_instruction_edit_type_1_while == 1:
                  new_instruction_while = 1
                  while new_instruction_while == 1:
                    user_new_instruction = input("Enter your new instruction.\n")
                    user_new_instruction_confirm = input(f"Is '{user_new_instruction}' correct?   'Yes' or 'No'\n")
                    if user_new_instruction_confirm.lower() == "no":
                      print("\nOk, let's try this again.\n")
                    elif user_new_instruction_confirm.lower() == "yes":
                      new_instruction_while = 0
                    else:
                      print("Invalid Response! Choose a number in the list.")
                  print("Here is the list of the current instructions:\n")
                  instruction_idx = 1
                  instruction_replacement_while = 1
                  while instruction_replacement_while == 1:
                    for instruction in recipe_to_edit.instructions:
                      print(f"{instruction_idx}. {instruction}\n")
                      instruction_idx = instruction_idx + 1
                    instruction_idx = 1
                    try:
                      user_instruction_add_placement = int(input(f"\nWhich instruction do you want to move down in the list and replace with the new one?    1-{len(recipe_to_edit.instructions)} or {len(recipe_to_edit.instructions)+1} to place it at the end.\n"))
                    except ValueError:
                      print("Invalid input. Please enter a number.")
                    if int(user_instruction_add_placement) <= len(recipe_to_edit.instructions):
                      recipe_to_edit.instructions.insert(int(user_instruction_add_placement) -1,user_new_instruction)
                      update_recipe_in_book(recipe_to_edit,file_path)
                      print(f"'{user_new_instruction}' added to '{recipe_to_edit.title}'.\n")
                    elif int(user_instruction_add_placement) == len(recipe_to_edit.instructions) + 1:
                      recipe_to_edit.instructions.insert(int(user_instruction_add_placement) -1,user_new_instruction)
                      update_recipe_in_book(recipe_to_edit,file_path)
                      print(f"'{user_new_instruction}' added to '{recipe_to_edit.title}'.\n")
                    else:
                      print("\nInvalid Response! Choose a number in the list.\n")
                    user_add_instruction_again_confirm = input("Do you want to add another instruction?    'Yes' or 'No'\n")
                    if user_add_instruction_again_confirm.lower() == "yes":
                      instruction_replacement_while = 0
                      print("\nOk lets add another!\n")
                    elif user_add_instruction_again_confirm.lower() == "no":
                      print("\nExiting to Menu\n")
                      main()
                    else:
                      print("\nInvalid Response\n")
                      print("\nExiting to Menu\n")
                      main()
              elif int(user_instruction_edit_type) == 2:
                user_instruction_edit_type_2_while = 1
                while user_instruction_edit_type_2_while == 1:
                  print(f"\nHere is a list of instructions for '{recipe_to_edit.title}'\n")
                  instruction_replacement_while = 1
                  instruction_idx = 1
                  for instruction in recipe_to_edit.instructions:
                    print(f"{instruction_idx}. {instruction}\n")
                    instruction_idx = instruction_idx + 1
                  instruction_idx = 1
                  confirm_while = 1
                  while confirm_while == 1:
                    try:
                      user_instruction_remove_selection = int(input(f"\nWhich instruction do you want to remove?    1-{len(recipe_to_edit.instructions)}.\n"))
                    except ValueError:
                      print("Invalid input. Please enter a number.")
                    if int(user_instruction_remove_selection) <= len(recipe_to_edit.instructions):
                      confirm_while = 0
                      removed_instruction = recipe_to_edit.instructions.pop(int(user_instruction_remove_selection)-1)
                      update_recipe_in_book(recipe_to_edit,file_path)
                      print(f"\nRemoved '{removed_instruction}' from '{recipe_to_edit.title}'.\n")
                      user_edit_delete_another = input("\nWould you like to delete another instruction?    'Yes' or 'No'\n")
                      if user_edit_delete_another.lower() == "yes":
                        print("\nOK, Let's go.\n")
                      elif user_edit_delete_another.lower() == "no":
                        user_instruction_edit_type_2_while = 0
                        print("Exiting to menu")
                        main()
                    else:
                      print("\nInvalid Response! Choose a number in the list.\n")
              elif int(user_instruction_edit_type) == 3:
                user_instruction_edit_type_3_while = 1
                while user_instruction_edit_type_3_while == 1:
                  print(f"\nHere is a list of instructions for '{recipe_to_edit.title}'\n")
                  instruction_replacement_while = 1
                  instruction_idx = 1
                  for instruction in recipe_to_edit.instructions:
                    print(f"{instruction_idx}. {instruction}\n")
                    instruction_idx = instruction_idx + 1
                  instruction_idx = 1
                  confirm_while = 1
                  while confirm_while == 1:
                    try:
                      user_instruction_edit_selection = int(input(f"\nWhich instruction do you want to edit?    1-{len(recipe_to_edit.instructions)}.\n"))
                    except ValueError:
                      print("Invalid input. Please enter a number.")
                    if int(user_instruction_edit_selection) <= len(recipe_to_edit.instructions):
                      confirm_while = 0
                      edit_instruction = recipe_to_edit.instructions.pop(int(user_instruction_edit_selection)-1)
                      edit_instruction_while = 1
                      while edit_instruction_while == 1:
                        edited_instruction = input(f"\nWhat would you like to change '{edit_instruction}' to?\n")
                        edited_instruction_confirm = input(f"\nIs '{edited_instruction}' correct?\n")
                        if edited_instruction_confirm.lower() == "no":
                          print("\nLet's try again.\n")
                        elif edited_instruction_confirm.lower() == "yes":
                          edit_instruction_while = 0
                          recipe_to_edit.instructions.insert(int(user_instruction_edit_selection)-1,edited_instruction)
                          update_recipe_in_book(recipe_to_edit,file_path)
                          print(f"\nUpdated instruction from'{edit_instruction}' to '{edited_instruction}'.\n")
                          user_edit_delete_another = input("\nWould you like to edit another instruction?    'Yes' or 'No'\n")
                          if user_edit_delete_another.lower() == "yes":
                            print("\nOK, Let's go.\n")
                          elif user_edit_delete_another.lower() == "no":
                            user_instruction_edit_type_3_while = 0
                            print("Exiting to menu")
                            main()
                          else:
                            print("\nInvalid Response! Choose a number in the list.\n")
              elif int(user_instruction_edit_type) == 4:
                user_instruction_edit_type_4_while = 1
                while user_instruction_edit_type_4_while == 1:
                  user_new_instruction_list = input(f"\nPlease either type or paste the instructions below sperated by '<i>'.\n").split("<i>")
                  recipe_to_edit.set_instructions(user_new_instruction_list)
                  print(f"\n'{recipe_to_edit.title}'s instructions have been updated to.\n")
                  for instruction in recipe_to_edit.instructions:
                    print(f"- {instruction}")
                  user_new_instruction_list_confirm = input(f"\nIs this new list correct?    'Yes' or 'No'\n")
                  if user_new_instruction_list_confirm.lower() == "yes":
                    update_recipe_in_book(recipe_to_edit,file_path)
                    print("\nGreat, returning to menu.\n")
                    main()
                  elif user_new_instruction_list_confirm.lower() == "no":
                    print("\nOK, Let's try again.\n")
                  else:
                    print("\nInvalid Option!\n")
            elif user_item_to_edit.lower() == "recipe_tags":
              print(f"\nHow would you like to edit the tag of '{recipe_to_edit.title}'\n")
              print("1. Add an tag")
              print("2. Remove an tag.")
              print("3. Edit one of the tag in the recipe")
              print("4. Replace all tag with new ones.\n")
              try:
                user_tag_edit_type = int(input("Which would you like to do?\n"))
              except ValueError:
                print("Invalid input. Please enter a number.")
              if int(user_tag_edit_type) == 1:
                user_tag_edit_type_1_while = 1
                while user_tag_edit_type_1_while == 1:
                  new_tag_while = 1
                  while new_tag_while == 1:
                    user_new_tag = input("Enter your new tag.\n")
                    user_new_tag_confirm = input(f"Is '{user_new_tag}' correct?   'Yes' or 'No'\n")
                    if user_new_tag_confirm.lower() == "no":
                      print("\nOk, let's try this again.\n")
                    elif user_new_tag_confirm.lower() == "yes":
                      new_tag_while = 0
                    else:
                      print("\nInvalid Response! Choose a number in the list.\n")
                  print("Here is the list of the current tag:\n")
                  tag_idx = 1
                  tag_replacement_while = 1
                  while tag_replacement_while == 1:
                    for tag in recipe_to_edit.recipe_tags:
                      print(f"{tag_idx}. {tag}\n")
                      tag_idx = tag_idx + 1
                    tag_idx = 1
                    try:
                      user_tag_add_placement = int(input(f"\nWhich tag do you want to move down in the list and replace with the new one?    1-{len(recipe_to_edit.recipe_tags)} or {len(recipe_to_edit.recipe_tags)+1} to place it at the end.\n"))
                    except ValueError:
                      print("Invalid input. Please enter a number.")
                    if int(user_tag_add_placement) <= len(recipe_to_edit.recipe_tags):
                      recipe_to_edit.recipe_tags.insert(int(user_tag_add_placement) -1,user_new_tag)
                      update_recipe_in_book(recipe_to_edit,file_path)
                      print(f"'{user_new_tag}' added to '{recipe_to_edit.title}'.\n")
                    elif int(user_tag_add_placement) == len(recipe_to_edit.recipe_tags) + 1:
                      recipe_to_edit.recipe_tags.insert(int(user_tag_add_placement) -1,user_new_tag)
                      update_recipe_in_book(recipe_to_edit,file_path)
                      print(f"'{user_new_tag}' added to '{recipe_to_edit.title}'.\n")
                    else:
                      print("\nInvalid Response\n")
                    user_add_tag_again_confirm = input("Do you want to add another tag?    'Yes' or 'No'\n")
                    if user_add_tag_again_confirm.lower() == "yes":
                      tag_replacement_while = 0
                      print("\nOk lets add another!\n")
                    elif user_add_tag_again_confirm.lower() == "no":
                      print("\nExiting to Menu\n")
                      main()
                    else:
                      print("\nInvalid Response\n")
                      print("\nExiting to Menu\n")
                      main()
              elif int(user_tag_edit_type) == 2:
                user_tag_edit_type_2_while = 1
                while user_tag_edit_type_2_while == 1:
                  print(f"\nHere is a list of tag for '{recipe_to_edit.title}'\n")
                  tag_replacement_while = 1
                  tag_idx = 1
                  for tag in recipe_to_edit.recipe_tags:
                    print(f"{tag_idx}. {tag}\n")
                    tag_idx = tag_idx + 1
                  tag_idx = 1
                  confirm_while = 1
                  while confirm_while == 1:
                    try:
                      user_tag_remove_selection = int(input(f"\nWhich tag do you want to remove?    1-{len(recipe_to_edit.recipe_tags)}.\n"))
                    except ValueError:
                      print("Invalid input. Please enter a number.")
                    if int(user_tag_remove_selection) <= len(recipe_to_edit.recipe_tags):
                      confirm_while = 0
                      removed_tag = recipe_to_edit.recipe_tags.pop(int(user_tag_remove_selection)-1)
                      update_recipe_in_book(recipe_to_edit,file_path)
                      print(f"\nRemoved '{removed_tag}' from '{recipe_to_edit.title}'.\n")
                      user_edit_delete_another = input("\nWould you like to delete another tag?    'Yes' or 'No'\n")
                      if user_edit_delete_another.lower() == "yes":
                        print("\nOK, Let's go.\n")
                      elif user_edit_delete_another.lower() == "no":
                        user_tag_edit_type_2_while = 0
                        print("Exiting to menu")
                        main()
                    else:
                      print("\nInvalid Response! Choose a number in the list.\n")
              elif int(user_tag_edit_type) == 3:
                user_tag_edit_type_3_while = 1
                while user_tag_edit_type_3_while == 1:
                  print(f"\nHere is a list of tag for '{recipe_to_edit.title}'\n")
                  tag_replacement_while = 1
                  tag_idx = 1
                  for tag in recipe_to_edit.recipe_tags:
                    print(f"{tag_idx}. {tag}\n")
                    tag_idx = tag_idx + 1
                  tag_idx = 1
                  confirm_while = 1
                  while confirm_while == 1:
                    try:
                      user_tag_edit_selection = int(input(f"\nWhich tag do you want to edit?    1-{len(recipe_to_edit.recipe_tags)}.\n"))
                    except ValueError:
                      print("Invalid input. Please enter a number.")
                    if int(user_tag_edit_selection) <= len(recipe_to_edit.recipe_tags):
                      confirm_while = 0
                      edit_tag = recipe_to_edit.recipe_tags.pop(int(user_tag_edit_selection)-1)
                      edit_tag_while = 1
                      while edit_tag_while == 1:
                        edited_tag = input(f"\nWhat would you like to change '{edit_tag}' to?\n")
                        edited_tag_confirm = input(f"\nIs '{edited_tag}' correct?\n")
                        if edited_tag_confirm.lower() == "no":
                          print("\nLet's try again.\n")
                        elif edited_tag_confirm.lower() == "yes":
                          edit_tag_while = 0
                          recipe_to_edit.recipe_tags.insert(int(user_tag_edit_selection)-1,edited_tag)
                          update_recipe_in_book(recipe_to_edit,file_path)
                          print(f"\nUpdated tag from'{edit_tag}' to '{edited_tag}'.\n")
                          user_edit_delete_another = input("\nWould you like to edit another tag?    'Yes' or 'No'\n")
                          if user_edit_delete_another.lower() == "yes":
                            print("\nOK, Let's go.\n")
                          elif user_edit_delete_another.lower() == "no":
                            user_tag_edit_type_3_while = 0
                            print("Exiting to menu")
                            main()
                          else:
                            print("\nInvalid Response! Choose a number in the list.\n")
              elif int(user_tag_edit_type) == 4:
                user_tag_edit_type_4_while = 1
                while user_tag_edit_type_4_while == 1:
                  user_new_tag_list = input(f"\nPlease either type or paste the tag(s) below sperated by '<t>'.\n").split("<t>")
                  recipe_to_edit.set_tags(user_new_tag_list)
                  print(f"\n'{recipe_to_edit.title}'s tag have been updated to.\n")
                  for tag in recipe_to_edit.recipe_tags:
                    print(f"- {tag}")
                  user_new_tag_list_confirm = input(f"\nIs this new list correct?    'Yes' or 'No'\n")
                  if user_new_tag_list_confirm.lower() == "yes":
                    update_recipe_in_book(recipe_to_edit,file_path)
                    print("\nGreat, returning to menu.\n")
                    main()
                  elif user_new_tag_list_confirm.lower() == "no":
                    print("\nOK, Let's try again.\n")
                  else:
                    print("\nInvalid Option!\n")
            elif user_item_to_edit.lower() == "url":
              #update with updating url
              user_item_to_edit_url_while = 1
              while user_item_to_edit_url_while == 1:
                print(f"\nThe current url for '{recipe_to_edit.title}' is '{recipe_to_edit.url}'.\n")
                user_edit_new_url = input(f"\nEnter the new url for '{recipe_to_edit.title}'.\n")
                user_edit_new_url_confirm = input(f"\nIs '{user_edit_new_url}' correct?    'Yes' or 'No'\n")
                if user_edit_new_url_confirm.lower() == "yes":
                  recipe_to_edit.url = user_edit_new_url 
                  update_recipe_in_book(recipe_to_edit,file_path)
                  print(f"\nurl for '{recipe_to_edit.title}' udpated to '{recipe_to_edit.url}'.\n")
                  print("\nExiting to main menu.\n")
                  main()
                if user_edit_new_url_confirm.lower() == "no":
                  print("\nLet's try again.\n")
                else:
                  print("\nInvalid Choice! Try Again.\n")
            else:
              print("\nInvalid Choice! Enter a field to edit.\n")
          elif user_edit_recipe_confirm.lower() == "no":
            choice_while = 0
            print("\nOK, Let's try again.\n")
            run_edit_recipes(file_path)
          else:
            print("Invalid choice! Try Again.\n")
        


def main():
  while True:
    print("\nWelome to BiteBook, All your best recipes, byte-sized!\n")
    print("1. Search for recipe(s)")
    print("2. Add a new recipe(s)")
    print("3. Edit recipe(s)")
    print("4. Exit program")
    try:
      user_feautre_choice = int(input("\nChoose an option:\n"))
      if int(user_feautre_choice) == 1:
        run_search(file_path)
      elif int(user_feautre_choice) == 2:
        run_add_recipes(file_path)
      elif int(user_feautre_choice) == 3:
        run_edit_recipes(file_path)
      elif int(user_feautre_choice) == 4:
        print("Goodbye")
        exit()
      else:
        print("\nInvalid Input! Please enter a number in the menu.\n")
    except ValueError:
      print("\nInvalid input. Please enter a number.\n")













if __name__ == "__main__":
    main()