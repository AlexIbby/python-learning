# Write your solution here

def most_common_character(user_str:str):

    most_common = []

    for character in user_str:
        if most_common == []:
            most_common.append(character) 
            most_common.append(user_str.count(character))

        if most_common != []:
            if user_str.count(character) > most_common[1]:
                most_common[0] = character
                most_common[1] = user_str.count(character)

    return most_common[0]

        


        


