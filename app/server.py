from fastapi import FastAPI
from .routers import token, user, poster

app = FastAPI()

app.include_router(token.router)
app.include_router(user.router)
app.include_router(poster.router)


@app.get('/')
def index():
    return {'text': 'hello'}
