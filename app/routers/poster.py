from fastapi import APIRouter, Depends

router = APIRouter(
    prefix='/poster',
    tags=['poster'],
    responses={404: {'description': 'Not found'}}
)


@router.get('/{movie}')
async def get_poster(movie: str):
    return {'text': 'hello'}
