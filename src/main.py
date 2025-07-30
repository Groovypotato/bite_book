from recipe import Recipe
from data_manager import add_recipe_to_book
file_path = "./static/recipes.json"
def create_recipe(title,ingredients,instructions,tags):
   new_recipe = Recipe(title=title,url=test_url)
   new_recipe.set_ingredients(ingredients)
   new_recipe.set_instructions(instructions)
   new_recipe.set_recipe_tags(tags)
   return new_recipe

test_title = "Bear Paw Cookies"
test_ingredients = """1 cup unsalted butter softened
1 cup sugar
1 egg
1 tsp vanilla extract
2 cups flour
1 tsp baking powder
1/2 tsp baking soda
1/4 tsp salt
1 bag of ghiradelli dark chocolate melting wafers only need 24 wafer chips
1 bag of semi sweet chocolate chips only 3 chips go onto each cookie for the claws"""
test_instructions = """Preheat oven to 350 degrees
Line cookie sheet with a cookie mat (or parchment paper) and set aside
Using a stand mixer, cream together the butter and sugar.
Add in the egg, vanilla and beat to combine.
Add in the baking soda, baking powder, salt and flour and beat until a soft dough forms.
Measure out into .5 ounce balls of dough and roll into balls. Roll in extra granulated sugar!
Place dough onto cookie sheet 2 inches apart and bake 9-12 minutes.
Once cookies are baked, place a melting wafer into the center of the cookie for the pad of the paw
Then place 3 chocolate chips above the paw for the claws.
Repeat steps with remaining dough and cookies.
Let cookies cool for about 30 minutes before enjoying!"""
test_tags = """Cookies"""
test_url ="""https://kitchenfunwithmy3sons.com/bear-paw-cookies/"""

test_title2 = """3-Ingredient Stovetop Mac and Cheese Recipe"""
test_ingredients2 = """6 ounces (170 g) elbow macaroni
Salt
6 ounces (180 ml) evaporated milk
6 ounces (170 g) grated mild or medium cheddar cheese, or any good melting cheese, such as Fontina, Gruyère, or Jack"""
test_instructions2 = """Place macaroni in a medium saucepan or skillet and add just enough cold water to cover. 
Add a pinch of salt and bring to a boil over high heat, stirring frequently. 
Continue to cook, stirring, until water has been almost completely absorbed and macaroni is just shy of al dente, about 6 minutes.
Immediately add evaporated milk and bring to a boil. 
Add cheese. 
Reduce heat to low and cook, stirring continuously, until cheese is melted and liquid has reduced to a creamy sauce, about 2 minutes longer. 
Season to taste with more salt and serve immediately. """
test_tags2 = """Kenji
cheese"""
test_url2 = """https://www.seriouseats.com/ingredient-stovetop-mac-and-cheese-recipe"""

