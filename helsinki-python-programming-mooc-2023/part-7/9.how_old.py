# Write your solution here

from datetime import datetime

while True:
    birthday = int(input("Day: "))
    birthmonth = int(input("Month: "))
    birthyear = int(input("Year: "))

    birth = datetime(birthyear, birthmonth, birthday)
    millenium = datetime(1999, 12, 31)

    if birth > millenium:
        print("You weren't born yet on the eve of the new millennium.")
        break 

    if millenium > birth:
        difference = millenium - birth 

        print(f"You were {difference.days} days old on the eve of the new millennium.")
        break 



