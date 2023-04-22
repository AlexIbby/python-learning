# Write your solution here

def double_items(numbers:list):

    doubled_list = []
    for number in numbers:
        number = number * 2
        doubled_list.append(number)
        
    return doubled_list