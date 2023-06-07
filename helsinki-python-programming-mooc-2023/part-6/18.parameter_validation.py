# Write your solution here

def new_person(name: str, age: int):

    if len(name.split(" ")) < 2:
        raise ValueError("Name contains less than two words ")
    if name == "":
        raise ValueError("Name was an empty string")
    
    if len(name) > 40:
        raise ValueError("Name is longer than 40 characters")
    
    if age < 0:
        raise ValueError("Age is less than zero")
    
    if age > 150:
        raise ValueError("Age is greater than 150")
    
    return (name, age)
    

