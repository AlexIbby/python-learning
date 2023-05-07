# Write your solution here
def search_by_name(filename:str, word:str):

    with open(f"{filename}") as recipes:

        recipe_dictionary = {}


        new_recipe = {}
        recipe_array = []
        lines = recipes.readlines() 

        for i,line in enumerate(lines):

            
            line = line.strip()

            
            if line != "":
                recipe_array.append(line)

            elif line == "":
                name = recipe_array[0]
                prep_time = recipe_array[1]
                ingredients = recipe_array[2:]

                new_recipe['name'] = name
                new_recipe['prep_time'] = prep_time
                new_recipe['ingredients'] = ingredients

                recipe_dictionary[name] = new_recipe

                new_recipe = {}
                recipe_array = []

        if len(recipe_array) >= 3:
            name = recipe_array[0]
            prep_time = recipe_array[1]
            ingredients = recipe_array[2:]

            new_recipe['name'] = name
            new_recipe['prep_time'] = prep_time
            new_recipe['ingredients'] = ingredients

            recipe_dictionary[name] = new_recipe

    matching_recipes = []
    for recipe in recipe_dictionary.values():
        recipe_name = recipe['name']
        recipe_name = recipe_name.lower()
        if word.lower() in recipe_name:
            matching_recipes.append(recipe['name'])

    return matching_recipes
            

def search_by_time(filename:str, prep_time:int):

    with open(f"{filename}") as recipes:

        recipe_dictionary = {}

        new_prep_time = prep_time + 0

        prep_time = ""

        new_recipe = {}
        recipe_array = []
        lines = recipes.readlines() 

        for i,line in enumerate(lines):

            
            line = line.strip()

            
            if line != "":
                recipe_array.append(line)

            elif line == "":
                name = recipe_array[0]
                prep_time = recipe_array[1]
                ingredients = recipe_array[2:]

                new_recipe['name'] = name
                new_recipe['prep_time'] = prep_time
                new_recipe['ingredients'] = ingredients

                recipe_dictionary[name] = new_recipe

                new_recipe = {}
                recipe_array = []

        if len(recipe_array) >= 3:
            name = recipe_array[0]
            prep_time = recipe_array[1]
            ingredients = recipe_array[2:]

            new_recipe['name'] = name
            new_recipe['prep_time'] = prep_time
            new_recipe['ingredients'] = ingredients

            recipe_dictionary[name] = new_recipe

    matching_recipes = []
    for recipe in recipe_dictionary.values():
        time_needed = recipe['prep_time']
        time_needed = int(time_needed)

        if time_needed <= new_prep_time:
            matching_recipes.append(f"{recipe['name']}, preparation time {time_needed} min")
    
    return matching_recipes


            
def search_by_ingredient(filename:str, ingredient:str):

    with open(f"{filename}") as recipes:

        recipe_dictionary = {}

        

        prep_time = ""

        new_recipe = {}
        recipe_array = []
        lines = recipes.readlines() 

        for i,line in enumerate(lines):

            
            line = line.strip()

            
            if line != "":
                recipe_array.append(line)

            elif line == "":
                name = recipe_array[0]
                prep_time = recipe_array[1]
                ingredients = recipe_array[2:]

                new_recipe['name'] = name
                new_recipe['prep_time'] = prep_time
                new_recipe['ingredients'] = ingredients

                recipe_dictionary[name] = new_recipe

                new_recipe = {}
                recipe_array = []

        if len(recipe_array) >= 3:
            name = recipe_array[0]
            prep_time = recipe_array[1]
            ingredients = recipe_array[2:]

            new_recipe['name'] = name
            new_recipe['prep_time'] = prep_time
            new_recipe['ingredients'] = ingredients

            recipe_dictionary[name] = new_recipe

    matching_recipes = []
    for recipe in recipe_dictionary.values():
        
        time_needed = recipe['prep_time']
        ingredients = recipe['ingredients']


        if ingredient in ingredients:
            matching_recipes.append(f"{recipe['name']}, preparation time {time_needed} min")
    
    return matching_recipes
        

