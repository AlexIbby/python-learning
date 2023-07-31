# Write your solution after the class Car

# Do not make changes to the class!
class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"

# WRITE YOUR SOLUTION HERE:

def fastest_car(cars: list):
    fastest_car = None 

    for car in cars:
        if fastest_car == None:
            fastest_car = car

        elif fastest_car != None:
            if car.top_speed > fastest_car.top_speed:
                fastest_car = car 

    return fastest_car.make

        
          



          