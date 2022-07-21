temperature = int(input("Please type in a temperature (F):"))

print(f"{temperature} degrees Fahrenheit equals {(temperature - 32) *(5/9)} degrees Celsius")

if temperature < (0):
    print("Brr! It's cold in here!")


