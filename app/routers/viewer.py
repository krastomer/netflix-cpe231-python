from database.crud import get_viewer
from sqlalchemy.orm.session import Session
from app.dependencies import get_current_active_user, get_db
from database.schemas import UserId
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix='/viewer',
    tags=['Viewer'],
    responses={404: {'description': 'Not found'}}
)


@router.get('/')
async def get_all_viewer(user: UserId = Depends(get_current_active_user), db: Session = Depends(get_db)):
    viewer_list = get_viewer(id_account=user.id_account, db=db)
    return viewer_list
