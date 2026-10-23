import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
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
    total_rating = sum(movie["rating"] for movie in movies)
    return round(total_rating / len(movies) if movies else 0, 1)

def catalog_age_stats(movies, current_year=2026):
    years = [current_year - movie["year"] for movie in movies]
    oldest_movie = movies[years.index(max(years))]["title"] if years else None
    newest_movie = movies[years.index(min(years))]["title"] if years else None
    avg_age = round(sum(years) / len(years), 1) if years else 0
    return oldest_movie, max(years), newest_movie, min(years), avg_age

def duration_in_hours(movies):
    return '\n'.join(f"{movie['title']}: {movie['duration_min'] // 60}ч {movie['duration_min'] % 60}мин" for movie in movies)
# Этап 2.
def rating_tear(rating):
    if rating >= 9.0:
        return "Шедевр"
    elif rating >= 7.0:
        return "Хорошо"
    else:
        return "Средне" if rating >= 5.0 else "Плохо"

def decade_label(year):
    match year:
        case old if year < 2015:
            return "Старые"
        case resent if 2015 <= year <= 2020:
            return "Недавние"
        case new if 2020 < year:
            return "Новые"
# Этап 3.
for movie in movies:
    if movie["genres"] == {"comedy"}:
        continue
    else:
        print(f"{movie['title']}")
i = 0
while i < len(movies):
    if movies[i]["rating"] > 9.0:
        print(f"Первый шедевр из списка: {movies[i]['title']}")
        break
    i += 1
else:
    print("Фильмов с рейтингом выше 9.0 нет")

    



        