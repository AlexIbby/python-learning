# Write your solution here
import re 
from datetime import datetime 

def is_it_valid(pic:str):

    #Check length 
    if len(pic) != 11:
        return False 
    
    #Check century marker 
    century_marker = pic[6]
    valid_century = ["+","-","A"]

    if century_marker not in valid_century:
        return False 

    #Check personal indentifier
    pin_number = pic[7:10]
    ##Regex 3 digits 
    pattern = r"\d{3}$" 

    if not re.fullmatch(pattern, pin_number):
        return False 
    
    #Check date
    day = pic[0:2]
    month = pic[2:4]
    year = str(pic[4:6])

    #The century marker is either + (1800s), - (1900s) or A (2000s).

    if century_marker == "+":
        year = str(18) + year

    if century_marker == "-":
        year = str(19) + year

    if century_marker == "A":
        year = str(20) + year

    
    year = int(year)
    day = int(day)
    month = int(month)

    try:
        the_date = datetime(year, month, day)
        
    except:
        return False 
    
    #Check control character
    control_char_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']



   
    check_control = str(pic[:6]) + str(pic[7:10])
    check_control = int(check_control)
    check_control = check_control % 31

    if pic[-1] == control_char_array[check_control]:
        return True 
    else:
        return False 
    
    
    







        

        





