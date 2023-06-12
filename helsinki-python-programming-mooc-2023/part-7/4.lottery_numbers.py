# Write your solution here
from random import sample 

def lottery_numbers(amount:int, lower:int, upper:int):

    possible_numbers = list(range(lower, upper+1))
    possible_numbers = sorted(sample(possible_numbers, amount))

    return possible_numbers



