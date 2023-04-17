# Write your solution here

def row_correct(sodoku:list, row_no:int):
    for i in range(1,10):
        if sodoku[row_no].count(i) > 1:
            return False
    
    return True 