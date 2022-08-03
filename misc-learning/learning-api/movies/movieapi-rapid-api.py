import json
import requests

url = "https://moviesdb5.p.rapidapi.com/om"

user_search = str(input("Which movie or tv show?:"))

querystring = {f"t": {user_search}}

headers = {
    "X-RapidAPI-Key": "461dd6993fmshc93bcd68e6ef918p10ba4cjsna6071e8763ff",
    "X-RapidAPI-Host": "moviesdb5.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

movie_data = json.loads(response.text)

# Search Result Properties
title = movie_data["Title"]  # Title of Movie
year = movie_data["Year"]  # Year of release (2011-2019)
rated = movie_data["Rated"]   # e.g. TV-MA
released = movie_data["Released"]  # "17th April 2011"
runtime = movie_data["Runtime"]
genre = movie_data["Genre"]
director = movie_data["Director"]
writer = movie_data["Writer"]
actors = movie_data["Actors"]
plot = movie_data["Plot"]  # short plot summary
language = movie_data["Language"]
country = movie_data["Country"]
awards = movie_data["Awards"]  # summary of awards
poster_url = movie_data["Poster"]
imdb_rating = movie_data["imdbRating"]
imdb_votes = movie_data["imdbVotes"]
imdb_id = movie_data['imdbID']


print(f"The IMDB score for {title} is {imdb_rating} on {imdb_votes} votes ")
