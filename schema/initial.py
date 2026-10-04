from pydantic import BaseModel
from fastapi import FastAPI


app = FastAPI()

class MovieCreate(BaseModel):
    MovieName : str
    Director: str
    Language: list[str]


class MovieResponse(MovieCreate):
    MovieName: str