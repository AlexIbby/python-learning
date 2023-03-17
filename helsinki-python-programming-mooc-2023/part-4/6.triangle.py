# Copy here code of line function from previous exercise
def line(number:int, user_string:str):

    if len(user_string) == 0:
        print("*"*number)

    else:
        print(user_string[0]* number )

def triangle(size:int):
    # You should call function line here with proper parameters
    rows = 1
    length = 1
    while rows <= size:
        line(length, "#")
        rows += 1
        length += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
