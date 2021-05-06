from fastapi import APIRouter

router = APIRouter(
    prefix='/movie',
    tags=['Movie'],
    responses={404: {'description': 'Not found'}}
)


@router.get('/')
async def get_movie_detail():
    pass
