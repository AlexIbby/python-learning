# Write your code here

def squared (word:str, number:int):
    
    original_number = number 
    #word
    index = 0

    #rows
    row_length = number 
    rows = number
    

    while rows != 0:
        while row_length != 0:
            
            if index == len(word):
                index = 0
            
            print(word[index], end="")
            index += 1
            row_length -= 1
            
        rows -= 1 
        row_length = original_number
        print()
            