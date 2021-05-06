from database import models
from database.database import engine
from fastapi import FastAPI
from .routers import token, user, poster, payment, viewer, movie

app = FastAPI(
    title='Netflix CPE231 API',
    description='This project for CPE231 Database System used in for education',
    # docs_url=None
)

models.Base.metadata.create_all(bind=engine)

app.include_router(movie.router)
app.include_router(payment.router)
app.include_router(poster.router)
app.include_router(user.router)
app.include_router(token.router)
app.include_router(viewer.router)


@app.get('/')
def homepage():
    return {'text': 'hello'}
