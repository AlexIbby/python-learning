# Write your solution here

def older_people(people:list, year:int):

    oldest = []
    for person in people:
        if person[1] < year:
            oldest.append(person[0])

    return oldest

