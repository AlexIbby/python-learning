# Write your solution here

def longest_series_of_neighbours(user_list:list):

    current = 0
    longest = []

    i = 0
    for number in user_list:
        
        if i + 1 >= len(user_list):
            current += 1
            longest.append(current)
            break 
        
        elif abs(user_list[i] - user_list[i+1]) == 1:
            current += 1
            i +=1 

        elif abs(user_list[i] - user_list[i+1]) != 1:
            current += 1
            longest.append(current)
            current = 0
            i+=1

    longest.sort(reverse=True)
    return longest[0]





        



