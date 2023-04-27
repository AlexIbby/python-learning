# write your solution here

def read_fruits():
    
    fruit_dictionary = {}
    
    with open("fruits.csv") as text_file:
              
              for line in text_file:
                     line = line.replace("\n", "")
                     line = line.split(";")

                     fruit = line[0]
                     price = float(line[1])
                     

                     fruit_dictionary[fruit] = price

    return fruit_dictionary




              
              
    