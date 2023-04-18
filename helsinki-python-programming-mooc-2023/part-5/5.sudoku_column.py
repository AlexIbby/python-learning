# Write your solution here

def column_correct(sodoku:list, column_no:int):
    column = []
    check = []
    for number in range(0,9):
        x = sodoku[number][column_no]
        
        if x == 0:
            continue 
        
        elif x not in check:
            check.append(x)
            
        elif x in check:
            return False
            
    return True