# Write your solution here

def line(number:int, user_string:str):

    if len(user_string) == 0:
        print("*"*number)

    else:
        print(user_string[0]* number )


# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "")