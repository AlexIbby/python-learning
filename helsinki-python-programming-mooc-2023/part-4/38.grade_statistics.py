# Write your solution here



# Total Points Function
def total_points_function(exam_points_exercises:list):
    total_points_list = []

    for item in exam_points_exercises:
        #exampoints
        exam_points = item[0]

        #exercise points 
        exercise_points = item[1]
        exercise_points = (exercise_points/100) * 10
        exercise_points = int(exercise_points)

        #total points
        total = exam_points + exercise_points
        total_points_list.append(total)
    
    return total_points_list

#Calculate Grades Function 
def grades_function(exam_points_exercises:list):
    
    grades = {
        5:"",
        4:"",
        3:"",
        2:"",
        1:"",
        0:"",
    }
    
    for item in exam_points_exercises:

        #exampoints
        exam_points = item[0]

        #exercise points 
        exercise_points = item[1]
        exercise_points = (exercise_points/100) * 10
        exercise_points = int(exercise_points)

        if exam_points < 10:
            grades[0] += "*"

        elif (exam_points + exercise_points) in range(1,15):
            grades[0] += "*"

        elif (exam_points + exercise_points) in range(15,18):
            grades[1] += "*"

        elif (exam_points + exercise_points) in range(18,21):
            grades[2] += "*"

        elif (exam_points + exercise_points) in range(21,24):
            grades[3] += "*" 

        elif (exam_points + exercise_points) in range(24,28):
            grades[4] += "*" 

        elif (exam_points + exercise_points) in range(28,31):
            grades[5] += "*" 
    
    return grades 

#Points Average Function
def points_average_function(total_points:list):
    return sum(total_points) / len(total_points)

#Pass Percentage Function
def pass_percentage_function(grades:dict):

    passing_grades = 0
    all_grades = 0

    for key,value in grades.items():
        if key == 0:
            x = len(value)
            all_grades += x 

        elif key != 0:
           x = len(value)
           passing_grades += x
           all_grades += x

    if passing_grades == 0 and all_grades == 0:
        return 0
    else:
        x = (passing_grades/all_grades) * 100
        x = round(x,1)
        return x 



#Program

#Get exam points and exercises and then place them into an array
exam_points_and_exercises_completed = []

while True:
    user_input = input("Exam points and exercises completed:")

    if user_input != "":
        user_input = user_input.split(" ")
        user_input = (int(user_input[0]),int(user_input[1]))
        exam_points_and_exercises_completed.append(user_input)

    else:
        break 

total_points = total_points_function(exam_points_and_exercises_completed)
points_average = points_average_function(total_points)
grades = grades_function(exam_points_and_exercises_completed)
pass_percentage = pass_percentage_function(grades)

#Print Everything
print("Statistics:")
print(f"Points average: {points_average}")
print(f"Pass percentage: {pass_percentage}")
print(f"Grade distribution: ")
for key, value in grades.items():
    print(f"  {key}: {value}")




