# WRITE YOUR SOLUTION HERE:
class ListHelper:
    def __init__(self):
        pass 

    @classmethod
    def greatest_frequency(cls, my_list: list):

        frequencies = {}

        for item in my_list:
            if item not in frequencies:
                frequencies[item] = 1
            
            else:
                frequencies[item] += 1

        highest_key = 0
        highest_value = 0

        for key, value in frequencies.items():
            if value > highest_value:
                highest_key = key
                highest_value = value 

        
        return highest_key

    @classmethod
    def doubles(cls, my_list:list):

        doubles_list = 0
        collected = []

        for item in my_list:

            count = my_list.count(item)

            if count >= 2 and item not in collected:
                doubles_list += 1 
                collected.append(item)

        
        return doubles_list

