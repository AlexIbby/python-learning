# write your solution here

def largest():

    biggest_number = None 

    with open(r'numbers.txt') as text_file:
        for number in text_file:
            number = int(number)

            if biggest_number == None:
                biggest_number = number 

            else:
                if number > biggest_number:
                    biggest_number = number 

    
    return biggest_number





