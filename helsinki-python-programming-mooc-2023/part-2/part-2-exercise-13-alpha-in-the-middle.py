# Write your solution here

#gather letter input 
first_letter = str(input("1st Letter: "))
second_letter = str(input("2nd Letter: "))
third_letter = str(input("3rd Letter: "))

#placing into alphabetically sorted array 
all_letters = [first_letter, second_letter, third_letter]
all_letters = sorted(all_letters)
middle_letter = all_letters[1]

#print middle letter 
print(f"The letter in the middle is {middle_letter}")