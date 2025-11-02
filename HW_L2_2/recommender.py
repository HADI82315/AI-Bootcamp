import json
import re

def load_users():
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {"Ali": ["Inception", "Matrix"],
                "Sara": ["Titanic", "Inception"]}
        
    return users

def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file)
        
def get_or_create_user(name):
    if name in users.keys():
        print(f"Welcome back, {name}!")
        print("Your recommendations:")
        for movie in users[name]:
            print(f"- {movie}")
            exit()   
    else:
        while True:
            input_movies = input("Enter your favorite movies (comma separated, 2 or 3 movies): ").strip()
            pattern = r"^.+,.+,.+$"
            if not re.match(pattern, movies):
                print("Please enter 2 or 3 movies separated by commas.")
                continue
            movies = [movie.strip() for movie in input_movies.split(',')]
            if not (1 < len(movies) < 4):
                print("Please enter 2 or 3 movies only.")
                continue
            break
            
    users[name] = [movie.strip() for movie in movies.split(',')]

users = load_users()
name = input("Enter your name: ").strip()
get_or_create_user(name)
save_users(users)