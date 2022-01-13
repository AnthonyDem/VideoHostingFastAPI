import shutil

from typing import List
from fastapi import UploadFile, File, APIRouter

video_route = APIRouter()


@video_route.get("/")
async def root():
    return {"massege": "sebis otsyda"}


@video_route.post("/upload_file")
async def upload_file(file: UploadFile = File(...)):
    with open(f'{file.filename}', 'wb') as file_obj:
        shutil.copyfileobj(file.file, file_obj)
    return {"status": "successfully uploaded"}


@video_route.post('/images_upload')
async def upload_images(images: List[UploadFile] = File(...)):
    for image in images:
        with open(f'{image.filename}', 'wb') as image_obj:
            shutil.copyfileobj(image.file, image_obj)
    return {"status": "successfully uploaded"}