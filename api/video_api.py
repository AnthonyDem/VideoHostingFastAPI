import shutil

from typing import List
from fastapi import UploadFile, File, APIRouter, Form

from models.user import User
from schemas.video_schemas import UploadVideoSchema, GetVideoSchema
from models.video import Video

video_route = APIRouter()


@video_route.get("/")
async def root():
    return {"massege": "Hello endpoint"}


@video_route.post("/video")
async def upload_file(title: str = Form(...), desc: str = Form(...), file: UploadFile = File(...)):
    info = UploadVideoSchema(title=title, description=desc).dict()
    with open(f'{file.filename}', 'wb') as file_obj:
        shutil.copyfileobj(file.file, file_obj)
    user = await User.objects.first()
    return await Video.objects.create(user=user, file=file.filename, **info)


@video_route.get('/video/{video_id}', response_model=Video)
async def get_video(video_id: int):
    return Video.objects.select_related("user").get(pk=video_id)
