# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}
    if title and genre and rating:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie
    
    else:
        return None

def add_to_watched(user_data, movie):
    if movie not in user_data["watched"]:
        user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    if movie not in user_data["watchlist"]:
        user_data["watchlist"].append(movie)
    return user_data
    
def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            add_to_watched(user_data, movie)
            user_data["watchlist"].remove(movie)

    return user_data
    
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0.0
    
    sum = 0.0
    for movie in user_data["watched"]:
        sum += movie["rating"]
    
    average = sum / len(user_data["watched"])
    return average

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    
    counts = {}
    most_watched_genre = user_data["watched"][0]["genre"]

    for movie in user_data["watched"]:
        genre = movie["genre"]

        if genre not in counts:
            counts[genre] = 0
            
        counts[genre] += 1

        if counts[most_watched_genre] < counts[genre]:
            most_watched_genre = genre

    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    friends_movies = get_friends_movies_list_no_duplicates(user_data["friends"])
    unique_movies = get_unique_list_1_movies(user_data["watched"], friends_movies)

    return unique_movies

def get_friends_unique_watched(user_data):
    friends_movies = get_friends_movies_list_no_duplicates(user_data["friends"])        
    unique_movies = get_unique_list_1_movies(friends_movies, user_data["watched"])

    return unique_movies

def get_friends_movies_list_no_duplicates(friends_list):
    friends_movies = []
    for friend in friends_list:
        for movie in friend["watched"]:
            if movie not in friends_movies:
                friends_movies.append(movie)
    return friends_movies

def get_unique_list_1_movies(list_1, list_2):
    unique_movies = []
    for movie_1 in list_1:
        is_unique = True
        for movie_2 in list_2:
            if movie_1 == movie_2:
                is_unique = False
                break
        if is_unique:
            unique_movies.append(movie_1)
        
    return unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

