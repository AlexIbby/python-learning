from math import sqrt

value_a = int(input("Value of a:"))
value_b = int(input("Value of b:"))
value_c = int(input("Value of c:"))

# Calculate the discriminant
discriminant = value_b**2 - 4*value_a*value_c

# Check if the discriminant is positive, negative, or zero
if discriminant > 0:
    # Calculate the two real roots
    root1 = (-value_b + sqrt(discriminant)) / (2*value_a)
    root2 = (-value_b - sqrt(discriminant)) / (2*value_a)
    print("The roots are", root1, "and", root2) 