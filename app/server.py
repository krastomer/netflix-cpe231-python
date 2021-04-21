from fastapi import FastAPI
from .routers import token

app = FastAPI()

app.include_router(token.router)


@app.get('/')
def index():
    return {'text': 'hello'}
