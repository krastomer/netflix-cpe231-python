from database import models
from database.database import engine
from fastapi import FastAPI
from .routers import token

app = FastAPI(
    title='Netflix CPE231 API',
    description='This project for CPE231 Database System used in for education',
    # docs_url=None
)

models.Base.metadata.create_all(bind=engine)

app.include_router(token.router)


@app.get('/')
def homepage():
    return {'detail': 'homepage'}
