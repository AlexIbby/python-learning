# Write your solution here

def sudoku_grid_correct(sodoku:list):

    ##**Check Colmns**##
    check = []
    column_no = 0
    row_no = 0
    
    zeros = []
    
    while column_no != 9:
        x = sodoku[row_no][column_no]
        if x == 0:
            zeros.append(x)
        
        elif x not in check:
            check.append(x)
            
        elif x in check:
            return False
        
        row_no += 1
        
        if row_no == 9:
            column_no += 1
            row_no = 0
            check = []
   ##**Check Rows**##

    for row in sodoku:
        for i in range(1,10):
            if row.count(i) > 1:
                return False 
    
   ##***Check Boxes**##
   
    boxes_complete = 0
    row_number = 0
    first_column = 0
    last_column = 3

    while boxes_complete != 9: 
        sodoku_row_1 = sodoku[row_number][first_column:last_column]
        sodoku_row_2 = sodoku[row_number + 1][first_column:last_column]
        sodoku_row_3 = sodoku[row_number + 2][first_column:last_column]
      
        full_row = sodoku_row_1 + sodoku_row_2 + sodoku_row_3
        for i in range(1,10):
            if full_row.count(i) > 1:
                return False
         
        boxes_complete += 1
        row_number += 3
      
        if boxes_complete == 3:
            row_number = 0
            first_column += 3
            last_column += 3

        elif boxes_complete == 6:
            row_number = 0
            first_column += 3
            last_column += 3
      
     
    return True

