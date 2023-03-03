# Write your code here

# Write your solution here

user_input = int(input("Please type in a number: "))

numbers = list(range(1, user_input + 1))

i = 0

for number in numbers:
    if i == len(numbers) - 1:
        print(numbers[-1])
        break 
    
    if i > len(numbers) - 1:
        break 
    
    
    print(numbers[i + 1])
    print(numbers[i])
    
    i += 2