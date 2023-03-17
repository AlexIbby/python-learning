# Copy here code of line function from previous exercise
def line(number:int, user_string:str):
    if len(user_string) == 0:
        print("*"*number)

    else:
        print(user_string[0]* number)


def square(size, character):
    # You should call function line here with proper parameters
    row = size 

    while row != 0:
        line(size, character)
        row -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")