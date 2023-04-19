# Write your solution here

def block_correct(sodoku:list, row_no:int , column_no:int):
    
   sodoku_row_1 = sodoku[row_no][column_no:column_no + 3]
   sodoku_row_2 = sodoku[row_no + 1][column_no:column_no + 3]
   sodoku_row_3 = sodoku[row_no + 2][column_no:column_no + 3]
   
   full_row = sodoku_row_1 + sodoku_row_2 + sodoku_row_3
   

   for i in range(1,10):
       if full_row.count(i) > 1:
            return False
    
   return True
