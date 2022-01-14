from models.video import Video
from schemas.video_schemas import UploadVideoSchema


class VideoService(object):
    def __init__(self, video_object: dict):
        self.video_object = video_object

    async def create_video(self) -> Video:
        return Video.objects.create(**self.video_object)