from fastapi import FastAPI, UploadFile, File
from .routers import token, user, poster
import shutil

app = FastAPI(
    title='Netflix CPE231 API',
    description='This project for CPE231 Database System used in for education',
    # docs_url=None
)

app.include_router(token.router)
app.include_router(user.router)
app.include_router(poster.router)


@app.get('/')
def index():
    return {'text': 'hello'}


# for uploadfile
# @app.post('/uploadfile')
# async def create_upload_file(file: UploadFile = File(...)):
#     with open(file.filename, 'wb+') as file_object:
#         shutil.copyfileobj(file.file, file_object)

#     return {'filename': file.filename}
