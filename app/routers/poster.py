from app.dependencies import get_current_active_user, get_storage
from fastapi import APIRouter, Depends
from database.schemas import UserId
from app.exceptions import badparameter_exception, notfound_exception

router = APIRouter(
    prefix='/poster',
    tags=['Poster'],
    responses={404: {'description': 'Not found'}}
)


@router.get('/')
async def get_poster_all(movie: str = None, user: UserId = Depends(get_current_active_user)):
    if movie == None:
        raise badparameter_exception
    storage = await get_storage()
    list_url = []
    count = 1
    for i in storage.child().list_files():
        if i.name == 'poster/{}/{}.jpg'.format(movie, str(count).zfill(2)):
            list_url.append({count: storage.child(i.name).get_url('')})
            count += 1
    if count == 1:
        raise notfound_exception
    return {movie: list_url}
