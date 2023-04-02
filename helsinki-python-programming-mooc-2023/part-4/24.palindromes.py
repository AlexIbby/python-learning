# Write your solution here

def palindromes(user_string:str):
    reversed = user_string
    reversed = list(reversed)
    reversed.reverse()
    reversed = "".join(reversed)

    if reversed == user_string:
        return True

    else:
        return False



while True:
    user_input = str(input("Please type in a palindrome: "))
    if palindromes(user_input) == True:
            print(f"{user_input} is a palindrome!")
            break 

    else:
         print(f"that wasn't a palindrome")


# Note, that at this time the main program should not be written inside
#if __name__ == "__main__":
    
