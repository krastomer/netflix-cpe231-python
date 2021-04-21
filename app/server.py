from app.backend.main import hello_db
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def index():
    return {'test': 'hello'}


if __name__ == '__main__':
    uvicorn.run(app, debug=True)
