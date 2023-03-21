# Write your solution here
def same_chars(user_str:int, index1:int, index2:int):

    if index1 >= len(user_str) or index2 >= len(user_str):
        return False

    elif user_str[index1] == user_str[index2]:
        return True 
    
    else:
        return False 

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))