test_title3 = """Feta Za’atar Biscuits"""
test_ingredients3 = """DAIRY
2 sticks unsalted butter, divided (Molly used Kerrygold unsalted!)
6 ounces feta cheese (block, not crumbled)
1 cup buttermilk
PANTRY
2 ½ cups all-purpose flour
1 tablespoon baking powder
2 ½ tablespoons za’atar spice blend, divided
1 tsp kosher salt
1 tsp sugar
Flaky sea salt
"""
test_instructions3 = """1. Do some prep:
Preheat the oven to 425. Line a baking sheet with parchment paper.
Throw 1½ sticks (12 tablespoons) of unsalted butter onto a small plate and store in the fridge for at least 10 minutes (and up to an hour) to ensure it is very very cold.
Thinly slice a 6-ounce chunk of feta (if it’s packed in brine, you’ll want to pat it dry first using paper towels) into ” thick planks. Doesn’t matter if they break–they are going to get scattered over the dough after it’s rolled out.
2. Make the dough
In a large bowl, whisk together 2 ½ cups all purpose flour, 1 tablespoon baking powder, 1½ tablespoons za’atar spice blend, 1 teaspoon salt and 1 teaspoon sugar.
Once the butter is very cold and hard, set a box grater over the bowl of flour, and grate the 12 tablespoons of butter on the large holes, right into the flour. Use your hands to lighly toss and fluff the flour to coat the butter.
Using a wooden spoon, make a well it the middle of the flour mixture. Pour 1 cup buttermilk into the well. Stir with the wooden spoon, starting in the center, until the dough sticks together in large clumps. There will still likely be a fair amount of unincorporated flour–don’t worry–we’ll get there.
Once the clumps have started to form, dump the contents of the bowl out onto a clean work surface. Using your hands, pat and knead the dough a bit until it comes together in a singular mass, and the loose floury bits start to become incorporated – it may seem like there’s a lot of excess flour but it will eventually become one! Once it’s mostly all incorporated, use a rolling pin or a wine bottle to roll the dough into a large 1 1/2” thick rectangle.
Scatter about a third of the feta planks over one half rectangle. Fold the rectangle in half to enclose the feta. Reroll the dough again into a 1 1/2” rectangle (you may want to add some flour to your surface throughout this process to avoid sticking). Add another third of the feta, fold the dough in half, and roll again. Repeat one last time (now all of the feta should be rolled into the dough.
From here, shape the dough into a 6” x 9” rectangle. Do your best to square off the edges but don’t worry too much! Using a sharp, floured knife, cut the dough into 6 equal squares. Transfer the biscuits to the prepared baking sheet. Keep chilled while you finish the last step.
3. Sizzle the za’atar in butter and bake:
In a small saucepan, melt the remaining 4 tablespoons of butter, along with another heaping tablespoon of za’atar spice blend. Once the foaming subsides and the butter smells fragrant, remove from the heat, 1-2 minutes.
Remove the biscuits from the fridge. Lightly brush the tops of each one with some melted za’atar butter.
Bake, rotating once halfway through, until golden brown at all the edges, 20-25 minutes.
Just before serving, brush with more of the za’atar butter (reheat it gently if you need to), and sprinkle with flaky sea salt. Serve warm (I promise they are soooo much better warm, it’s worth it. If you have to reheat them, do it!). Store in an airtight container, and reheat at 375, for about 5 minutes."""
test_tags3 = """Molly
Biscuits"""
test_url3 =""""""


test_title4 = """Apple Cider Bundt Cake"""
test_ingredients4 = """Cake
2 cups plus 2 tablespoons (266 g) all-purpose flour, spooned and leveled
1 teaspoon baking powder
1/2 teaspoon baking soda
3/4 teaspoon salt
1 teaspoon ground cinnamon
1/2 teaspoon ground ginger
1/4 teaspoon ground nutmeg
1/8 teaspoon ground cloves
3/4 cups (170 g) unsalted butter, room temperature
3/4 cup (150 g) dark brown sugar, packed
1/2 cup (100 g) granulated sugar
3 eggs, room temperature
1 teaspoon vanilla
1/3 cup full fat sour cream, room temperature
3/4 cup apple cider (not apple juice)
Topping
3 tablespoons unsalted butter, melted
1/4 cup granulated sugar
1 1/2 teaspoons ground cinnamon
pinch of nutmeg
Glaze
1 1/2 cups confectioners sugar, sifted
4–6 tablespoons apple cider (or milk)"""
test_instructions4 = """Preheat oven to 350° F.
Whisk together flour, baking powder, baking soda, salt and spices in a medium bowl. Set aside.
In the bowl of a stand mixer, or using a hand held mixer, beat the butter and sugars together on medium until light and fluffy. Scrape down the sides of the bowl.
Reduce the mixer to low and add the eggs one at a time. Scrape down the sides of the bowl between each addition.
Add the vanilla and sour cream. Mix well.
Mix in the flour mixture, alternating with the apple cider. Begin and end with the flour. Mix until just incorporated.
Spray a 12-cup bundt pan with non-stick baking spray.
Transfer the batter to the bundt pan, smoothing the top with a spatula.
Place the bundt pan on a large baking sheet and bake for 45-50 minutes. The cake is done when a toothpick inserted in the top of the cake comes out clean or with a few crumbs remaining. Do not over bake.
Remove the cake from the oven and cool in the pan on a wire rack for 10 minutes. After 10 minutes, invert the cake onto a plate or platter. Cool the cake completely before adding the cinnamon sugar topping.
To coat the cake, use a pastry brush to coat the entire cake with the melted butter. Mix together the sugar, cinnamon and nutmeg in a small bowl.
Immediately sprinkle the cake generously with the cinnamon sugar mixture, using your hands to press it gently into the top and sides of the cake. Use all of the cinnamon sugar topping.
To make the glaze, stir together the confectioners sugar and apple cider (or milk). Whisk until smooth but pourable. If the glaze is too thick, add more cider or milk. If too thin, add more sugar. Drizzle over the cinnamon sugar topping."""
test_tags4 = """Cake"""
test_url4 ="""https://www.brownedbutterblondie.com/apple-cider-bundt-cake/?sf152665861=1#tasty-recipes-8797-jump-target"""


