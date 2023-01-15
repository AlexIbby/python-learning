print("What is the weather forecast for tomorrow?")
temperature = int(input("Temperature: "))
rain = str(input("Will it rain (yes/no): "))


# Temp > 21 & rain

if temperature > 20 and rain == "no":
    print("Wear jeans and a T-shirt")

elif temperature > 20 and rain == "yes":
    print("Wear jeans and a T-shirt")
    print("Don't forget your umbrella!")

# Temp between 10-20 & rain

if ((temperature <= 20)  & (temperature > 10)) & (rain == "no"):
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")

elif ((temperature <= 20)  & (temperature > 10)) & (rain == "yes"):
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Don't forget your umbrella!")


# Temp between 5-10 & rain

if ((temperature <= 10) & (temperature >=5)) & (rain == "no"):
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")

elif ((temperature <= 10) & (temperature >5)) & (rain == "yes"):
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Don't forget your umbrella!")

# Temp less than 5 & rain

if (temperature <= 5) & (rain == "no"):
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

elif (temperature <= 5)  & (rain == "yes"):
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
    print("Don't forget your umbrella!")

