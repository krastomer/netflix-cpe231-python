from database.schemas import UserId
from app.models.movie import MovieDetail
from database.crud import get_actor_movie, get_movie_actors, get_movie_detail_db, get_movie_directors, get_movie_episode_db, get_movie_genres
from app.dependencies import get_current_active_user, get_db
from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends
from app.exceptions import notfound_exception

router = APIRouter(
    prefix='/movie',
    tags=['Movie'],
    responses={404: {'description': 'Not found'}}
)


@router.get('/')
async def get_movie_detail(movie_id: int, db: Session = Depends(get_db),  _: UserId = Depends(get_current_active_user)):
    try:
        actors = get_movie_actors(db, movie_id)
        directors = get_movie_directors(db, movie_id)
        rate, name, description, year, n_episode, n_season = get_movie_detail_db(
            db, movie_id)
        genres = get_movie_genres(db, movie_id)
        return MovieDetail(
            actors=actors,
            directors=directors,
            rate=rate,
            name=name,
            genres=genres,
            description=description,
            year=year,
            n_episode=n_episode,
            n_season=n_season
        )
    except:
        raise notfound_exception


@router.get('/actor')
async def get_list_movie_from_actor(actor: str, db: Session = Depends(get_db), _: UserId = Depends(get_current_active_user)):
    movie_list = get_actor_movie(db, actor)
    if not movie_list:
        raise notfound_exception
    return movie_list


@router.get('/episode')
async def get_movie_episode(movie_id: int, db: Session = Depends(get_db),  _: UserId = Depends(get_current_active_user)):
    episode_list = get_movie_episode_db(db, movie_id)
    if not episode_list:
        raise notfound_exception
    return episode_list
