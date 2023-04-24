# Write your solution here

def oldest_person(people:list):

    oldest = None

    for person in people:
        if oldest == None:
            oldest = person
        
        else:
            if person[1] < oldest[1]:
                oldest = person

    return oldest[0]



