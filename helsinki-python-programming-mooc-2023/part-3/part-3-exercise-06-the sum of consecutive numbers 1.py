# Write your code here

limit = int(input("Limit: "))
consecutive_num = 1
number = 0

while limit > number:
    number += consecutive_num
    consecutive_num += 1

print(number)