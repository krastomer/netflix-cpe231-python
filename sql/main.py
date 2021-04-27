from sql import schemas, models, crud
from sql.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == '__main__':
    user = schemas.User(
        email='kasama.pops@mail.kmutt.ac.th',
        password='password',
        phone_number='0000000000',
        firstname='Kasama',
        lastname='Thongsawang',
        card_number='1012351230',
        exp_date='2021-10-08',
        security_code='132',
        next_billing='2021-10-08'
    )
    x = crud.create_user(db=get_db(), user=user)
    print('done')
