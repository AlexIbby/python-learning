
def print_square(layers):
    # define the letters to use in the square
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # determine the size of the square
    size = layers * 2 - 1

    # initialize the grid with all 'A's
    grid = [['A' for j in range(size)] for i in range(size)]

    # fill in the layers of the square
    for layer in range(layers):
        letter = letters[layers - layer - 1]

        # fill in the top row
        for j in range(layer, size - layer):
            grid[layer][j] = letter

        # fill in the bottom row
        for j in range(layer, size - layer):
            grid[size - layer - 1][j] = letter

        # fill in the left column
        for i in range(layer, size - layer):
            grid[i][layer] = letter

        # fill in the right column
        for i in range(layer, size - layer):
            grid[i][size - layer - 1] = letter

    # print the grid
    for row in grid:
        print("".join(row))

user_letter = int(input("Layers:"))
x = print_square(user_letter)