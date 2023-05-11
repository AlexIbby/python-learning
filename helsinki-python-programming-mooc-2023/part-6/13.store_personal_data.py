# Write your solution here

def store_personal_data(person:tuple):

    name = str(person[0])
    age = int(person[1])
    height = float(person[2])

    new_line = f"{name};{age};{height}"

    #write people csv
    with open("people.csv", "a") as file:
        file.write(new_line)


