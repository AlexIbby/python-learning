# Write your solution here

story = ""

list_of_words = []
last_word = ""

while True:
    word = str(input("Please type in a word: "))

    if (word != "end") and last_word != word:
        story += word + " "
        list_of_words.append(word)
        last_word = word 

    else:
        print(story)
        break 