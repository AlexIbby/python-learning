# Write your solution here

points = int(input("How many points [0-100]: "))

# less than zero
if points < 0:
    print("impossible!")

#0-49
elif points >= 0 and points <= 49:
    print("fail")

# 50 - 59
elif points >=50 and points <= 59:
    print("Grade: 1")

# 60 - 69
elif points >=60 and points <= 69:
    print("Grade: 2")

#70 - 79
elif points >=70 and points <= 79:
    print("Grade: 3")

#80 - 89
elif points >=80 and points <= 89:
    print("Grade: 4")

#90 - 99
elif points >=90 and points <= 100:
    print("Grade: 5")

else:
    print("impossible!")