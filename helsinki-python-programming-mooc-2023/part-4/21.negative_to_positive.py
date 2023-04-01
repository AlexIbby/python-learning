# Write your solution here

user_number = int(input("Please type in  a positive integer: "))

for number in range(user_number * -1, user_number + 1):
    if number != 0:
        print(number)