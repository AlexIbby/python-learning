# Write your solution here

def read_input(prompt:str, low_end:int, high_end:int):

    while True:

        try:
            user_input = int(input(prompt))
            
            if user_input >= low_end and user_input <= high_end:
                return user_input

        except ValueError:
            pass

        print(f"You must type in an integer between {low_end} and {high_end}")

