# Write your solution here

number = int(input("Please type in a number: "))

counter1 = 1
counter2 = 1 

while counter1 <= number:
    print(f"{counter1} x {counter2} = {counter1 * counter2}")

    counter2 += 1
    if counter2 > number:
        counter1 +=1 
        counter2 = 1