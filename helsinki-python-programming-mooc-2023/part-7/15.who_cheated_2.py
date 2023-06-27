# Write your solution here

# Write your solution here

import csv 
from datetime import timedelta

def final_points():
    students = {}

    start_times_file = r"start_times.csv"
    submission_file = r"submissions.csv"

    with open(start_times_file) as start_times_csv:
        for line in csv.reader(start_times_csv, delimiter=";"):
            name = line[0]
            start_time = line[1]
            
            if name not in students:
                students[name] = {}
                students[name]["submissions"] = []
            
            students[name]["start_time"] = start_time

    with open(submission_file) as submission_csv:
        for line in csv.reader(submission_csv, delimiter=";"):
            name = line[0]
            task = line[1]
            points = line[2]
            end_time = line[3]

            submission = {
                "task_number": f"{task}",
                "points": f"{int(points)}",
                "end_time": f"{end_time}"
            }

            students[name]['submissions'].append(submission)

    


    cheaters = []

    exam_points = {}
    for student, information in students.items():

        points = 0

        #Create start time + 3 hours

        start_time = information['start_time']
        start_time = start_time.split(":")

        start_delta = timedelta(hours=int(start_time[0]), minutes=int(start_time[1]) )


        start_delta 

        #max difference 
        max_diff = timedelta(hours=3)

        #create dictionary to only award tasks once
        task_dict = {
            '1': 0,
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 0,
            '6': 0,
            '7': 0,
            '8': 0
        }

        #Check all end times
        student_submissions = information['submissions']

        #check if submission for task counts 
        for submissions in student_submissions:
            end_time = submissions['end_time']
            end_time = end_time.split(":")
            end_delta = timedelta( hours=int(end_time[0]), minutes=int(end_time[1]))

            if end_delta < start_delta:
                end_delta += timedelta(days=1)

            difference = end_delta - start_delta

            #if correct timing submission
            if difference < max_diff: 
                task_no = submissions['task_number']
                
                if task_dict[f"{task_no}"] == 0:
                    task_dict[f"{task_no}"] = submissions['points']
        
                
                if submissions['points'] > task_dict[f"{task_no}"]:
                    task_dict[f"{task_no}"] = submissions['points']
            


        total_points = 0
        for key, value in task_dict.items():
            total_points += int(value)

        exam_points[f'{student}'] = total_points

    return exam_points

                


