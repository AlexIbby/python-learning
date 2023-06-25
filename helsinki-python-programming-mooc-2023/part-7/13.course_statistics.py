# Write your solution here

import urllib.request
import json 

from math import floor

def retrieve_all():

    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = json.loads(my_request.read())

    currently_active = []

    for item in data:
        if item['enabled'] == True:
            sum_of_exercises = sum(item['exercises'])
            add_to_list = (item['fullName'], item['name'], item['year'], sum_of_exercises)
            currently_active.append(add_to_list)


    return currently_active


def retrieve_course(course_name:str):

    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = json.loads(my_request.read())

    #get weeks
    weeks = len(data)

    total_students = 0
    total_hours  = 0
    exercise_total = 0
    first_key = int(list(data.keys())[0])

    range_weeks = weeks

    if first_key == 1:
        range_weeks +=1 

    #get total students & hour totals and exercise totals
    for i in range(first_key,range_weeks):
        #students 
        weekly_student = data[f"{i}"]['students']

        if weekly_student > total_students:
            total_students = weekly_student

        #hours total
        weekly_hours = data[f"{i}"]['hour_total']

        total_hours += weekly_hours

        #exercise total
        exercise_weekly = data[f"{i}"]['exercise_total']

        exercise_total += exercise_weekly




    
    hours_average = floor(total_hours/total_students)
    exercise_average = floor(exercise_total / total_students)

    return_dict = {
        'weeks': weeks,
        'students': total_students,
        'hours': total_hours, 
        'hours_average': hours_average,
        'exercises': exercise_total, 
        'exercises_average': exercise_average
    }

    return return_dict

    

    
      
