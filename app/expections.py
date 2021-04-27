from fastapi import HTTPException, status

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

notfound_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail='Not found'
)

badrequest_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail='Incorrent parameter'
)
