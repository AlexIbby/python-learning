# Write your solution here

def invert(dictionary: dict):
    
    new_dict = {}

    for key, value in dictionary.items():
        new_dict[value] = key 
    
    for key, value in new_dict.items():
        del dictionary[value]
        dictionary[key] = value