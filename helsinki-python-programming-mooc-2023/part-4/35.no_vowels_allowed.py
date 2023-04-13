# Write your solution here

def no_vowels(user_str:str):
     word = ""
     vowels = ['a', 'e', 'i', 'o', 'u']

     for character in user_str:
          if character not in vowels:
               word += character

     return word 

