# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0

        self.numbers_array = []

    def add_number(self, number:int):
        self.numbers +=1 
        self.numbers_array.append(number)

    def count_numbers(self):
        return self.numbers 
    
    def get_sum(self):
        return sum(self.numbers_array)

    def average(self):
        if self.numbers == 0:
            return 0
        else:
            return self.get_sum()/len(self.numbers_array)
        
user_stats = NumberStats()
odd_numbers = NumberStats()
even_numbers = NumberStats()

while True:
    user_input = int(input("Please type in integer numbers: "))

    if user_input != -1:
        user_stats.add_number(user_input)

        #even
        if user_input % 2 == 0:
            even_numbers.add_number(user_input)
        
        else:
            odd_numbers.add_number(user_input)

    elif user_input == -1:
        print(f"Sum of numbers: {user_stats.get_sum()}")
        print(f"Mean of numbers: {user_stats.average()}")
        print(f"Sum of even numbers: {even_numbers.get_sum()}")
        print(f"Sum of odd numbers: {odd_numbers.get_sum()}")
        break 

    
