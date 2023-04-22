# Write your solution here

def remove_smallest(numbers: list):
    smallest = min(numbers)
    numbers = numbers.remove(smallest)
