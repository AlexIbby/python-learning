# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):

        if self.seconds == 59:
            self.seconds = 0

            if self.minutes == 59:
                self.minutes = 0
                
            else:
                self.minutes += 1
        
        else:
            self.seconds += 1
    
    def __str__(self):

        print_minutes = ""
        print_seconds = ""

        if self.minutes < 10:
            print_minutes = f"0{self.minutes}"
        else:
            print_minutes = f"{self.minutes}"

        if self.seconds < 10:
            print_seconds = f"0{self.seconds}"
        else:
            print_seconds = f"{self.seconds}"


        return f"{print_minutes}:{print_seconds}"




