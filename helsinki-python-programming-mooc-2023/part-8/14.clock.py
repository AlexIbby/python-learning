# Write your solution here:

class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = int(hours)
        self.minutes = int(minutes) 
        self.seconds = int(seconds) 

    
    def __str__(self):
        print_hours = ""
        print_minutes = ""
        print_seconds = ""

        if self.hours < 10:
            print_hours = f"0{self.hours}"
        else:
            print_hours = f"{self.hours}"

        if self.minutes < 10:
            print_minutes = f"0{self.minutes}"
        else:
            print_minutes = f"{self.minutes}"

        if self.seconds < 10:
            print_seconds = f"0{self.seconds}"
        else:
            print_seconds = f"{self.seconds}"     
        
        return f"{print_hours}:{print_minutes}:{print_seconds}"
    
    def set(self, hours, minutes):
        self.hours = int(hours) 
        self.minutes = int(minutes)
        self.seconds = 0
    
    def tick(self):
        self.seconds += 1

        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0

            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1

                if self.hours == 24:
                    self.seconds = 0
                    self.minutes = 0
                    self.hours = 0



        

