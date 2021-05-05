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

badparameter_exception = HTTPException(
    status_code=status.HTTP_406_NOT_ACCEPTABLE,
    detail='Incorrect parameter'
)

emailvalid_exception = HTTPException(
    status_code=status.HTTP_406_NOT_ACCEPTABLE,
    detail='Email has registered'
)

bademail_exception = HTTPException(
    status_code=status.HTTP_406_NOT_ACCEPTABLE,
    detail='Incorrect email'
)

badpassword_exception = HTTPException(
    status_code=status.HTTP_406_NOT_ACCEPTABLE,
    detail='Incorrect password'
)

badregister_exception = HTTPException(
    status_code=status.HTTP_406_NOT_ACCEPTABLE,
    detail='Incorrect data to register'
)

inactive_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Account didn't active or didn't have payment"
)

fullviewer_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Viewer is full"
)

badaddviewer_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Viewer password not correct"
)

badviewerowner_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Viewer ID not found"
)
