# Write your solution here:

class Person:
    def __init__(self, name:str):

        

        self.name = name 
        
    
    def return_first_name(self):
        first_name = self.name.split(" ")
        first_name = first_name[0]
        return first_name
    
    def return_last_name(self):
        last_name = self.name.split(" ")
        last_name = last_name[1]
        return last_name
    
    













