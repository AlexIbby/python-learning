# Write your solution here

value_of_gift = int(input("Value of gift: "))
tax_owed = 0

#under 5000
if value_of_gift < 5000:
    print("No tax!")

#value 5000 - 25000
elif (value_of_gift >= 5000) and (value_of_gift <= 25000):
    tax_owed += 100
    tax_owed += (value_of_gift - 5000) * .08

#value 25000 - 55000
elif (value_of_gift >= 25_000) and (value_of_gift <= 55_000):
    tax_owed += 1700 
    tax_owed += (value_of_gift - 25000) * .10

#value 55 000 — 200 000
elif (value_of_gift >= 55_000) and (value_of_gift <= 200_000):
    tax_owed += 4700 
    tax_owed += (value_of_gift - 55_000) * .12

#value 200_000 - 1_000_000
elif (value_of_gift >= 200_000) and (value_of_gift <= 1_000_000):
    tax_owed += 22_100 
    tax_owed += (value_of_gift - 200_000) * .15

elif value_of_gift >= 1_000_000:
    tax_owed += 142_100 
    tax_owed += (value_of_gift - 1_000_000) * .17

#print tax owed 
if tax_owed > 0:
    print(f"Amount of tax: {tax_owed} euros")
