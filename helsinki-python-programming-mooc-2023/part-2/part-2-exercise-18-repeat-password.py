# Write your solution here

password = str(input("Password: "))

while True:
    attempt = str(input("Repeat password: "))

    if attempt != password:
        print("They do not match!")

    elif attempt == password:
        print("User account created!")
        break 