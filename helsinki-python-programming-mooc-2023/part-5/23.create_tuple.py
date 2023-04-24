# Write your solution here

def create_tuple(x:int, y:int, z:int):
    items = sorted([x,y,z])

    first_element = items[0]
    second_element = items[-1]
    third_element = sum(items)

    return (first_element,second_element,third_element)
