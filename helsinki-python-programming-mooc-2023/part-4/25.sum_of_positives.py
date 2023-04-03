# Write your solution here

def sum_of_positives(list_of_ints:int):

    positive_ints = []

    for number in list_of_ints:
        if number > 0:
            positive_ints.append(number)

    return sum(positive_ints)
