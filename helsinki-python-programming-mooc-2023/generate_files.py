part_number = input("What part are you in? ")

exercise_names = [
    "print numbers",
    "fix the code countdown",
    "numbers",
    "powers of two",
    "powers of base n",
    "the sum of consecutive numbers 1",
    "the sum of consecutive numbers 2",
    "string multiplied",
    "the longer string",
    "end to beginning",
    "second and second to last characters",
    "a line of hashes",
    "a rectangle of hashes",
    "underlining",
    "right aligned",
    "a framed word",
    "substrings part 1",
    "substrings part 2",
    "does it contain vowels",
    "find the substring",
    "find all the substrings",
    "the second occurrence",
    "multiplication",
    "first letters of words",
    "factorial",
    "flip the pairs",
    "taking turns",
    "seven brothers",
    "the first character",
    "mean",
    "print many times",
    "a square of hashes",
    "chessboard",
    "a word squared"
]

for i, name in enumerate(exercise_names):
    exercise_number = str(i+1).zfill(2)
    file_name = f"part-{part_number}-exercise-{exercise_number}-{name}.py"
    with open(file_name, "w") as f:
        f.write("# Write your code here")
    print(f"Created file: {file_name}")
