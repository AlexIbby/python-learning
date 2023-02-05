# Write your solution here

year = int(input("Please type in a year: "))
next_leap_year = year 
leap_year = False

while True:
    next_leap_year += 1
    if (next_leap_year % 4 == 0) and (next_leap_year % 100 == 0):
        if (next_leap_year % 400 == 0):
            print(f"The next leap year after {year} is {next_leap_year}")
            break 

    elif (next_leap_year % 4 == 0):
        print(f"The next leap year after {year} is {next_leap_year}")
        break 
