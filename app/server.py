from fastapi import FastAPI
from .routers import token, user

app = FastAPI()

app.include_router(token.router)
app.include_router(user.router)


@app.get('/')
def index():
    return {'text': 'hello'}
