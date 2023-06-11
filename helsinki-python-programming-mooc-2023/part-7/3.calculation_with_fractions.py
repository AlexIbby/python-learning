# Write your solution here

from fractions import Fraction

def fractionate(amount:int):

    fraction_array = []
    fraction = Fraction(1,amount)

    for i in range(0, amount):
        fraction_array.append(fraction)

    return fraction_array

    
