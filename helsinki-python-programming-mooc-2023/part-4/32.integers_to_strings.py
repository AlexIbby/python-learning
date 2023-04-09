# Write your solution here

def formatted(user_list:list):
    new_list = []

    for number in user_list:
        number = "{:.2f}".format(number)
        new_list.append(number)

    return new_list

