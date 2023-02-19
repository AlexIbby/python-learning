# Write your solution here

user_input = None 

while user_input != "":
    user_input = str(input("Please type in a string: "))
    underline = len(user_input)
    print(user_input)
    print("-"*underline)