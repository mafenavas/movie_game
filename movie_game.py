import json

while True:
    movies = None

    with open ('movie_game.json') as f:
        movies = json.load(f)

    for movie in movies:
        print(f"Movie: {movie}")
        for key, value in movies[movie].items():
            print(f"{key}: {value}")
        print()

    print("Hello there")

    user_choice= (str(input('Please choose the action you want to do: ' \
    '\n1. Add a new movie ' \
    '\n2. Edit an existing movie ' \
    '\n3. Delete a movie ' \
    '\n4. Search a movie:' \
    '\n5. Exit the game: ')))

    if user_choice == '1':
        movie = str(input('Please add a movie '))
        while True:
            try: 
                year = int(input('Add the year the movie was released '))
                break
            except:
                print('The year must be a number!')
        genre = str(input('Type the genre of the movie '))
        director = str(input('Who is the director of the movie '))
        actors = str(input('List three actors from the movie '))

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
        
        try:
            movies[edit_movie][edit_details] = user_new_info
        except:
            print('Invalid movie!')

        with open('movie_game.json', 'w') as f:
            json.dump(movies, f)

    elif user_choice == '3':
            
        deleted_movie = input('Please type the movie you want to delete: ')

        try:
            del movies[deleted_movie]
        except:
            print('Invalid movie!')

        with open('movie_game.json', 'w') as f:
            json.dump(movies, f)


        for movie in movies:
            print(f"Movie: {movie}")
            for key, value in movies[movie].items():
                print(f"{key}: {value}")
            print()

    elif user_choice == '4':
        search_type = input('Please type the detail related to the movie you want to search: ' \
        '\n1. Year' \
        '\n2. Genre' \
        '\n3. Director' \
        '\n4. Actors: ')

        search_info = input('Please the info related to the movie you want to search: ')

        if search_type == 'year' or search_type == 'genre' or search_type == 'director' or search_type == 'actors':
            for movie in movies:
                for key, value in movies[movie].items():
                    if str(key) == search_type and str(value) == search_info:
                        print(f"{movie}")
        else:
            print('Invalid detail!')

    elif user_choice == '5':
        break