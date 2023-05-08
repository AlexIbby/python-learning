# Write your solution here


name = str(input(" Whom should I sign this to: "))
filename = str(input("Where shall I save it: "))

with open(f"{filename}", "w") as my_file:
    my_file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")