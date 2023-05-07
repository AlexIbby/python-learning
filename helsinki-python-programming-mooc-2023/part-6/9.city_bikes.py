# Write your solution here
import math  

#Get Station Data

def get_station_data(filename:str = "C:\\Users\\alexa\AppData\\Local\\tmc\\vscode\\mooc-programming-23\\part06-09_city_bikes\\src\\stations1.csv"):
    
    #Create stations dictionary/object
    stations = {}

    # Create dictionaries to organize stations
    with open(filename) as station_csv:

        for i, line in enumerate(station_csv):
            if i == 0:
                continue

            elif i != 0:
                line = line.split(";")

                name = line[3]

                stations[name] = {
                    'name': name, 
                    'lattitude':float(line[1]), 
                    'longitude': float(line[0]), 
                    'FID': int(line[2]),
                    'total_slot': int(line[4]), 
                    'operative': line[5],
                    'id':line[6]
                }
    #Complete exercise task
    task_dictionary = {}

    for station in stations.values():
        task_dictionary[station['name']] = (station['longitude'], station['lattitude'])

    

    return task_dictionary


# Get Station Data

def distance(stations:dict, station1:str, station2:str):
    

    longitude1 = stations[station1][0]
    longitude2 = stations[station2][0]

    lattitude1 = stations[station1][1]
    lattitude2 = stations[station2][1]

    #Calculate distance
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (lattitude1 - lattitude2) * 111.2
    
    distance_km = math.sqrt(x_km**2 + y_km**2)
    

    return distance_km


# Get Station Data

def greatest_distance(stations:dict):

    distance = 0
    station1_winner = ""
    station2_winner = ""
    
    for i, (key1,value1) in enumerate(stations.items()):
       

        for j,(key2,value2) in enumerate(stations.items()):

            #get two stations
            longitude1 = value1[0]
            longitude2 = value2[0]

            lattitude1 = value1[1]
            lattitude2 = value2[1]

            #Calculate distance
            x_km = (longitude1 - longitude2) * 55.26
            y_km = (lattitude1 - lattitude2) * 111.2
            
            distance_km = math.sqrt(x_km**2 + y_km**2)

            if distance_km > distance:
                distance = distance_km
                station1_winner = key1
                station2_winner = key2
                

    
    return (station1_winner, station2_winner, distance)
        



        
                

    




