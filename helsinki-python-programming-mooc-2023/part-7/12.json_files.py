# Write your solution here

import json 

def print_persons(filename: str):
    with open(filename) as file:
        
        data = file.read()
        courses = json.loads(data)

        for item in courses:
            hobbies = item['hobbies']
            hobbies = f'({", ".join(hobbies)})'

            print(f"{item['name']} {item['age']} years {hobbies}") 
