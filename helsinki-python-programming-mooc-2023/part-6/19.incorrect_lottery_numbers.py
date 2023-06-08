# Write your solution here

def filter_incorrect():

    correct_numbers = []

    #C:\Users\alexa\AppData\Local\tmc\vscode\mooc-programming-23\part06-19_incorrect_lottery_numbers\src\lottery_numbers.csv

    with open(r"lottery_numbers.csv", "r") as file:

        for line in file:

            weekPass = False 
            numberPass = False 

            original_line = line.strip()
            original_line += "\n"

            line = line.strip()
            line = line.split(";")

            #numbers 
            lottery_numbers = line[1]

            #verify week
            week = line[0]
            week = week.split(" ")

            week_number = week[1]

            try:
                week_number = int(week_number)
                weekPass = True 
            
            except:
                continue 


            #verify week
            lottery_numbers = lottery_numbers.split(",")

            ##verify length
            if len(lottery_numbers) != 7:
                continue 

            ##check if all numbers are int and in range

            check_int = check_all_int(lottery_numbers)

            if check_int != 7:
                continue 

            ##check duplicates

            if len(lottery_numbers) != len(set(lottery_numbers)):
                continue 

            numberPass = True 
            correct_numbers.append(original_line)

    #write to correct
    with open("correct_numbers.csv", "w") as file:
         for line in correct_numbers:
             file.write(line)


            


def check_all_int(lottery_numbers):
    count = 0

    for number in lottery_numbers:
        try:
            int(number)
            if int(number) >= 1 and int(number) <= 39:
                count += 1
        except:
            continue 

    return count 








    





    