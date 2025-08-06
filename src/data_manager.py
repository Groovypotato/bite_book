import json
from recipe import Recipe

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

def save_recipes_to_json(data,file_path):
    try:
        with open(file_path, 'w') as book:
            json.dump(data, book, indent=2)
    except FileNotFoundError as e:
        print(e)

def load_recipes_from_json(file_path):
    try:
        with open(file_path,'r')as book:
            data = json.load(book)
        return data
    except FileNotFoundError:
        return {"recipes": []}

def add_recipe_to_book(recipe_obj,file_path):
    book = load_recipes_from_json(file_path)
    if "recipes" not in book or not isinstance(book["recipes"], list):
        book["recipes"] = []
    book["recipes"].append(recipe_obj.recipe_to_dictionary())
    save_recipes_to_json(book,file_path)

def update_recipe_in_book(recipe_obj,file_path):
    book = load_recipes_from_json(file_path)
    for i, recipe in enumerate(book["recipes"]):
        if recipe["id"] == recipe_obj.id:
            book["recipes"][i] = recipe_obj.recipe_to_dictionary()
            save_recipes_to_json(book, file_path)
            return True
    return False

def delete_recipe_in_book(recipe_obj, file_path):
    book = load_recipes_from_json(file_path)
    if "recipes" not in book or not isinstance(book["recipes"], list):
        print(f"Error: No valid 'recipes' list found in {file_path}")
        return False
    for i, recipe in enumerate(book["recipes"]):
        if recipe["id"] == recipe_obj.id:
            book["recipes"].pop(i)
            save_recipes_to_json(book, file_path)
            return True
    print(f"Error: Recipe with ID '{recipe_obj.id}' not found.")
    return False




