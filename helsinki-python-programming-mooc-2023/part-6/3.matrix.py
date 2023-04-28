# write your solution here

def matrix_sum():

    matrix_sum = 0

    with open("matrix.txt") as text_file:

        for line in text_file:
            line = line.replace("\n", "")
            line = line.split(",")
            for item in line:
                item = int(item)
                matrix_sum += item

    return matrix_sum



def matrix_max():

    matrix_max = None 

    with open("matrix.txt") as text_file:

        for line in text_file:
            line = line.replace("\n", "")
            line = line.split(",") 
            for item in line:
                item = int(item)

                if matrix_max == None:
                    matrix_max = item 

                elif item > matrix_max:
                    matrix_max = item 
    
    return matrix_max

def row_sums():

    row_sums = []

    with open("matrix.txt") as text_file:

        for line in text_file:
            line = line.replace("\n", "")
            line = line.split(",") 

            line_total = 0

            for item in line:
                item = int(item)
                line_total += item

            row_sums.append(line_total)
    
    return row_sums






