# Write your solution here
from datetime import datetime, timedelta

# Intitial Parameters
filename = str(input("Filename: "))
start_date = str(input("Starting date: "))
number_of_days = int(input("How many days: "))

#Fix Start Date
start_date = start_date.split(".")
year = int(start_date[2])
month = int(start_date[1])
day = int(start_date[0])
start_date = datetime(year, month, day)

original_date = start_date.strftime("%d.%m.%Y")


end_date = start_date + timedelta(days=(number_of_days - 1))
end_date = end_date.strftime("%d.%m.%Y")


#Dictionary for days and times

days_and_watchtime = {}

total_watch_time = 0

print("Please type in screen time in minutes on each day (TV computer mobile): \n")

#Add watch time to each day
for _ in range(0,number_of_days):
    formatted_date = start_date.strftime("%d.%m.%Y")
    time_watched = str(input(f"Screen time: {formatted_date}: "))

    time_watched = time_watched.split(" ")

    for time in time_watched:
        total_watch_time += int(time)

    time_watched = f"{time_watched[0]}/{time_watched[1]}/{time_watched[2]}"

    days_and_watchtime[f"{formatted_date}"] = time_watched

    if number_of_days > 1:
        start_date += timedelta(days=1)

average_watch_time = total_watch_time/number_of_days


with open(f'{filename}', 'w') as f:
    f.write(f"Time period: {original_date}-{end_date}\n")
    f.write(f"Total minutes: {total_watch_time}\n")
    f.write(f"Average minutes: {average_watch_time}\n")
    
    for key,value in days_and_watchtime.items():
        f.write(f"{key}: {value} \n")

print("Data stored in file late_june.txt")