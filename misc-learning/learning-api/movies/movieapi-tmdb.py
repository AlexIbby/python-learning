import json
from unicodedata import name
from urllib.request import urlopen
import requests


# My API Key:

api_key = 'de42831cb837cfa3ca687d3e0d1c68c9'

search_term = str(input("Movie Title?: "))
if " " in search_term:
    search_term = search_term.replace(" ", "%20")

# GET Search-Movie

url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=en-US&query={search_term}&page=1&include_adult=false"

response = urlopen(url)

movie_search_json_file = json.loads(response.read())

movie_data = movie_search_json_file['results'][0]

# for key, value in movie_data.items():
#     print(key)

movie_title = movie_data['original_title']
plot = movie_data['overview']
movie_id = movie_data["id"]

# for item in movie_data:
#     print(item)

# print(f"{movie_title}\n\nOverview:\n{plot}")


############ Second API Pull for credits #########
# credits search url below

credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}&language=en-US"
credits_response = urlopen(credits_url)
credits_search_json_file = json.loads(credits_response.read())
on_screen_credits_data = credits_search_json_file['cast']
crew_data = credits_search_json_file['crew']


for item in on_screen_credits_data[:5]:
    for_loop_actor = item['name']
    for_loop_character = item['character']
    print(f"{for_loop_character} played by {for_loop_actor}")

# Get Director
for item in crew_data:
    if item['job'] == 'Director':
        print(f"Directed by {item['name']}")
