# Fix the program
points = int(input("How many points are on your card? "))


#Under 100 Points
if points < 100:
    factor = 1.1
    print("Your bonus is 10%")
    

#Over 100 Points 
if points >= 100:
    factor = 1.15
    print("Your bonus is 15%")

points *= factor
print(f"You now have {points} points")
