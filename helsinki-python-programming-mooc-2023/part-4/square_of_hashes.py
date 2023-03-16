# Copy here code of line function from previous exercise
def line(number:int, user_string:str):
    if len(user_string) == 0:
        print("*"*number)

    else:
        print(user_string[0]* number)


def square_of_hashes(size):
    # You should call function line here with proper parameters
    
    rows = size

    while rows != 0:
        line(size, "#")
        rows -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
