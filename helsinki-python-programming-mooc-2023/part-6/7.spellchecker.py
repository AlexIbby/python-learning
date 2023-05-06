# write your solution here

userText = str(input("Write text: "))
userText = userText.split(" ")


words = []

with open("wordlist.txt") as allWords:

    for line in allWords:
        line = line.strip()
        words.append(line)

newString = []

for word in userText:
    if word.lower() in words:
        newString.append(word)
    else:
        word = f"*{word}*"
        newString.append(word)

print(' '.join(newString))