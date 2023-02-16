# Write your code here

# Write your solution here

user_string = str(input("Please type in a string: "))

if user_string[1] == user_string[-2]:
    print(f"The second and the second to last characters are {user_string[1]}")

else:
    print("The second and the second to last characters are different")