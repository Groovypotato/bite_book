import json

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
