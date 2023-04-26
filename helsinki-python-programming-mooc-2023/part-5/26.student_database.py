# Write your solution here

def add_student(students:dict, name:str):
    if name not in students:
        students[name] = {}

    elif name in students:
        pass  
    return students


def print_student(students, name:str):
    if name not in students:
        print(f"{name}: no such person in the database")
    
    elif students[name] == {}:
        print(f"{name}: ")
        if students[name] == {}:
            print(" no completed courses")

    elif students[name] != {}:
        #print name
        print(f"{name}: ")

        #print completed courses
        no_of_courses = len(students[name])
        print(f" {no_of_courses} completed courses: ")

        #print course name and grade     
        for course, grade in students[name].items():
            print(f"  {course} {grade}")

        #average agrade
        total= 0
        for course, grade in students[name].items():
            total += grade
        
        average = total / len(students[name])

        print(f" average grade {average}")


def add_course(students:dict, name:str, course_and_grade:tuple):
    
    course = course_and_grade[0]
    grade = course_and_grade[1]

    if grade == 0:
        pass

    elif course in students[name]:
        if grade < students[name][course]:
            pass

        elif grade >= students[name][course]:
            students[name][course] = grade 

    
    elif course not in students[name]:
        students[name][course] = grade

    return students


def summary(students:dict):
    print(f"students {len(students)}")

    most_courses = []
    #most courses 
    for name, courses in students.items():
        if most_courses == []:
            most_courses.append(name)
            most_courses.append(len(students[name]))

        elif most_courses != []:
            if len(students[name]) > most_courses[1]:
                most_courses[0] = name
                most_courses[1] = len(students[name])

    print(f"most courses completed {most_courses[1]} {most_courses[0]}")

    
    

    best_average = None
    best_average_name = None



    for name, courses in students.items():
        total_courses = 0
        total_grades = 0
        
        
        for grade in courses:
            total_grades += courses[grade]
            total_courses += 1  
        
        average = total_grades / total_courses
        
        if best_average == None:
            best_average = average
            best_average_name = name 
            
        elif best_average != None:
            if average > best_average:
                best_average = average
                best_average_name = name

    print(f"best average grade {best_average} {best_average_name}")




