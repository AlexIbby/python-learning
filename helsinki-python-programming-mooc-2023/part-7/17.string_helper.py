# Write your solution here
import string 

def change_case(orig_string:str):
    newString = ""

    for letter in orig_string:
        if letter in string.ascii_lowercase:
            letter = letter.capitalize()
            newString += letter
        elif letter in string.ascii_uppercase:
            letter = letter.lower()
            newString += letter

        else:
            newString += letter

    return newString

def split_in_half(orig_string: str):

    #one character
    if len(orig_string) == 1:
        return (orig_string)

    #blank
    if len(orig_string) == 1:
        return (orig_string)

    #even length
    if len(orig_string) % 2 == 0:
        split = int(len(orig_string) / 2)

        first_half = orig_string[:split]
        second_half = orig_string[split:]

        return (first_half, second_half)
    
    #odd length
    else:
        split = int((len(orig_string) - 1) / 2)

        first_half = orig_string[:split]
        second_half = orig_string[split:]

        return (first_half, second_half)
    
def remove_special_characters(orig_string: str):
    allowed_chars = list(string.ascii_letters) + list(string.ascii_uppercase) + list(string.digits) + [" "]

    
    newString = ""

    for letter in orig_string:
         if letter in allowed_chars:
             newString += letter

    return newString 