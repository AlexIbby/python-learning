# Write your solution here

user_string = str(input("Please type in a string: "))

length = len(user_string) * -1
counter = -1

while length != 0:
    print(user_string[counter])
    length +=1 
    counter -= 1