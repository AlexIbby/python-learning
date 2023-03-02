# Write your solution here

user_string = str(input("Please type in a sentence"))
user_string = user_string.split(" ")

for word in user_string:
    print(word[0])