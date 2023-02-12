# Write your code here

# Write your solution here

limit = int(input("Limit: "))
consecutive_num = 1
number = 0
written_sum = []

while limit > number:
    written_sum.append(consecutive_num)
    number += consecutive_num
    consecutive_num += 1
    
print_statement = ""
for digit in written_sum:
    
    if digit != written_sum[-1]:
        print_statement += f" {str(digit)} +"
        
    if digit == written_sum[-1]:
        print_statement += f" {str(digit)} = {number}"
        


print(f"The consecutive sum: {print_statement}")