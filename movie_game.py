# Define dictionary of movies and their information
movies = {
    "The Dark Knight": {
        "year": 2008,
        "genre": "Action",
        "director": "Christopher Nolan",
        "actors": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]
    },
    "Inception": {
        "year": 2010,
        "genre": "Sci-Fi",
        "director": "Christopher Nolan",
        "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"]
    },
    "Pulp Fiction": {
        "year": 1994,
        "genre": "Crime",
        "director": "Quentin Tarantino",
        "actors": ["John Travolta", "Samuel L. Jackson", "Uma Thurman"]
    }
}

# 1. User Add a movie

movie = input('Please add a movie ')
year = input('Add the year the movie was released ')
genre = input('Type the genre of the movie ')
director = input('Who is the director of the movie ')
actors = input('List three actors from the movie ')

movies[movie] = {
    'year': year,
    'genre': genre,
    'director': director,
    'actors': actors
}

for movie in movies:
    print(f"Movie: {movie}")
    for key, value in movies[movie].items():
        print(f"{key}: {value}")
    print()

# 2. User can edit any existing movie by updating its info

edit_movie = input('Please type the movie do you want to update: ')
edit_details = input('Please type what kind of info do you want to update: ')
user_new_info = input('Type the new info: ')

movies[edit_movie][edit_details] = user_new_info

# 3. User can delete any movie

deleted_movie = input('Please type the movie you want to delete: ')

del movies[deleted_movie]


for movie in movies:
    print(f"Movie: {movie}")
    for key, value in movies[movie].items():
        print(f"{key}: {value}")
    print()

# 4. User can search any movie and its info

search_type = input('Please type the info related to the movie you want to search: ')
search_info = input('Please the info related to the movie: ')

for movie in movies:
    for key, value in movies[movie].items():
        if str(key) == search_type and str(value) == search_info:
            print(f"{movie}")
        else:
            print('We cannot find the movie you are looking for')


