# Write your code here

user_string = str(input("Please type in a word: "))
character = str(input("Please type in a character: "))

for i, letter in enumerate(user_string):
    if letter == character:
        if i + 2 < len(user_string):
            print(user_string[i:i+3])
            break 