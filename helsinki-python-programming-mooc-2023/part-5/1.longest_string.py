# Write your solution here

def longest(user_list:list):

    longest_word = ""

    for word in user_list:
        if len(word) > len(longest_word):
            longest_word = word 

    return longest_word
