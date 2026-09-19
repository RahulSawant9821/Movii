from fastapi import FastAPI

app = FastAPI()

Movies = [
    {"MovieId": 1, "MovieName": "Jumanji", "Director": "Joe Johnston", "Language": "English, French"},
    {"MovieId": 2, "MovieName": "Batman", "Director": "Tim Burton", "Language": "English, French, Spanish"},
    {"MovieId": 3, "MovieName": "Inception", "Director": "Christopher Nolan", "Language": "English, French"},
    {"MovieId": 4, "MovieName": "Titanic", "Director": "James Cameron", "Language": "English, French, Spanish"},
    {"MovieId": 5, "MovieName": "Avatar", "Director": "James Cameron", "Language": "English, French"},
    {"MovieId": 6, "MovieName": "Gladiator", "Director": "Ridley Scott", "Language": "English, Latin"},
    {"MovieId": 7, "MovieName": "The Matrix", "Director": "The Wachowskis", "Language": "English, French"},
    {"MovieId": 8, "MovieName": "Jurassic Park", "Director": "Steven Spielberg", "Language": "English, Spanish"},
    {"MovieId": 9, "MovieName": "Interstellar", "Director": "Christopher Nolan", "Language": "English, French"},
    {"MovieId": 10, "MovieName": "The Dark Knight", "Director": "Christopher Nolan", "Language": "English, French, Spanish"},
]

# Simple get request
@app.get('/getMovies')
def getMovies():
    return Movies

# Get Request using Path parameter
@app.get('/getMovie/{id}')
def getMovie(id:int):
    for movie in Movies:
        if movie.get('MovieId') == id:
            return movie

# Get Request using Query Parameter
@app.get('/getMovie')
def getMovie(MovieName:str):
    MovieSet = []
    for movie in Movies:
        if movie.get('MovieName').casefold() == MovieName.casefold() :
            MovieSet.append(movie)
            return MovieSet