# Write your solution here

the_list = []

print(f"The list is now {the_list}")

while True:
    value = str(input("a(d)d, (r)emove or e(x)it: "))

    if value == "d" and len(the_list) == 0:
        the_list.append(1)
        print(f"The list is now {the_list}")
    
    elif value == "d" and len(the_list) != 0:
        x = the_list[-1] + 1
        the_list.append(x)
        print(f"The list is now {the_list}")

    elif value == "r":
        the_list.pop(-1)
        print(f"The list is now {the_list}")

    elif value == "x":
        print("Bye!")
        break 
