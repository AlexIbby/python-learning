# Write your solution here

def all_the_longest(user_list:list):

    long_words = []
   
    longest_word = None
   
    #find longest word length
    for word in user_list:
        
        if longest_word == None:
            longest_word = word
            
        else:
            if len(word) > len(longest_word):
                longest_word = word
                
    
    long_words.append(longest_word)
    
    #find any other same length long words
    for word in user_list:
        
        if word in long_words:
            continue
        
        elif len(word) == len(longest_word):
            long_words.append(word)
            
    
    return long_words

