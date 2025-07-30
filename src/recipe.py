class Recipe:
    def __init__(self,title,ingredients= None, instructions = None, recipe_tags = None):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.recipe_tags = recipe_tags
        self.max_length = 0

    def __repr__(self):
        return f"Recipe({self.title},{self.description},{self.ingredients},{self.instructions},{self.recipe_tags})"
    
    def __str__(self):
        return f"{self.title}\n{self.description}\n{self.ingredients}\n{self.instructions}\n{self.recipe_tags}"
    

    def print_recipe_card(self):
        title_card = self.title
        if len(title_card) > self.max_length:
            self.max_length = len(title_card)
        self.max_length = self.max_length +5
        top_bottom = "+" + "-" * (self.max_length - 2) + "+"
        print(top_bottom)
        print("| " + "* * * Recipe * * *".center(self.max_length - 4) + " |")
        print("| " + " " * (self.max_length -4) + " |")
        print("| " + title_card.ljust(self.max_length - 4) + " |")
        print(top_bottom)
        print("| " + "* * * Ingredients * * *".center(self.max_length - 4) + " |")
        print(top_bottom)
        for ingredients in self.ingredients:
            print("| " + ingredients.ljust(self.max_length - 4) + " |")
        print(top_bottom)
        print("| " + "* * * Instructions * * *".center(self.max_length - 4) + " |")
        print(top_bottom)
        for instructions in self.instructions:
             print("| " + instructions.ljust(self.max_length - 4) + " |")
             print("| " + " " * (self.max_length -4) + " |")
        print(top_bottom)

    def set_ingredients(self,text):
        ingredient_list = []
        ingredient_lines = text.splitlines()
        for ingredient in ingredient_lines:
            ingredient_list.append(ingredient)
            if len(ingredient) > self.max_length:
                 self.max_length = len(ingredient)
        self.ingredients = ingredient_list
        
    
    def set_instructions(self,text):
            instructions_list = []
            split_instructions = text.splitlines()
            for instruction in split_instructions:
                instructions_list.append(instruction)
                if len(instruction) > self.max_length:
                 self.max_length = len(instruction)
            self.instructions = instructions_list

    def set_recipe_tags(self,text):
            recipie_tags_list = []
            split_tags = text.splitlines()
            for tag in split_tags:
                recipie_tags_list.append(tag)
            self.recipe_tags = recipie_tags_list
