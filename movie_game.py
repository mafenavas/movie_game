import json

# Define dictionary of movies and their information
movies = None

with open ('movie_game.json') as f:
    movies = json.load(f)
    print(movies)

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

with open('movie_game.json', 'w') as f:
    json.dump(movies, f)

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

with open('movie_game.json', 'w') as f:
    json.dump(movies, f)

# 3. User can delete any movie

deleted_movie = input('Please type the movie you want to delete: ')

del movies[deleted_movie]

with open('movie_game.json', 'w') as f:
    json.dump(movies, f)


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



