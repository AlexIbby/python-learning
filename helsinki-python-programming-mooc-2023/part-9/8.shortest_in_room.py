# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name


class Room:
    def __init__(self):
        self.people = []

    
    def add(self, person:"Person"):
        self.people.append(person)


    def is_empty(self):
        return not self.people 
    
    
    def total_height(self):
        total = 0
        for person in self.people:
            total += person.height 

        return total 

        
    
    def print_contents(self):
        if self.people == []:
            print(f"There are 0 persons in the room, and their combined height is 0cm")

        else:
            print(f"There are {len(self.people)} persons in the room, and their combined height is {self.total_height()} cm")

            for person in self.people:
                print(f"{person.name} ({person.height} cm)")

    

    def shortest(self):
        if self.people == []:
            return None 
        
        else:
            sorted_people = sorted(self.people, key=lambda person: person.height)
            return sorted_people[0]

    def remove_shortest(self):
        if self.people == []:
            return None 
        
        else:
            sorted_people = sorted(self.people, key=lambda person: person.height)
            removed_person = sorted_people[0]


            for person in self.people:
                if person.name == removed_person.name:
                    self.people.remove(person)

            

            return removed_person


        
