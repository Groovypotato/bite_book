from enum import Enum

class SearchType(Enum):
    TITLE = "title"
    INGREDIENT = "ingredient"
    TAG = "tag"
    ID = "id"

def search_recipes(book,search_type: SearchType,search_term:str):
    results = []
    for recipe in book["recipes"]:
        if search_type == SearchType.TITLE and search_term.lower in recipe["title"].lower():
                results.append(recipe)
        elif search_type == SearchType.INGREDIENT and search_term.lower in recipe["ingredients"].lower():
                results.append(recipe)
        elif search_type == SearchType.TAG and search_term.lower in recipe["tags"].lower():
                results.append(recipe)
        elif search_type == SearchType.ID and search_term.lower in recipe["id"].lower():
                results.append(recipe)
    return results