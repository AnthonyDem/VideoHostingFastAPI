from models.video import Video
from schemas.video_schemas import UploadVideoSchema


class VideoService(object):

    async def create_video(self, video_object: dict) -> Video:
        return Video.objects.create(**video_object)

    async def get_video(self, video_id: int) -> Video:
        return Video.objects.get(pk=video_id)