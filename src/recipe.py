import uuid

class Recipe:
    def __init__(self,title,ingredients= None, instructions = None, recipe_tags = None, url = None, id = None):
        self.id = id if id is not None else str(uuid.uuid4())
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.recipe_tags = recipe_tags
        self.url = url
        self.max_length = 0

    def __repr__(self):
        return f"Recipe({self.title},{self.ingredients},{self.instructions},{self.recipe_tags})"
    
    def __str__(self):
        return f"{self.title}\n{self.ingredients}\n{self.instructions}\n{self.recipe_tags}"


    def print_recipe_card(self):
        title_card = self.title
        tags =  "Tags: [" + ", ".join(self.recipe_tags) + "]"
        if len(title_card) > self.max_length:
            self.max_length = len(title_card)
        self.max_length = self.max_length +7
        top_bottom = "+" + "-" * (self.max_length - 2) + "+"
        print(top_bottom)
        print("| " + "* * * Recipe * * *".center(self.max_length - 4) + " |")
        print("| " + " " * (self.max_length -4) + " |")
        print("| " + title_card.ljust(self.max_length - 4) + " |")
        print(top_bottom)
        print("| " + "* * * Ingredients * * *".center(self.max_length - 4) + " |")
        print(top_bottom)
        for ingredients in self.ingredients:
            print("| " + "- " + ingredients.ljust(self.max_length - 6) + " |")
        print(top_bottom)
        print("| " + "* * * Instructions * * *".center(self.max_length - 4) + " |")
        print(top_bottom)
        for instructions in self.instructions:
             print("| " + "- " + instructions.ljust(self.max_length - 6) + " |")
             print("| " + " " * (self.max_length -4) + " |")
        print("| " + tags.ljust(self.max_length - 4) + " |")
        print("| "+ "URL: " + self.url.ljust(self.max_length - 9) + " |")
        print(top_bottom)

    def set_ingredients(self,ingredient_list):
        new_ingredient_list = []
        for ingredient in ingredient_list:
            new_ingredient_list.append(ingredient.strip())
            if len(ingredient) > self.max_length:
                 self.max_length = len(ingredient)
        self.ingredients = ingredient_list
        
    
    def set_instructions(self,instructions_list):
            new_instructions_list = []
            for instruction in instructions_list:
                new_instructions_list.append(instruction.strip())
                if len(instruction) > self.max_length:
                 self.max_length = len(instruction)
            self.instructions = new_instructions_list

    def set_recipe_tags(self,recipie_tags_list):
            new_recipie_tags_list = []
            for tag in recipie_tags_list:
                new_recipie_tags_list.append(tag.strip())
            self.recipe_tags = recipie_tags_list


    def recipe_to_dictionary(self):
        return {
        "id": self.id,
        "title": self.title,
        "ingredients": self.ingredients,
        "instructions": self.instructions,
        "tags": self.recipe_tags,
        "url": self.url
        }
    
