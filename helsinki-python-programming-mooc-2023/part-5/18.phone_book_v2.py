# Write your solution here

phonebook = {}

user_input = None 

while True:
    user_input = str(input("command (1 search, 2 add, 3 quit): "))

    #Search Option - 1
    if user_input == "1":
        name = str(input("name: "))

        if name not in phonebook:
            print("no number")
        
        else:
            for number in phonebook[name]:
                print(number )

    #Add Option - 2
    elif user_input == "2":
        name = str(input("name: "))
        number = str(input("number: "))

        if name not in phonebook:
            phonebook[name] = []
            phonebook[name].append(number)
            print("ok!")

        else:
            phonebook[name].append(number)
            print("ok!")


    elif user_input == "3":
        print("quitting...")
        break 