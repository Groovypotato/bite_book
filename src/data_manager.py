import json

file_path = "./static/recipes.json"



def save_recipes_to_json(data):
    try:
        with open(file_path, 'w') as book:
            json.dump(data, book, indent=2)
    except Exception as e:
        print(e)

