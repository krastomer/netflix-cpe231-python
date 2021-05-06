from typing import List
from pydantic import BaseModel


class MovieDetail(BaseModel):
    name: str
    actors: List
    directors: List
    year: int
    rate: int
    genres: List
    description: str
    n_episode: int
    n_season: int
