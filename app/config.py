from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

TOKEN_EXPIRES = 30
SECRET_KEY = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
ALGORITHM = 'HS256'

firebase_config = {
    'apiKey': "AIzaSyAz-5UqRKZo3VYCB5VH4xQWNzXWESfCuI4",
    'authDomain': "netflix-cpe231.firebaseapp.com",
    'projectId': "netflix-cpe231",
    'storageBucket': "netflix-cpe231.appspot.com",
    'messagingSenderId': "202995106255",
    'appId': "1:202995106255:web:229af33543bfa493e412ba",
    'databaseURL': '',
    'serviceAccount': 'key/firebaseKey.json'
}
