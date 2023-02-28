# Write your code here

# Write your solution here

user_string = str(input("Please type in a string"))
substring = str(input("Please type in a substring"))


first_occurrence = user_string.find(substring)
second_occurrence = user_string.find(substring, first_occurrence + len(substring))

if second_occurrence != -1:
    print(f"The second occurrence of the substring is at index {second_occurrence}.")
else:
    print("The substring does not occur twice in the string.")