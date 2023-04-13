# Write your solution here

def count_matching_elements(my_matrix:list, element:int ):
    
    count = 0
    for item in my_matrix:
        element_count = item.count(element)
        count += element_count 
    return count 

