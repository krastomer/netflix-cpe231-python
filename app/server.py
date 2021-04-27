from fastapi import FastAPI
from starlette.responses import JSONResponse
from .routers import token

app = FastAPI(
    title='Netflix CPE231 API',
    description='This project for CPE231 Database System used in for education'
)

app.include_router(token.router)


@app.get('/')
def home():
    return JSONResponse(content={'page': 'homepage'})
