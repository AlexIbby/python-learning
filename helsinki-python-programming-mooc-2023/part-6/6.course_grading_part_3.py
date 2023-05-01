#src\students1.csv
#src\exercises1.csv
#src\exam_points1.csv

student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")
exam_points_file = input("Exam points: ")






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


#Exam points 
with open(exam_points_file) as students:
    
    for line in students:

        parts = line.split(";")
        if parts[0] == "id":
            continue 
    
        id = parts[0].strip()
        exam_points = parts[1:]

        total_exam_points = 0
        for exam_score in exam_points:
            total_exam_points += int(exam_score)
        

        # Add to student record
        if id in student_records:
            student_records[id]['exam_points'] = total_exam_points



for student in student_records:
    name = student_records[student]['name']
    score = student_records[student]['score']
    exam_points = student_records[student]['exam_points']


    #grade
    score = (score/40) * 10
    score = int(score)

    #exec_pts
    student_records[student]['exec_pts'] = score

    grade = score + exam_points
    
    #tot_pts
    tot_pts = grade + 0
    student_records[student]['tot_pts'] = tot_pts




    if grade > 0 and grade <= 14:
        grade = 0
        student_records[student]['grade'] = 0

    elif grade >= 15 and grade <= 17:
        grade = 1
        student_records[student]['grade'] = 1

    elif grade >= 18 and grade <= 20:
        grade = 2
        student_records[student]['grade'] = 2

    elif grade >= 21 and grade <= 23:
        grade = 3
        student_records[student]['grade'] = 3

    elif grade >= 24 and grade <= 27:
        grade = 4
        student_records[student]['grade'] = 4
    
    elif grade >= 28:
        grade = 5
        student_records[student]['grade'] = 5


name_header = 'name'
exec_nbr_header = 'exec_nbr'
exec_pts_header = 'exec_pts.'
exm_pts_header = 'exm_pts.'
tot_pts_header = 'tot_pts.'
grade_header = 'grade'

print(f"{name_header:<30}{exec_nbr_header:<10}{exec_pts_header:<10}{exm_pts_header:<10}{tot_pts_header:<10}{grade_header}")
for student in student_records:
    name = student_records[student]['name']
    exec_nbr = student_records[student]['score']
    exec_pts = student_records[student]['exec_pts']
    exam_pts = student_records[student]['exam_points']
    tot_pts_print = student_records[student]['tot_pts']
    grades_print = student_records[student]['grade']

    print(f"{name:<30}{exec_nbr:<10}{exec_pts:<10}{exam_pts:<10}{tot_pts_print:<10}{grades_print}")





