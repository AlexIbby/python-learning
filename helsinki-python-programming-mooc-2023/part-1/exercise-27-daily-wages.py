hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hourly worked: "))
day_of_the_week = str(input("Day of the week: "))

daily_wages = 0

if day_of_the_week != "Sunday":
    daily_wages = hourly_wage * hours_worked

elif day_of_the_week == "Sunday":
    daily_wages = (hourly_wage * hours_worked) * 2

print(f"Daily wages: {daily_wages} euros")