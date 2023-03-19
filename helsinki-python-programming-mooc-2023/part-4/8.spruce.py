# Write your solution here
# You can test your function by calling it within the following block

def spruce(tree:int):
    print("a spruce!")

    rows = 1

    white_space = tree -1
    final_white_space = tree -1
    
    while tree != 0:
        print(white_space * " " + rows * "*")
        rows += 2
        tree -= 1
        white_space -=1
    
    print(" " * final_white_space + "*" )

if __name__ == "__main__":
    spruce(5)