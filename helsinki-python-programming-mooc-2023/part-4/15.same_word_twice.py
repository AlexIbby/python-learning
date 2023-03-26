# Write your solution here

words = []

while True:
    new_word = str(input("Word: "))
    if new_word not in words:
        words.append(new_word)
    
    else:
        print(f"You typed in {len(words)} different words")
        break 
