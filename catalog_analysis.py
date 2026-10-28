import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

# Этап 1.
def average_rating(movies):
    return round(sum(movie["rating"] for movie in movies) / len(movies) if movies else 0, 1)

def catalog_age_stats(movies, current_year=2026):
    years = [current_year - movie["year"] for movie in movies]
    oldest_movie = movies[years.index(max(years))]["title"] if years else None
    newest_movie = movies[years.index(min(years))]["title"] if years else None
    avg_age = math.ceil(sum(years) / len(years))
    return oldest_movie, newest_movie,  avg_age

def duration_in_hours(duration_min):
    return (f"{duration_min // 60}ч {duration_min % 60}мин")

# Этап 2.
def rating_tear(rating):
    if rating >= 9.0:
        return "шедевр"
    elif rating >= 7.0:
        return "хорошо"
    else:
        return "средне" if rating >= 5.0 else "слабо"

def decade_label(year):
    match year:
        case _ if year < 2015:
            return "Старые"
        case _ if 2015 <= year <= 2020:
            return "Недавние"
        case _ if 2020 < year:
            return "Новые"
        
# Этап 3.

for movie in movies:
    if "comedy" in movie["genres"]:
         continue
    else:
         print(f"{movie['title']}")
            

i = 0
while i < len(movies):
    if movies[i]["rating"] > 9.0:
        print(movies[i]['title'])
        break
    i += 1
else:
    print("Шедевров не найдено")

def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
        else:
            continue
    return count

# Этап 4.
def normalize_title(title):
    normalized = str(title)
    for i in range(len(normalized)):
        if i == 0 or normalized[i - 1] == " ":
            normalized = normalized[:i] + normalized[i].upper() + normalized[i + 1:]
    else:
        normalized = normalized[:i] + normalized[i].lower() + normalized[i + 1:]
    return normalized

def make_slug(title):
    return str(title).lower().replace(" ", "-")

def format_report_line(movie):
        return str(f"{normalize_title(movie["title"])} ({movie["year"]}) - \
{movie["rating"]}/10, {duration_in_hours(movie["duration_min"])}, \
жанры: {', '.join(movie["genres"])}")
    
# Этап 5.
def titles_sorted_by_rating(movies):
    return sorted(movies, key=lambda x: x["rating"], reverse=True)

def top_n_by_rating(movies, n):
    result = []
    movies = titles_sorted_by_rating(movies)
    for movie in movies[:n]:
        result.append((movie["title"], movie["rating"]))
    return result

# Этап 6.
def count_by_genre(movies):
    genre_count = {}
    for movie in movies:
        for genre in movie.get('genres', []):
            genre_count[genre] = genre_count.get(genre, 0) + 1
    return genre_count  

def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        title = movie.get('title')
        for actor in movie.get('actors', []):
            filmography[actor] = filmography.get(actor, []) + [title]
    return filmography

high_rating_movies = {
    movie["title"]: movie["rating"] for movie in movies if \
movie["rating"] > average_rating(movies)
}

# Этап 7.
def all_genres(movies):
    genres = set()
    for movie in movies:
        genres.update(movie.get('genres', []))
    return genres

def common_actors(movie_1, movie_2):
    if movie_1["actors"] and movie_2["actors"]:
        result = set(movie_1["actors"]) & set(movie_2["actors"])
        return result if result else "У фильмов нет общих актеров"

def genres_only_in_one(movie_a, movie_b):
    return set(movie_a.get('genres', [])) - set(movie_b.get('genres', []))

# Этап 8.
def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie

total_duration = sum(movie["duration_min"] for movie in movies if movie["rating"] > 7)
print(f"Суммарная длительность: {total_duration}")

# Для проверки
print("-----------------ВЫВОД ЭТАПОВ-----------------")

print(".............ЭТАП 1.............")
print(average_rating(movies))
print(catalog_age_stats(movies))
for movie in movies:
    print(duration_in_hours(movie["duration_min"]))

print(".............ЭТАП 2.............")
for movie in movies:
    print(rating_tear(movie["rating"]))
for movie in movies:
    print(decade_label(movie["year"]))

print(".............ЭТАП 3.............")
print(count_long_movies(movies))

print(".............ЭТАП 4.............")
print(normalize_title([movies[0]["title"]]))
print(make_slug([movies[0]["title"]]))
print(format_report_line(movies[0]))

print(".............ЭТАП 5.............")
print(titles_sorted_by_rating(movies[:1]))
print(top_n_by_rating(movies,3))

print(".............ЭТАП 6.............")
print(count_by_genre(movies))
print("\n")
print(actor_filmography(movies))
print("\n")
print(high_rating_movies)

print(".............ЭТАП 7.............")
print(all_genres(movies))
print("\n")
print(common_actors(movies[0],movies[3]))
print(common_actors(movies[0],movies[6]))
print("\n")
print(genres_only_in_one(movies[5:6], movies[:5]))
print(genres_only_in_one(movies[0], movies[3]))