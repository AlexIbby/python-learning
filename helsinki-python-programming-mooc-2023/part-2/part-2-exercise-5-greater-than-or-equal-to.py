# Write your solution here

number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))

if number1 == number2:
    print("The numbers are equal!")

elif number1 > number2:
    print(f"The greater number was: {number1}")

elif number2 > number1:
    print(f"The greater number was: {number2}")