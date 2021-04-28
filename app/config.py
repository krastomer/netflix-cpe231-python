from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

TOKEN_EXPIRES = 30
SECRET_KEY = 'de8b533781c224224ea9fe781e3c77035fa4769e077e21b137ec723d45819f1b'
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
