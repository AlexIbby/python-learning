# Write your solution here

the_list = [1,2,3,4,5]

index = None
new_value = None

while True:
    index = int(input("Index: "))
    if index == -1:
        break 
    new_value = int(input("New Value: "))

    if index != -1:
        the_list[index] = new_value
        print(the_list)