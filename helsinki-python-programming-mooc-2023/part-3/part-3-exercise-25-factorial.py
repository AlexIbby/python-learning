# Write your code here

user_input = int(input("Please type in a number:"))
original_input = user_input * 1
factorial = 1

while user_input > 0:
    factorial = factorial * user_input
    user_input -= 1
    
    if user_input == 0:
        print(f"The factorial of the number {original_input} is {factorial}")
        user_input = int(input("Please type in a number:"))
        original_input = user_input * 1
        factorial = 1
        
print("Thanks and bye!")