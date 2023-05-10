# Write your solution here


def filter_solutions():
    correct = []
    incorrect = []

    with open(r"solutions.csv", "r") as file:

        for line in file:
            line = line.strip()
            #raw line for adding later
            raw_line = f"{line}\n"

            line = line.split(";")

            #break out expression, numbers and answer/result
            expression = line[1]
            answer = int(line[2])

            #asess subtraction
            if "-" in expression:
                expression = expression.split("-")
                number1 = int(expression[0])
                number2 = int(expression[1])

                if (number1 - number2 == answer):
                    correct.append(raw_line)
                else:
                    incorrect.append(raw_line)

            #assess addition
            if "+" in expression:
                expression = expression.split("+")
                number1 = int(expression[0])
                number2 = int(expression[1])

                if (number1 + number2 == answer):
                    correct.append(raw_line)
                else:
                    incorrect.append(raw_line)

        #write to correct.csv
        with open("correct.csv", "w") as file:
                for line in correct:
                    file.write(line)

        #write to incorrect.csv
        with open("incorrect.csv", "w") as file:
                for line in incorrect:
                    file.write(line)
        
            

            
                 




