from fastapi import FastAPI,HTTPException
from schema.initial import MovieCreate, MovieResponse
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

#helper function
def getNextMovieId():
    last_movie = Movies[-1]
    return last_movie["MovieId"] + 1

# Simple get request
@app.get('/getMovies')
def getMovies():
    return Movies

# Get Request using Path parameter
@app.get('/getMovie/{id}')
def getMovie_id(id:int):
    for movie in Movies:
        if movie.get('MovieId') == id:
            return movie

    raise HTTPException(status_code=404,detail="Movie Not Found")

# Get Request using Query Parameter
@app.get('/getMovie')
def getMovie(MovieName:str):
    MovieSet = []
    for movie in Movies:
        if movie.get('MovieName').casefold() == MovieName.casefold() :
            MovieSet.append(movie)
            return MovieSet

    raise HTTPException(status_code=404,detail="Movie Not Found")


# simple post request
@app.post('/AddMovie',response_model=MovieResponse)
def add_movie(movie:MovieCreate):
    movie_dict = movie.model_dump()
    movie_dict["MovieId"] = getNextMovieId()
    Movies.append(movie_dict)
    return movie_dict