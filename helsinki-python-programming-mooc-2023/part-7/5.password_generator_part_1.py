# Write your solution here

from string import ascii_lowercase
from random import randint

def generate_password(number):

    lowers = [char for char in ascii_lowercase]
    password = ""

    for i in range(0, number):
        password += lowers[randint(0,25)]
    return password




