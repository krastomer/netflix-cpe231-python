from database.crud import create_user
from database import models, schemas
from database.database import engine
from fastapi import FastAPI
from .routers import token, register, poster

app = FastAPI(
    title='Netflix CPE231 API',
    description='This project for CPE231 Database System used in for education',
    # docs_url=None
)

models.Base.metadata.create_all(bind=engine)

app.include_router(token.router)
app.include_router(register.router)
app.include_router(poster.router)


@app.get('/')
def homepage():
    return {'detail': 'homepage'}
