# Write your solution here

from string import ascii_lowercase
from random import randint

def generate_strong_password(number, add_num:bool, add_special:bool):

    lowers = [char for char in ascii_lowercase]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    special = ["!","?","=","+","-","(",")","#"]

    password = ""


    if add_num == False and add_special == False:
        for i in range(0, number ):
            password += lowers[randint(0,25)]
        

    elif add_num == True and add_special == False:
        for i in range(0, number):

            if len(password) == 0:
                password += lowers[randint(0,25)]
            

            elif len(password) == 1:
                password += numbers[randint(0,9)]

            else:
                choice = randint(1,2)
            
                if choice == 1:
                    password += lowers[randint(0,25)]
                
                else:
                    password += numbers[randint(0,9)]

    elif add_num == True and add_special == True:
        for i in range(0, number):

            if len(password) == 0:
                password += lowers[randint(0,25)]
            
            elif len(password) == 1:
                password += numbers[randint(0,9)]


            elif len(password) == 2:
                password += special[randint(0,7)]
            
            else:
                choice = randint(1,3)
                
                if choice == 1:
                    password += lowers[randint(0,25)]
                
                elif choice == 2:
                    password += numbers[randint(0,9)]

                elif choice == 3:
                    password += special[randint(0,7)]



    elif add_num == False and add_special == True:
        for i in range(0, number):

            if len(password) == 0:
                password += lowers[randint(0,25)]
            
            elif len(password) == 1:
                password += special[randint(0,7)]
            
            else:
                choice = randint(1,2)
                
                if choice == 1:
                    password += lowers[randint(0,25)]
                
                elif choice == 2:
                    password += special[randint(0,7)]

        

    return password 




             
