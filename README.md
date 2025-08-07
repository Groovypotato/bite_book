# 🍴 Bite Book

**All your best recipes, byte-sized!**

Bite Book is a command-line Python application that lets you store, search, edit, and import your favorite recipes from multiple sources like Mealie or other Bite Book JSON files. It keeps your recipe collection organized, customizable, and easily shareable.

---

## 🚀 Features

- 🔍 **Search Recipes** by Title, Ingredient, Tag, or ID
- 📝 **Add Recipes** interactively through terminal prompts
- ✏️ **Edit Recipes** (title, ingredients, instructions, tags, URL)
- 🗑️ **Remove Recipes** by search
- 📦 **Bulk Import**
  - From other Bite Book `.json` files
  - From a folder of Mealie recipe exports
- 🖨️ **Printable Recipe Cards** displayed in a clean, bordered format

---

## 📂 File Structure

```text
bite_book/
├── main.py                # Main application loop
├── data_manager.py        # Recipe creation, save/load logic
├── recipe.py              # Recipe class and formatting
├── search_manager.py      # Search utilities
├── mealie_importer.py     # Mealie export importer
├── bite_book_importer.py  # Bite Book format importer
└── static/
    └── recipes.json       # Your saved recipe book
```

---

## 📥 Bulk Import Formats

### 1. Bite Book JSON Format

Import recipes from another Bite Book `.json` file using this structure:

```json
{
  "recipes": [
    {
      "id": "uuid-string",
      "title": "Recipe Title",
      "ingredients": [
        "ingredient 1",
        "ingredient 2"
      ],
      "instructions": [
        "instruction 1",
        "instruction 2"
      ],
      "tags": [
        "tag1",
        "tag2"
      ],
      "url": "https://optional.source.url"
    }
  ]
}
```

To import:
- Choose **Bulk Import**
- Select **Normal Import**
- Enter path to the `.json` file

### 2. Mealie Export Format

Point to the `recipes` folder inside a Mealie export. Bite Book will find each folder, extract the recipe `.json` inside, and add it to your book.

To import:
- Choose **Bulk Import**
- Select **Mealie Import**
- Enter path to the exported `recipes/` directory

---

## 🧾 Example Recipe Card

Here’s what a recipe looks like in the terminal:

```
+------------------------------------------------------------------------------+
|                    * * * Recipe * * *                                        |
|                                                                              |
| Apple Cider Bundt Cake                                                       |
+------------------------------------------------------------------------------+
|                       * * * Ingredients * * *                                |
+------------------------------------------------------------------------------+
| - Cake                                                                       |
| - 2 cups plus 2 tablespoons (266 g) all-purpose flour, spooned and leveled   |
| - 1 teaspoon baking powder                                                   |
| ...                                                                          |
+------------------------------------------------------------------------------+
|                      * * * Instructions * * *                                |
+------------------------------------------------------------------------------+
| - Preheat oven to 350° F.                                                    |
| - Whisk together flour, baking powder, baking soda, salt and spices.        |
| - Beat the butter and sugars until light and fluffy.                        |
| ...                                                                          |
|                                                                              |
| Tags: [Cake]                                                                 |
| URL: https://kitchenfunwithmy3sons.com/bear-paw-cookies/                    |
+------------------------------------------------------------------------------+
```

---

## 🔧 Running Bite Book

```bash
python main.py
```

Make sure your `recipes.json` exists in the `static/` directory. The application will prompt you through interactive menus.

---

## 💡 Tips

- Separate ingredients/instructions with `<i>` and tags with `<t>` when prompted.
- All data is stored in a single JSON file, making it easy to sync, backup, or share.
- Great for migrating from other platforms or keeping a local archive.

---

## 📜 License

MIT License – use it freely and make it yours!