test_title5 = """After-School Banana Bread"""
test_ingredients5 = """Nonstick baking spray, for the pan
8 tablespoons (1 stick) salted butter, melted and cooled, plus softened butter for serving
1 cup packed light brown sugar
2 large eggs, beaten
1 1/2 teaspoons pure vanilla extract
4 to 5 very ripe bananas, mashed (I like to leave them a little chunky)
1 3/4 cups all-purpose flour
1 teaspoon baking soda
1/2 teaspoon kosher salt
1/2 cup chopped pecans (optional; see Cook’s Note)
1 to 2 tablespoons granulated sugar as needed"""
test_instructions5 = """Preheat the oven to 350°F. Spray an 8 x 8-inch pan with nonstick baking spray or line it with parchment paper.
In a stand mixer fitted with the paddle attachment (or in a large bowl with a handheld electric mixer), beat together the butter, brown sugar, eggs, and vanilla until well blended. Add the bananas and mix until combined.
In a medium bowl, whisk together the flour, baking soda, and salt. Add the dry ingredients to the wet ingredients and beat just until combined. Add the pecans (if using) and mix until combined.
Pour the batter into the prepared pan and spread it evenly. Sprinkle the granulated sugar over the top. I like to cover the whole surface completely with sugar; use as much as you’d like.
Bake until a tester inserted in the center comes out clean, 45 to 50 minutes. Let the bread cool slightly in the pan on a rack. Slice and serve warm with butter.
When completely cooled, cover the pan with foil and store at room temperature for up to 2 days."""
test_tags5 = """Banana"""
test_url5 ="""https://magnolia.com/blogs/recipe/after-school-banana-bread"""


def main():
  test_recipe = create_recipe(test_title,test_ingredients,test_instructions,test_tags)
  test_recipe2 = create_recipe(test_title2,test_ingredients2,test_instructions2,test_tags2)
  test_recipe3 = create_recipe(test_title3,test_ingredients3,test_instructions3,test_tags3)
  test_recipe4 = create_recipe(test_title4,test_ingredients4,test_instructions4,test_tags4)
  test_recipe5 = create_recipe(test_title5,test_ingredients5,test_instructions5,test_tags5)
  test_recipe5.print_recipe_card()
  add_recipe_to_book(test_recipe,file_path)
  add_recipe_to_book(test_recipe2,file_path)
  add_recipe_to_book(test_recipe3,file_path)
  add_recipe_to_book(test_recipe4,file_path)
  add_recipe_to_book(test_recipe5,file_path)






if __name__ == "__main__":
    main()