from pathlib import Path
import json
from data_manager import create_recipe, add_recipe_to_book

def import_from_mealie(mealie_recipe_export, bite_book_book_path):
    root = Path(mealie_recipe_export).expanduser()
    dst = Path(bite_book_book_path).expanduser()

    if not root.is_dir():
        print(f"Error: '{root}' is not a valid folder.")
        return

    recipe_count = 0
    for folder_path in root.iterdir():
        if not folder_path.is_dir():
            continue

        recipe_json_path = folder_path / f"{folder_path.name}.json"
        if not recipe_json_path.is_file():
            print(f"Skipping '{folder_path.name}': No {folder_path.name}.json found.")
            continue
        try:
            with recipe_json_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
            title = data.get("name", "Untitled Recipe")
            ingredients = [i["display"] for i in data.get("recipe_ingredient", [])]
            instructions = [step["text"] for step in data.get("recipe_instructions", [])]
            tags = [tag["name"] for tag in data.get("tags", [])]
            url = data.get("org_url")
            recipe_obj = create_recipe(title, ingredients, instructions, tags, url)
            add_recipe_to_book(recipe_obj, dst)
            print(f"Imported: {title}")
            recipe_count += 1
        except Exception as e:
            print(f"Failed to import '{folder_path.name}': {e}")
    print(f"\nFinished importing. {recipe_count} recipe(s) added.")
