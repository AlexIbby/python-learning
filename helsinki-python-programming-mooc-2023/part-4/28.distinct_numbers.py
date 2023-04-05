# Write your solution here

def distinct_numbers(user_list:list):
    new_list = []

    for number in user_list:
        if number not in new_list:
            new_list.append(number)

    return sorted(new_list)