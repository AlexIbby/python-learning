# Write your solution here

userInput = None 

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    userInput = str(input("Function: "))


    #Add Word
    if userInput == "1":
        finnishWord = str(input("The word in Finnish: "))
        englishWord = str(input("The word in English: "))

        with open(r"dictionary.txt", "a") as dictionary:
            dictionary.write(f"{finnishWord} - {englishWord}\n")

        print("Dictionary entry added")
    
    if userInput == "2":
        searchTerm = str(input("Search term: "))

        matchingWords = []

        with open(r"dictionary.txt", "r") as dictionary:

            for line in dictionary:
                line = line.strip()
                line = line.split("-")

                if searchTerm in line[0] or searchTerm in line[1]:
                    matchingWords.append(f"{line[0]}-{line[1]}")

            for match in matchingWords:
                print(match)
    

    if userInput == "3":
        print("Bye!")
        break 





