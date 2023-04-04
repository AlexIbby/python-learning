# Write your solution here

def list_sum(int_list1:list, int_list2:list):

    summed_list = []
    index = 0
    for number in int_list1:
        new_number = number + int_list2[index]
        index +=1 
        summed_list.append(new_number)

    return summed_list

