# Write your solution here

def shortest(user_list:list):
    shorty = None 

    for word in user_list:

        if shorty == None:
            shorty = word

        if shorty != None:
            if len(word) < len(shorty):
                shorty = word

    return shorty 

