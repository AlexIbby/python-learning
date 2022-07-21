print("What is the weather forecast for tomorrow?")

temperature = int(input("Temperature:"))

rain = input("Will it rain (yes/no):")

#Over 20 
if temperature > 20: 
    print("Wear jeans and a T-shirt")
#20
if temperature == 20: 
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    
#10-20 degrees

if temperature in range(11,19):
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")

#6-11 degrees
if temperature in range(6,11):
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    


#0-6 degrees
if temperature in range(0,6):
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

#rain
if rain == "yes":
    print("Don't forget your umbrella!") 




