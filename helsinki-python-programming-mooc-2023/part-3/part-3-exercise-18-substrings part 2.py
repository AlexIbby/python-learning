# Write your solution here

user_string = str(input("Please type in a string: "))

index = -1
for letter in user_string:
    print(user_string[index:])
    index -= 1
     