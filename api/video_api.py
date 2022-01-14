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
async def upload_file(title: str = Form(...), desc: str = Form(...), user_id: int = Form(...), file: UploadFile = File(...)):
    user = await User.objects.get(pk=user_id)
    with open(f'{file.filename}', 'wb') as file_obj:
        shutil.copyfileobj(file.file, file_obj)
    serialized_video = UploadVideoSchema(title=title, description=desc, user=user, file=file.filename).dict()
    return await Video.objects.create(**serialized_video)


@video_route.get('/video/{video_id}', response_model=Video)
async def get_video(video_id: int):
    return await Video.objects.select_related("user").get(pk=video_id)


@video_route.get('/video')
async def get_videos():
    return await Video.objects.select_related("user").all()
