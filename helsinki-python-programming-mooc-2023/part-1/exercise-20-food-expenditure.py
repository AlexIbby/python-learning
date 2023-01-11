# Write your solution here

cafeteria_spend = float(input("How many times a week do you eat the student cafeteria?"))
caf_lunch = float(input("The price of a typical student lunch?"))
grocery_week = float(input("How much money do you spend on groceries in a week?"))

total_caf_lunch_spend = cafeteria_spend * caf_lunch

total_daily_spend = (total_caf_lunch_spend + grocery_week) / 7
total_weekly_spend = total_caf_lunch_spend + grocery_week

print("Average food expenditure:")
print(f"Daily: {total_daily_spend} euros")
print(f"Weekly: {total_weekly_spend} euros")