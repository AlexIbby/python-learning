# Write your solution here

def transpose(matrix: list):
    
    #copy matrix
    matrix_copy = []
    
    for item in matrix:
        matrix_copy.append(item)
    
    #loop through copy to get tranposed values, then change ref
    
    replace_row = []
    new_matrix = []
    
    rows = len(matrix_copy) - 1
    i = 0
    row_helper = 0
    values_changed = 0
    number_helper = 0
    
    counter = 0
    while counter <= rows:
        
        while row_helper < len(matrix[i]):
            
            x = matrix_copy[row_helper][number_helper]
            replace_row.append(x)
            row_helper += 1
            
        
        new_matrix.append(replace_row)
        replace_row = []
        number_helper += 1
        row_helper = 0   
        counter += 1
        
    for i, row in enumerate(matrix):
        matrix[i] = new_matrix[i]

    

    






