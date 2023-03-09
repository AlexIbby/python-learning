# Write your solution here
def print_many_times(word:str, times:int):
    while times != 0:
        print(word)
        times -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)