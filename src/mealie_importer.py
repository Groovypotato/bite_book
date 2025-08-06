import os
import json
from data_manager import create_recipe, add_recipe_to_book

def import_from_mealie(mealie_recipe_export, bite_book_book_path):
    if not os.path.isdir(mealie_recipe_export):
        print(f"Error: '{mealie_recipe_export}' is not a valid folder.")
        return
    recipe_count = 0
    for folder_name in os.listdir(mealie_recipe_export):
        recipe_folder_path = os.path.join(mealie_recipe_export, folder_name)
        if not os.path.isdir(recipe_folder_path):
            continue
        recipe_json_path = os.path.join(recipe_folder_path, f"{folder_name}.json")
        if not os.path.isfile(recipe_json_path):
            print(f"Skipping '{folder_name}': No recipe.json found.")
            continue
        try:
            with open(recipe_json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            title = data.get("name", "Untitled Recipe")
            ingredients = [i["display"] for i in data.get("recipe_ingredient", [])]
            instructions = [step["text"] for step in data.get("recipe_instructions", [])]
            tags = [tag["name"] for tag in data.get("tags", [])]
            url = data.get("org_url")
            recipe_obj = create_recipe(title, ingredients, instructions, tags, url)
            add_recipe_to_book(recipe_obj, bite_book_book_path)
            print(f"Imported: {title}")
            recipe_count += 1
        except Exception as e:
            print(f"Failed to import '{folder_name}': {e}")
    print(f"\nFinished importing. {recipe_count} recipe(s) added.")
