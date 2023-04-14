# Write your solution here

def no_shouting(user_list:list):

    no_shouting = []

    for word in user_list:
        if word.isupper() == False:
            no_shouting.append(word)

    return no_shouting