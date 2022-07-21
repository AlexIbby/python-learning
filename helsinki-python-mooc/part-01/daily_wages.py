hourly_wage = float(input("Hourly wage:"))
hours_worked = float(input("Hours worked:"))
day = (input("Day of the week:"))
wages = float(hourly_wage*hours_worked)

if day == ("Sunday"):
    wages = float(hourly_wage*hours_worked*2)

print(f"Daily wages: {wages} euros")



