# Write your solution here:

class Series:
    def __init__(self, title:str, seasons:int, genres:list, ratings=None):
        self.title = title
        self.seasons = seasons 
        self.genres = genres
        self.ratings = ratings


    def __str__(self):
        print_ratings = ""
        
        if self.ratings == None:
            number_of_ratings = "no ratings"

        if self.ratings != None and sum(self.ratings) > 0:
            number_of_ratings = len(self.ratings)
            average = sum(self.ratings)/len(self.ratings)
            average = f"{average:.1f}"

            print_ratings = f"{number_of_ratings} ratings, average {average} points"

        else:
            print_ratings = f"{number_of_ratings}"


        return f"{self.title} ({self.seasons} seasons) \ngenres: {', '.join(self.genres)} \n{print_ratings}"
    
    def rate(self, rating):
        if self.ratings == None:
            self.ratings = []

        self.ratings.append(rating)






def minimum_grade(rating:float, series_list):
    found_series = []

    for series in series_list:
        if series.ratings == None or sum(series.ratings) == 0:
            average = 0 
        else:
            average = sum(series.ratings)/len(series.ratings)

        if average >= rating:
            found_series.append(series)
            

    return found_series


def includes_genre(genre:str, series_list:list):
    found_series = []

    for series in series_list:
        if genre in series.genres:
            found_series.append(series)


    return found_series

