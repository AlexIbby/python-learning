# Write your solution here

# get input
user_string = str(input("Word: "))

#frame logic
frame = 30
white_space = (30 - len(user_string)) / 2

#splitting odds and evens 
left_side = None
right_side = None 

if white_space % 2 == 0:
    left_side = int((white_space - 1)) * " "
    right_side = int(( white_space - 1)) * " "

else:
    left_side = int(white_space) * " "
    right_side = (int(white_space) - 1) * " "