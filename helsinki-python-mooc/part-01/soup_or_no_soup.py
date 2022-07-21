soup_cost = (5.90)
name = (input("What is your name:"))
if name == ("Jerry"):
    print("Next please!")

if name !=("Jerry"):
    no_of_portions = int(input("How many portions of soup?"))
    print(f"The total cost is {soup_cost*no_of_portions}")
    print("Next please!")
