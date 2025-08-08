from pathlib import Path
from data_manager import add_recipe_to_book, load_recipes_from_json, dictionary_to_recipe

def import_from_bite_book(bite_book_book_to_import_path, bite_book_book_path):
    src = Path(bite_book_book_to_import_path).expanduser()
    dst = Path(bite_book_book_path).expanduser()

    if not src.is_file():
        print(f"Error: '{src}' is not a valid file.")
        return

    current_recipes = load_recipes_from_json(dst)
    existing_ids = {recipe["id"] for recipe in current_recipes.get("recipes", [])}

    recipe_count = 0
    skipped_count = 0
    recipes_to_import = load_recipes_from_json(src)

    for recipe_dict in recipes_to_import.get("recipes", []):
        recipe_to_import = dictionary_to_recipe(recipe_dict)
        if recipe_to_import.id not in existing_ids:
            add_recipe_to_book(recipe_to_import, dst)
            recipe_count += 1
            print(f"Import: '{recipe_to_import.title}' has been added.")
        else:
            skipped_count += 1
            print(f"Import: '{recipe_to_import.title}' skipped (duplicate id).")

    print(f"\nThe import has finished. {recipe_count} recipe(s) imported, {skipped_count} skipped.\n")
