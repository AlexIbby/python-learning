# Write your solution here

def everything_reversed(user_list:list):

    new_list = []

    for word in user_list:
        word = word[::-1]
        
        new_list.append(word)
        
    new_list.reverse()  
        
    return new_list
