# Copy here code of line function from previous exercise and use it in your solution

#line
def line(number:int, user_string:str):

    if len(user_string) == 0:
        print("*"*number)

    else:
        print(user_string[0]* number )

# triangle 
def triangle(size:int,char):
    # You should call function line here with proper parameters
    rows = 1
    length = 1
    while rows <= size:
        line(length, char)
        rows += 1
        length += 1

#shape 
def shape(tri_int:int, tri_char:str, rect_int:int, rect_char:str):
    triangle(tri_int,tri_char)
    
    rows = 0
    while rows < rect_int:
        line(tri_int,rect_char)
        rows +=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")