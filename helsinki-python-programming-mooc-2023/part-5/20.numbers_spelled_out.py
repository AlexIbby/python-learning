# Write your solution here
def dict_of_numbers():

    numbers = {}

    numbers[0] = "zero"

    zero_to_nine = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
    ]
    
    ten_to_nineteen = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen"
     ]
    tens = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"
    ]

    #1-10
    for i in range(1,10):
        numbers[i] = zero_to_nine[i-1]
    
    #10-20
    j = 0
    for i in range(10,20):
        numbers[i] = ten_to_nineteen[j]
        j+= 1
    
    #20-30
    j = 0
    
    for i in range(20,30):
        if i == 20:
            numbers[i] = tens[0]
        
        else:
            numbers[i] = tens[0] + "-" + zero_to_nine[j]
            j += 1
            
    #30-40
    j = 0
    
    for i in range(30,40):
        if i == 30:
            numbers[i] = tens[1]
        
        else:
            numbers[i] = tens[1] + "-" + zero_to_nine[j]
            j += 1
            
            
    #40-50
    j = 0
    
    for i in range(40,50):
        if i == 40:
            numbers[i] = tens[2]
        
        else:
            numbers[i] = tens[2] + "-" + zero_to_nine[j]
            j += 1
            
    #40-50
    j = 0
    
    for i in range(40,50):
        if i == 40:
            numbers[i] = tens[2]
        
        else:
            numbers[i] = tens[2] + "-" + zero_to_nine[j]
            j += 1
            
    #50-60
    j = 0
    
    for i in range(50,60):
        if i == 50:
            numbers[i] = tens[3]
        
        else:
            numbers[i] = tens[3] + "-" + zero_to_nine[j]
            j += 1
            
    #60-70
    j = 0
    
    for i in range(60,70):
        if i == 60:
            numbers[i] = tens[4]
        
        else:
            numbers[i] = tens[4] + "-" + zero_to_nine[j]
            j += 1
     
    #70-80
    j = 0
    
    for i in range(70,80):
        if i == 70:
            numbers[i] = tens[5]
        
        else:
            numbers[i] = tens[5] + "-" + zero_to_nine[j]
            j += 1      
 
    #80-90
    j = 0
    
    for i in range(80,90):
        if i == 80:
            numbers[i] = tens[6]
        
        else:
            numbers[i] = tens[6] + "-" + zero_to_nine[j]
            j += 1      

    #80-90
    j = 0
    
    for i in range(90,100):
        if i == 90:
            numbers[i] = tens[7]
        
        else:
            numbers[i] = tens[7] + "-" + zero_to_nine[j]
            j += 1      

    
    
    return numbers 
    
