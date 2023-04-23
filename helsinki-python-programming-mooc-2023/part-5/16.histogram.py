# Write your solution here

def histogram(word:str):

    dictionary = {}

    for letter in word:
        dictionary[letter] = word.count(letter) * "*"

    for key, value in dictionary.items():
        print(key, value) 

    