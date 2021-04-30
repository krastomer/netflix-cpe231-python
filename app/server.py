from starlette.responses import HTMLResponse
from database import models
from database.database import engine
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from .routers import token, register, poster, payment

app = FastAPI(
    title='Netflix CPE231 API',
    description='This project for CPE231 Database System used in for education',
    docs_url=None
)

models.Base.metadata.create_all(bind=engine)

app.include_router(token.router)
app.include_router(register.router)
app.include_router(poster.router)
app.include_router(payment.router)

templates = Jinja2Templates(directory='app/templates/')


@app.get('/', response_class=HTMLResponse)
def homepage(request: Request):
    return templates.TemplateResponse("index.html", context={'request': request})
