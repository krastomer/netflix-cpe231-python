from database.database import SessionLocal
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['sha256_crypt'])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
