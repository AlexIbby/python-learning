# Write your solution here
# Write your solution here

def print_sudoku(sudoku:list):
    modified_sudoku = []  # create a new list to hold the modified rows
    for i, row in enumerate(sudoku):
        modified_row = []  # create a new list to hold the modified items in the row
        for j, item in enumerate(range(len(row))):
            if sudoku[i][j] == 0:
                modified_row.append("_")  # append the modified item to the modified row
            else:
                modified_row.append(str(sudoku[i][j]))  # convert non-zero items to string and append
        modified_sudoku.append(modified_row)  # append the modified row to the modified sudoku
    
    # print formatting
    for i, row in enumerate(modified_sudoku):
        for j, item in enumerate(range(len(row))):
            if j == 3:
                modified_sudoku[i].insert(3, "")
            if j == 7:
                modified_sudoku[i].insert(7, "")
                
    # printing 
    for i, row in enumerate(modified_sudoku):
        row = " ".join(row)
        if i == 3:
            print()
            
        elif i == 6:
            print()
        print(row)

#add number function
def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):

    sudoku_copy = []

    for row in sudoku:
        row_copy = []
        for element in row:
            row_copy.append(element)
        sudoku_copy.append(row_copy)

    sudoku_copy[row_no][column_no] = number
    return sudoku_copy