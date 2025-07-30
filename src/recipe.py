class Recipe:
    def __init__(self,title,description = None,ingredients= None, instructions = None, recipetags = None):
        self.title = title
        self.description = description
        self.ingredients = ingredients
        self.instructions = instructions
        self.recipetags = recipetags

    def __repr__(self):
        return f"Recipe({self.title},{self.description},{self.ingredients},{self.instructions},{self.recipetags})"
    
    def __str__(self):
        return f"{self.title}\n{self.description}\n{self.ingredients}\n{self.instructions}\n{self.recipetags}"
    
    
    def set_ingredients(self,ingredient_list):
        ingredients = []
        for ingredient in ingredient_list:
            ingredients.append(ingredient)
        self.ingredients = ingredients
    
    def set_instructions(self,instruction_list):
            instructions = []
            for instruction in instruction_list:
                instructions.append(instruction)
            self.instructions = instructions