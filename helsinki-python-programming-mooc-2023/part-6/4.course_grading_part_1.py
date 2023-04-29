# write your solution here

student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")



student_records = {}

#Student File 
with open(student_file) as students:


    for line in students:

        parts = line.split(";")
        if parts[0] == "id":
            continue 

        name = parts[1] + " " + parts[2]
        name = name.strip()
        id = parts[0].strip()

        student_records[id] = {}
        student_records[id]['name'] = name 
        student_records[id]['score'] = 0

#Exercises File
with open(exercise_file) as students:


    for line in students:

        parts = line.split(";")
        if parts[0] == "id":
            continue 

        id = parts[0].strip()
        exercises = parts[1:]

        total = 0
        for exercise in exercises:
            total += int(exercise)
        
        if id in student_records:
            student_records[id]['score'] = total


for student in student_records:
    name = student_records[student]['name']
    score = student_records[student]['score']

    print(name, score )
   






        


        





        




