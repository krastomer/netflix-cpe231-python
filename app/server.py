from fastapi import FastAPI
from .routers import token, user, register

app = FastAPI()

app.include_router(token.router)
app.include_router(user.router)
app.include_router(register.router)


@app.get('/')
def index():
    return {'text': 'hello'}
