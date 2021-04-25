from fastapi import APIRouter, Depends
from firebase_admin import credentials, initialize_app, storage
import firebase_admin
# from ..dependencies import firebase_config

router = APIRouter(
    prefix='/poster',
    tags=['poster'],
    responses={404: {'description': 'Not found'}}
)

firebase_config = {
    'apiKey': "AIzaSyAz-5UqRKZo3VYCB5VH4xQWNzXWESfCuI4",
    'authDomain': "netflix-cpe231.firebaseapp.com",
    'projectId': "netflix-cpe231",
    'storageBucket': "netflix-cpe231.appspot.com",
    'messagingSenderId': "202995106255",
    'appId': "1:202995106255:web:229af33543bfa493e412ba",
    'databaseURL': ''
}

# @router.get('/{movie}')
# async def get_poster(movie: str):
#     return {'text': 'hello'}

cred = credentials.Certificate('key/firebaseKey.json')
firebase = initialize_app(cred, firebase_config)


x = storage.bucket('netflix-cpe231.appspot.com')
y = x.list_blobs()
print('done')
