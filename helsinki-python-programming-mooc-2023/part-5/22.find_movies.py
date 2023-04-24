# Write your solution here

def find_movies(database: list, search_term: str):
    
    found_movies = []

    for movie in database:
        title = str(movie['name']).lower()
        search_term = search_term.lower()

        if search_term in title:
            found_movies.append(movie)

    return found_movies




