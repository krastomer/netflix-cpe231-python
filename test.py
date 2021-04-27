from database.database import SessionLocal
from database import schemas
from database import schemas, crud, models
from database.database import SessionLocal, engine


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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

models.Base.metadata.create_all(bind=engine)

y = get_db()
x = crud.create_user(db=SessionLocal(), user=user)
if x is None:
    print('a fuck')
print('done')
