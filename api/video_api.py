import shutil

from typing import List
from fastapi import UploadFile, File, APIRouter, Form, BackgroundTasks, HTTPException
from starlette.requests import Request
from starlette.responses import StreamingResponse

from models.user import User
from schemas.video_schemas import UploadVideoSchema, GetVideoSchema
from models.video import Video
from helpers.video_helpers import FileHelper
from services.video_service import VideoService

video_route = APIRouter()


@video_route.get("/")
async def root():
    return {"massege": "Hello endpoint"}


@video_route.post("/video")
async def upload_file(
        background_tasks: BackgroundTasks,
        title: str = Form(...),
        desc: str = Form(...),
        user_id: int = Form(...),
        file: UploadFile = File(...)
) -> Video:
    if file.content_type == 'video/mp4':
        file_helper = FileHelper(file=file, user_id=user_id)
        background_tasks.add_task(file_helper.write_file)
    else:
        raise HTTPException(status_code=418, detail="file format must be mp4")
    user = await User.objects.get(pk=user_id)
    serialized_video = UploadVideoSchema(title=title, description=desc, user=user, file=file.filename).dict()
    service = VideoService()
    return await service.create_video(**serialized_video)


@video_route.get('/video/{video_id}', response_model=Video)
async def get_video(request: Request, video_id: int) -> StreamingResponse:
    file_helper = FileHelper()
    video, status_code, content_length, headers = file_helper.open_file(request=request, video_id=video_id)
    response = StreamingResponse(video, media_type="video/mp4", status_code=status_code)
    response.headers.update({
        'Accept-Ranges': 'bytes',
        'Content-Length': str(content_length),
        **headers,
    })
    return response


@video_route.get('/video')
async def get_videos() -> Video:
    return await Video.objects.select_related("user").all()
