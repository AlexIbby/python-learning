# Write your code here

def hash_square(number:int):
    row = number * 1
    while number != 0:
        print("#"*row)
        number -= 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)