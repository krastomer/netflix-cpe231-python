from database.crud import delete_user_db, get_user_viewer, add_user_viewer
from sqlalchemy.orm.session import Session
from app.dependencies import get_current_active_user, get_db
from database.schemas import UserId, Viewer
from fastapi import APIRouter, Depends
from app.exceptions import fullviewer_exception, badaddviewer_exception, badviewerowner_exception

router = APIRouter(
    prefix='/viewer',
    tags=['Viewer'],
    responses={404: {'description': 'Not found'}}
)


def check_owner_viewer(viewer_id: int, user=UserId, db=Session):
    v_list = get_user_viewer(db, user.id_account)
    v_id_list = [i.id_viewer for i in v_list]
    if viewer_id not in v_id_list:
        return False
    return True


@router.get('/')
async def get_all_viewer(user: UserId = Depends(get_current_active_user), db: Session = Depends(get_db)):
    viewer_list = get_user_viewer(id_account=user.id_account, db=db)
    return viewer_list


@router.post('/')
async def add_viewer(viewer: Viewer, user: UserId = Depends(get_current_active_user), db: Session = Depends(get_db)):
    if viewer.pin_number:
        if not (len(viewer.pin_number) == 4 and viewer.pin_number.isdigit()) or viewer.pin_number:
            raise badaddviewer_exception
    if len(get_user_viewer(id_account=user.id_account, db=db)) == 5:
        raise fullviewer_exception
    v = add_user_viewer(db=db, id_account=user.id_account, viewer=viewer)
    return {'success': True if v else False}


@router.delete('/')
async def delete_viewer(viewer_id: int, user: UserId = Depends(get_current_active_user), db: Session = Depends(get_db)):
    if not check_owner_viewer(viewer_id, user, db):
        raise badviewerowner_exception
    v = delete_user_db(db, viewer=viewer_id)
    return {'success': True if v else False}
