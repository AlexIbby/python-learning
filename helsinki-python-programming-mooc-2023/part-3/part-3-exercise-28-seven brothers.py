# Write your code here

# You can test your function by calling it within the following block
# if __name__ == "__main__":
#   seven_brothers()

def seven_brothers():
    names = ["Aapo", "Eero", "Juhani", "Lauri", "Simeoni", "Timo", "Tuomas"]
    names = sorted(names)

    for name in names:
        print(name)