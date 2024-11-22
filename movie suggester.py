import tkinter as tk
import random

# List of movies with titles, genres, actors and Movie Ratings
movies = [
    {"title": "M*A*S*H", "year": 1970, "genre": "Comedy", "actors": "Donald Sutherland, Elliot Gould", "rating": "R"},
    {"title": "The Godfather", "year": 1972, "genre": "Drama", "actors": "Marlon Brando, Al Pacino", "rating": "R"},
    {"title": "Star Wars", "year": 1977, "genre": "Sci-Fi", "actors": "Mark Hamill, Harrison Ford", "rating": "PG"},
    {"title": "E.T. the Extra-Terrestrial", "year": 1982, "genre": "Sci-fi", "actors": "Henry Thomas, Drew Barrymore", "rating": "PG"},
    {"title": "Back to the future", "year": 1985, "genre": "Adventure", "actors": "Michael J. Fox, Christopher Lloyd", "rating": "PG"},
    {"title": "Jurrasic Park", "year": 1993, "genre": "Adventure", "actors": "Sam Neil, Laura Dern", "rating": "PG-13"},
    {"title": "The Shawshank Redemption", "year": 1994, "genre": "Drama", "actors": "Tim Robbins, Morgan Freeman", "rating": "R"},
    {"title": "Titanic", "year": 1997, "genre": "Romance", "actors": "Leonardo Dicaprio, Kate Winslet", "rating": "PG-13"},
    {"title": "The Matrix", "year": 1999, "genre": "Sci-Fi", "actors": "Keanu Reeves, Lawrence Fishburn", "rating": "R"},
    {"title": "Gladiator", "year": 2000, "genre": "Action", "actors": "Russell Crowe, Joaquin Phoenix", "rating": "R"},
    {"title": "Eight Crazy Nights", "year": 2002, "genre": "Comedy", "actors": "Adam Sandler, Jackie Sandler, Rob Schneider", "rating": "PG-13"},
    {"title": "The Dark Knight", "year": 2008, "genre": "Action", "actors": "Christian Bale, Heath Ledger", "rating": "PG-13"},
    {"title": "Avatar", "year": 2009, "genre": "Sci-Fi", "actors": "Sam Worthington, Zoe Saldana", "rating": "PG-13"},
    {"title": "Inception", "year": 2010, "genre": "Sci-Fi", "actors": "Leonardo DiCaprio, Joseph Gordon-Levitt", "rating": "PG-13"},
    {"title": "Frozen", "year": 2013, "genre": "Musical", "actors": "Kristen Bell, Idina Menzel", "rating": "PG"},
    {"title": "Avengers: Endgame", "year": 2019, "genre": "Action", "actors": "Robert Downey Jr., Chris Evans", "rating": "PG-13"},
    {"title": "Parasite", "year": 2019, "genre": "Horror", "actors": "Kang-ho Song, Sun-Kyun Lee", "rating": "R"},
    {"title": "Dune", "year": 2021, "genre": "Sci-Fi", "actors": "Timothée Chalamet, Rebecca Ferguson", "rating": "PG-13"},
    {"title": "Spider-Man: No Way Home", "year": 2021, "genre": "Action", "actors": "Tom Holland, Zendaya", "rating": "PG-13"},
    {"title": "The Batman", "year": 2022, "genre": "Action", "actors": "Robert Pattinson, Zoë Kravitz", "rating": "PG-13"},
    {"title": "Babylon", "year": 2022, "genre": "Drama", "actors": "Margot Robbie, Diego Calva", "rating": "R"},
    {"title": "Oppenheimer", "year": 2023, "genre": "Biography", "actors": "Cillian Murphy, Emily Blunt", "rating": "R"},
    {"title": "Barbie", "year": 2023, "genre": "Comedy", "actors": "Margot Robbie, Ryan Gosling", "rating": "PG-13"},
    {"title": "Dune Part Two", "year": 2024, "genre": "Sci-Fi", "actors": "Timothée Chalamet, Zendaya", "rating": "PG-13"},
]   


def suggesting_movie():
    genre = genre_var.get()
    age = int(age_var.get())

    #Filtering Movies based on user inputs
    filtered_movies = [movie for movie in movies if movie['genre'].lower() == genre.lower()]


    #Filtered Movies based on age rating

    if age < 18:
        filtered_movies = [movie for movie in filtered_movies if movie['rating'] in ['G', 'PG,', 'PG-13']]
    else:
        filtered_movies = [movie for movie in filtered_movies if movie['rating'] in ['G', 'PG,', 'PG-13', 'R']]
    
    if filtered_movies:
        movie = random.choice(filtered_movies)
        result = f"Title: {movie['title']}\nYear: {movie['year']}\nGenre: {movie['genre']}\nActors: {movie['actors']}\nRating: {movie['rating']}"
    else:
        result = "I'm sorry, no results were found for a movie based on your preferences."

    result_label.config(text=result)

#Now creating = GUI Window

root = tk.Tk()
root.title("Movie Suggester")

#User input for Preferred Genre
tk.Label(root, text="Preferred Genre:").pack(pady=5)
genre_var = tk.StringVar()
genre_entry = tk.Entry(root, textvariable=genre_var)
genre_entry.pack(pady=5)

#User input for Age
tk.Label(root, text="Your Age:").pack(pady=5)
age_var = tk.StringVar()
age_entry = tk.Entry(root, textvariable=age_var)
age_entry.pack(pady=5)

#Button to get this random movie suggestion
suggestion_button = tk.Button(root, text= " Get your personalized movie suggestion", command=suggesting_movie)
suggestion_button.pack(pady=20)

# Let's create a label to show the result
result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=20)

#Run the main loop/Program
root.mainloop()