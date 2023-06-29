# Write your solution here

def smallest_average(person1:dict, person2:dict, person3:dict):
    best_average = 11
    winner = None

    people = [person1, person2, person3]

    for person in people:
        current_average = sum([person['result1'], person['result2'], person['result3']]) / 3
        if current_average < best_average:
            best_average = current_average
            winner = person
            

    return winner

