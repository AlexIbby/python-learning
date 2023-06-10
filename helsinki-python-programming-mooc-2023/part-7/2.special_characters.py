# Write your solution here
import string 

from string import ascii_letters, punctuation

def separate_characters(my_string:str):
    ascii_array = []
    punctuation_array = []
    other_array = []

    for letter in my_string:
        if letter in ascii_letters:
            ascii_array.append(letter)

        elif letter in punctuation:
            punctuation_array.append(letter)

        else:
            other_array.append(letter)
    
    return (''.join(ascii_array), ''.join(punctuation_array), ''.join(other_array))


