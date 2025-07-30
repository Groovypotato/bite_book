class Recipe:
    def __init__(self,title,description = None,ingredients= None, instructions = None, recipe_tags = None):
        self.title = title
        self.description = description
        self.ingredients = ingredients
        self.instructions = instructions
        self.recipe_tags = recipe_tags

    def __repr__(self):
        return f"Recipe({self.title},{self.description},{self.ingredients},{self.instructions},{self.recipe_tags})"
    
    def __str__(self):
        return f"{self.title}\n{self.description}\n{self.ingredients}\n{self.instructions}\n{self.recipe_tags}"


    def set_ingredients(self,text):
        ingredient_list = []
        ingredient_lines = text.splitlines()
        for ingredient in ingredient_lines:
            ingredient_list.append(ingredient)
        self.ingredients = ingredient_list
    
    def set_instructions(self,instruction_list):
            instructions = []
            for instruction in instruction_list:
                instructions.append(instruction + "\n")
            self.instructions = instructions

    def set_recipe_tags(self,recipe_tag_list):
            recipie_tags = []
            for tag in recipe_tag_list:
                recipie_tags.append(tag)
            self.recipe_tags = recipie_tags
