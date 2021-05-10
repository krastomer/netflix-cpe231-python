from database.crud import delete_user_viewer, get_user_viewer, add_user_viewer, update_user_viewer
from sqlalchemy.orm.session import Session
from app.dependencies import get_current_active_user, get_db
from database.schemas import UserId, Viewer
from fastapi import APIRouter, Depends
from app.exceptions import fullviewer_exception, badaddviewer_exception, badviewerowner_exception, database_exception

router = APIRouter(
    prefix='/viewer',
    tags=['User - Viewer'],
    responses={404: {'description': 'Not found'}}
)


def check_owner_viewer(viewer_id: int, user=UserId, db=Session):
    v_list = get_user_viewer(db, user.id_account)
    v_id_list = [i.id_viewer for i in v_list]
    if viewer_id not in v_id_list:
        return False
    return True


def check_pin_number(password: str):
    if password:
        if not (len(password) == 4 and password.isdigit()):
            raise badaddviewer_exception


@router.get('/')
async def get_all_viewer(user: UserId = Depends(get_current_active_user), db: Session = Depends(get_db)):
    viewer_list = get_user_viewer(id_account=user.id_account, db=db)
    return viewer_list


@router.post('/')
async def add_viewer(viewer: Viewer, user: UserId = Depends(get_current_active_user), db: Session = Depends(get_db)):
    check_pin_number(viewer.pin_number)
    if len(get_user_viewer(id_account=user.id_account, db=db)) == 5:
        raise fullviewer_exception
    v = add_user_viewer(db=db, id_account=user.id_account, viewer=viewer)
    if not v:
        raise database_exception
    return {'success': True}


@router.delete('/')
async def delete_viewer(viewer_id: int, user: UserId = Depends(get_current_active_user), db: Session = Depends(get_db)):
    if not check_owner_viewer(viewer_id, user, db):
        raise badviewerowner_exception
    v = delete_user_viewer(db, viewer=viewer_id)
    if not v:
        raise database_exception
    return {'success': True}


@router.put('/')
async def update_viewer(viewer: Viewer, user: UserId = Depends(get_current_active_user), db: Session = Depends(get_db)):
    if not viewer.id_viewer:
        raise badviewerowner_exception
    check_pin_number(viewer.pin_number)
    if not check_owner_viewer(viewer.id_viewer, user, db):
        raise badviewerowner_exception
    v = update_user_viewer(db, viewer)
    if not v:
        raise database_exception
    return {'success': True}
