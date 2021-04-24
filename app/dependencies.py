from app.models.user import UserWithHash
from app.models.token import TokenData
from fastapi import Header, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

# settings
TOKEN_EXPIRES = 30
SECRET_KEY = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
ALGORITHM = 'HS256'

# fakedb
fake_db = {
    "johndoe@example.com": {
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    },
    "kasama.pops@mail.kmutt.ac.th": {
        "full_name": "Kasama Thongsawang",
        "email": "kasama.pops@mail.kmutt.ac.th",
        "password": '$2b$12$Hk1JXca8O5wWLVt21ZqQrulIvd48pY8EMaz0V.X0xhAmDSgNsPNdG',
        "disabled": False,
    },
}

credentials_expection = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Could not validate credentials',
    headers={'WWW-Authenticate': 'Bearer'}
)

incorrect_expection = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Incorrect username or password',
    headers={'WWW-Authenticate': 'Bearer'}
)


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserWithHash(**user_dict)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise credentials_expection
        token_data = TokenData(email=username)
    except JWTError:
        raise credentials_expection
    user = get_user(fake_db, username=token_data.email)
    if user is None:
        raise credentials_expection
    return user
