# Write your solution here

print("Please type in integer numbers. Type in 0 to finish.")
number = None

all_numbers = []
pos_numbers = 0
negative_numbers = 0

while True:
    number = int(input("Number: "))

    if number != 0:
        all_numbers.append(number)
        if number > 0:
            pos_numbers += 1
        
        if number < 0:
            negative_numbers += 1

    if number == 0:
        print(f"Numbers typed in {len(all_numbers)}")
        print(f"The sum of the numbers is {sum(all_numbers)}")
        print(f"The mean of the numbers is {sum(all_numbers) / len(all_numbers)}")
        print(f"Positive numbers {pos_numbers}")
        print(f"Negative numbers {negative_numbers}")
        break 






    