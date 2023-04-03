# Write your solution here

def even_numbers(list_of_ints:list):

    evens = []

    for number in list_of_ints:
        if number % 2 == 0:
            evens.append(number)

    return evens