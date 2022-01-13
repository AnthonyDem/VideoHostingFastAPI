import shutil

from typing import List
from fastapi import UploadFile, File, APIRouter, Form
from schemas.video_schemas import UploadVideoSchema

video_route = APIRouter()


@video_route.get("/")
async def root():
    return {"massege": "Hello endpoint"}


@video_route.post("/upload_file")
async def upload_file(title: str = Form(...), desc: str = Form(...), file: UploadFile = File(...)):
    info = UploadVideoSchema(title=title, description=desc).dict()
    with open(f'{file.filename}', 'wb') as file_obj:
        shutil.copyfileobj(file.file, file_obj)
    return {"status": "successfully uploaded", "info": info}


@video_route.post('/images_upload')
async def upload_images(images: List[UploadFile] = File(...)):
    for image in images:
        with open(f'{image.filename}', 'wb') as image_obj:
            shutil.copyfileobj(image.file, image_obj)
    return {"status": "successfully uploaded"}


@video_route.get('/video')
async def get_video(title: str = Form(...), desc: str = Form(...)):
    pass
