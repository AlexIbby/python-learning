import json
from urllib.request import urlopen
import urllib.request


api_key = 'de42831cb837cfa3ca687d3e0d1c68c9'


# getMovie() function returns the details of movie into a dictionary. It uses nested fucntions with other API calls to get details like cast and crew.
# It allows easy access for addtional API calls by including the TMDB ID

def getMovie(search_term: str):
    movie_result = {}

    # search_term = "The Avengers"  # str(input("Movie Title?: "))
    if " " in search_term:
        search_term = search_term.replace(" ", "%20")

    # GET Search-Movie

    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=en-US&query={search_term}&page=1&include_adult=false"

    response = urlopen(url)
    movie_search_json_file = json.loads(response.read())
    movie_data = movie_search_json_file['results'][0]

    # Indentify values from API JSON object to be entered into the movie dictionary

    original_title = movie_data['original_title']
    movie_overview = movie_data['overview']
    tmdb_id = movie_data['id']
    poster_path = movie_data['poster_path']
    backdrop_path = movie_data['backdrop_path']
    release_date = movie_data['release_date']

    # Add basic detail values to the movie dictionary
    movie_result['original_title'] = original_title
    movie_result['movie_overview'] = movie_overview
    movie_result['tmdb_id'] = tmdb_id
    movie_result['poster_path'] = poster_path
    movie_result['backdrop_path'] = backdrop_path
    movie_result['release_date'] = release_date

    # Add top 5 billed actors to the movie dictionary using the getCredits function
    credits = getCredits(movie_result)

    string_cast = str(credits[0])
    string_director = str(credits[1])

    movie_result['cast'] = string_cast
    movie_result['director'] = string_director

    return(movie_result)


def getCredits(movie_result: dict):
    credits = []
    cast_list = []
    director = []

    movie_id = movie_result['tmdb_id']
    credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}&language=en-US"
    credits_response = urlopen(credits_url)
    credits_search_json_file = json.loads(credits_response.read())
    on_screen_credits_data = credits_search_json_file['cast']
    crew_data = credits_search_json_file['crew']

    for item in on_screen_credits_data[:5]:
        actor = item['name']
        character = item['character']
        x = f"{character} played by {actor}"
        cast_list.append(x)

    for item in crew_data:
        if item['job'] == 'Director':
            director = item['name']

    

    credits.append(cast_list)
    credits.append(director)

    return credits


# Function to grab runtime, genre, rating
# Model will need to add categories
#Database add will need to change too
# def movieDetails(movie_result):

# movie_result = getMovie("Indpendence Day 1996")




