# Write your solution here

userText = str(input("Write text: "))
userText = userText.split(" ")
import difflib



words = []

with open(r"wordlist.txt") as allWords:

    for line in allWords:
        line = line.strip()
        words.append(line)

newString = []

wrong_words = []

for word in userText:
    if word.lower() in words:
        newString.append(word)
    else:
        wrong_words.append(word)
        word = f"*{word}*"
        newString.append(word)

print(' '.join(newString))
print("suggestions:")
for word in wrong_words:
    suggestions = difflib.get_close_matches(word, words)
    suggestions = ', '.join(word for word in suggestions)
    print(f"{word}: {suggestions}")