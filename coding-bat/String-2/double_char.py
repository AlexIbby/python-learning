# Problem


# Given a string, return a string where for every char in the original, there are two chars.


# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'

def double_char(str):
    index = 0
    new_string = ""
    for character in str:
        new_string = new_string + (character + character)
    return new_string
