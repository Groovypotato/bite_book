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
        all_lines = [self.title] + (self.ingredients or []) + (self.instructions or [])
        all_lines.append("Tags: [" + ", ".join(self.recipe_tags or []) + "]")
        all_lines.append("URL: " + (self.url or "None"))
        longest_line = max(len(line) for line in all_lines)
        self.max_length = min(longest_line + 7, 80)
        title_card = self.title
        tags = "Tags: [" + ", ".join(self.recipe_tags or []) + "]"
        url_display = self.url if self.url else "None"
        top_bottom = "+" + "-" * (self.max_length - 2) + "+"
        print(top_bottom)
        print("| " + "* * * Recipe * * *".center(self.max_length - 4) + " |")
        print("| " + " " * (self.max_length -4) + " |")
        print("| " + title_card.ljust(self.max_length - 4) + " |")
        print(top_bottom)
        print("| " + "* * * Ingredients * * *".center(self.max_length - 4) + " |")
        print(top_bottom)
        for ingredient in self.ingredients:
            wrapped = wrapped_line(ingredient, self.max_length - 6)
            print("| - " + wrapped[0].ljust(self.max_length - 6) + " |")
            for line in wrapped[1:]:
                print("|   " + line.ljust(self.max_length - 6) + " |")
        print(top_bottom)
        print("| " + "* * * Instructions * * *".center(self.max_length - 4) + " |")
        print(top_bottom)
        for instruction in self.instructions:
            wrapped = wrapped_line(instruction, self.max_length - 6)
            print("| - " + wrapped[0].ljust(self.max_length - 6) + " |")
            for line in wrapped[1:]:
                print("|   " + line.ljust(self.max_length - 6) + " |")
            print("| " + " " * (self.max_length -4) + " |")
        print("| " + " " * (self.max_length -4) + " |")
        print("| " + tags.ljust(self.max_length - 4) + " |")
        wrapped_url = wrap_url_line(self.url or "None", self.max_length - 10)
        print("| URL: " + wrapped_url[0].ljust(self.max_length - 10) + "  |")
        for line in wrapped_url[1:]:
            print("|       " + line.ljust(self.max_length - 10) + " |") 
        print(top_bottom)

    def set_ingredients(self,ingredient_list):
        new_ingredient_list = []
        for ingredient in ingredient_list:
            new_ingredient_list.append(ingredient.strip())
            if len(ingredient) > self.max_length:
                 self.max_length = len(ingredient)
        self.ingredients = new_ingredient_list
        
    
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
            self.recipe_tags = new_recipie_tags_list


    def recipe_to_dictionary(self):
        return {
        "id": self.id,
        "title": self.title,
        "ingredients": self.ingredients,
        "instructions": self.instructions,
        "tags": self.recipe_tags,
        "url": self.url
        }
    
def wrapped_line(line: str, width: int):
    if len(line) <= width:
        return [line]
    lines = []
    split_words = line.split()
    current_line = ""
    for word in split_words:
        if len(current_line) + len(word) + 1 <= width:
            if current_line:
                current_line += " "
            current_line += word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines

def wrap_url_line(url: str, width: int):
    return [url[i:i+width] for i in range(0, len(url), width)]