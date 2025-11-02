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
            pattern = r"^[^,\n]+,[^,\n]+(?:,[^,\n]+)?$"
            if not re.match(pattern, input_movies):
                print("Please enter 2 or 3 movies separated by commas.")
                continue
            movies = [movie.strip() for movie in input_movies.split(',')]
            movies_number = len(set(movie.lower() for movie in movies))
            if not (1 < movies_number < 4):
                print("Please enter 2 or 3 unique movies only.")
                continue
            break
            
    users[name] = movies

def find_best_match(name, users):
    common_numbers = {}
    for user in users.keys():
        if user == name:
            continue
        common_numbers[user] = similarity(name, user)
        
    common_numbers = dict(sorted(common_numbers.items(), reverse=True))
    max = -1
    for user, score in common_numbers.items():
        if score > max:
            max = score
            best_match = user
        
    return best_match
        
def similarity(user_a, user_b):
    movies_a = set(users[user_a])
    movies_b = set(users[user_b])
    common_movies = movies_a.intersection(movies_b)
    return len(common_movies)

users = load_users()
name = input("Enter your name: ").strip()
get_or_create_user(name)
best_match_user = find_best_match(name, users)
print(f"Your best match is: {best_match_user}")
save_users(users)