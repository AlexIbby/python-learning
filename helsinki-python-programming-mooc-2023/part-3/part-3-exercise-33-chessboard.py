
# Write your solution here
def chessboard(number:int):
    original_number = number * 1
    row = number * 1
    board = 1
    numbers = []
    while number != 0:
        while row != 0:
            if row != 1:
                print(f"{board}", end="")
                
            else:
                print(f"{board}")
            
            numbers.append(board)
            
            # switch numbers
            if board == 1:
                board = 0
            else:
                board = 1
            row -= 1
            
        
        if (len(numbers) % 2 == 0) and board == 0 and original_number % 2 == 0:
            board = 1
            
        elif (len(numbers) % 2 == 0) and board == 1 and original_number % 2 == 0:
            board = 0
        
        number -=1
        row = original_number


# Testing the function
if __name__ == "__main__":
    chessboard(3)
