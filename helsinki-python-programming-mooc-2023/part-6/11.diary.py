# Write your solution here



while True:
    print("1 - add an entry, 2 - read entries, 0 - quit: ")
    user_input = str(input("Function: "))
    
    if user_input == "1":

        diary_entry = str(input("Diary entry: "))
        diary_entry = f"{diary_entry}\n"

        with open("diary.txt", "a") as file:
            file.write(f"{diary_entry}")

        print("Diary saved")

    elif user_input == "2":
        with open("diary.txt", "r") as file:
            for line in file:
                print(line)

    else:
        print("Bye now!")
        break 
        
