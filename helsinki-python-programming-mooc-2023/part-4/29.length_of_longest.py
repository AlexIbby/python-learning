# Write your solution here
def length_of_longest(user_list:list):
    
    longest = 0

    for word in user_list:
        if len(word) > longest:
            longest = len(word)

    return longest

