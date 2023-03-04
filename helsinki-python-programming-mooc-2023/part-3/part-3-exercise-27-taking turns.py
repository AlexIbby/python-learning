# Write your code here

# Write your solution here

user_input = int(input("Please type in a number: "))

numbers = list(range(1, user_input + 1))

front_index = 0
back_index = -1
counter = 0

while counter < len(numbers):
    print(numbers[front_index])
    counter += 1
    
    if counter >= len(numbers):
        break
    
    print(numbers[back_index])
    counter += 1
    front_index += 1
    back_index -= 1