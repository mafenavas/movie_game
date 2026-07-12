import json

# Define dictionary of movies and their information
movies = None

with open ('movie_game.json') as f:
    movies = json.load(f)

for movie in movies:
    print(f"Movie: {movie}")
    for key, value in movies[movie].items():
        print(f"{key}: {value}")
    print()

print("Welcome to Movie Directory. Let's start")

user_choice= (str(input('Please choose the action you want to do: ' \
'\n1. Add a new movie ' \
'\n2. Edit an existing movie ' \
'\n3. Delete a movie ' \
'\n4. Search a movie: ')))

if user_choice == '1':
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

elif user_choice == '2':
    edit_movie = input('Please type the movie do you want to update: ')
    edit_details = input('Please type what kind of info do you want to update: ')
    user_new_info = input('Type the new info: ')
    
    movies[edit_movie][edit_details] = user_new_info

    with open('movie_game.json', 'w') as f:
        json.dump(movies, f)

elif user_choice == '3':
    deleted_movie = input('Please type the movie you want to delete: ')

    del movies[deleted_movie]

    with open('movie_game.json', 'w') as f:
        json.dump(movies, f)


    for movie in movies:
        print(f"Movie: {movie}")
        for key, value in movies[movie].items():
            print(f"{key}: {value}")
        print()

else:
    search_type = input('Please type the info related to the movie you want to search: ')
    search_info = input('Please the info related to the movie: ')

    for movie in movies:
        for key, value in movies[movie].items():
            if str(key) == search_type and str(value) == search_info:
                print(f"{movie}")



