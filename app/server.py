from fastapi import FastAPI
from .routers import token, user, poster

app = FastAPI(
    title='Netflix CPE231 API',
    description='This project for CPE231 Database System used in for education',
    docs_url=None
)

app.include_router(token.router)
app.include_router(user.router)
app.include_router(poster.router)


@app.get('/')
def index():
    return {'text': 'hello'}
