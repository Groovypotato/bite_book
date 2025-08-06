import os
from data_manager import add_recipe_to_book,load_recipes_from_json,dictionary_to_recipe

def import_from_bite_book(bite_book_book_to_import_path, bite_book_book_path):
    if not os.path.isfile(bite_book_book_to_import_path):
        print(f"Error: '{bite_book_book_to_import_path}' is not a valid file.")
        return

    current_recipes = load_recipes_from_json(bite_book_book_path)
    existing_ids = {recipe["id"] for recipe in current_recipes.get("recipes", [])}

    recipe_count = 0
    skipped_count = 0
    recipes_to_import = load_recipes_from_json(bite_book_book_to_import_path)

    for recipe_dict in recipes_to_import["recipes"]:
        recipe_to_import = dictionary_to_recipe(recipe_dict)
        if recipe_to_import.id not in existing_ids:
            add_recipe_to_book(recipe_to_import, bite_book_book_path)
            recipe_count += 1
            print(f"Import: '{recipe_to_import.title}' has been added.")
        else:
            skipped_count += 1
            print(f"Import: '{recipe_to_import.title}' has been skipped as its 'id' matches a current 'id'.")

    print(f"\nThe import has finished. {recipe_count} recipe(s) imported, {skipped_count} skipped.\n")

    






