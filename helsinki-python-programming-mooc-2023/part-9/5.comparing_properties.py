# Write your solution here:

class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self, another:"RealProperty"):
        return self.square_metres > another.square_metres 
    
    def price_difference(self, another:"RealProperty"):
        return abs((self.square_metres * self.price_per_sqm) - (another.square_metres * another.price_per_sqm))


    def more_expensive(self,another:"RealProperty"):
        return (self.square_metres * self.price_per_sqm) > (another.square_metres * another.price_per_sqm) 
    

