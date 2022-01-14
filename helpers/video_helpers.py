import shutil
from pathlib import Path
from typing import Optional, Generator
from uuid import uuid4

import ormar.exceptions
from fastapi import UploadFile, File, HTTPException
from starlette.requests import Request
from typing.io import IO

from services.video_service import VideoService


class FileHelper(object):
    def __init__(self, user_id: int, file: UploadFile = File(...)):
        self.file = file
        self.user_id = user_id
        self.video_service = VideoService()

    def write_file(self) -> None:
        filepath = f'media/{self.user_id}/{uuid4()}_{self.file.filename}'
        with open(filepath, 'wb') as file_obj:
            shutil.copyfileobj(self.file.file, file_obj)

    def ranged(
            self,
            file: IO[bytes],
            start: int = 0,
            end: int = None,
            block_size: int = 8192,
    ) -> Generator[bytes, None, None]:
        consumed = 0

        file.seek(start)
        while True:
            data_length = min(block_size, end - start - consumed) if end else block_size
            if data_length <= 0:
                break
            data = file.read(data_length)
            if not data:
                break
            consumed += data_length
            yield data

        if hasattr(file, 'close'):
            file.close()

    def open_file(self, request: Request, video_id: int) -> Optional[tuple, HTTPException]:
        try:
            video = await self.video_service.get_video(video_id)
        except ormar.exceptions.NoMatch:
            return HTTPException(status_code=404, detail="don't match")
        path = Path(video.dict().get("file"))
        video = path.open("rb")
        video_size = path.stat().st_size

        content_length = video_size
        status_code = 200
        headers = {}
        content_range = request.headers.get("range")

        if content_range:
            content_range = content_range.strip().lower()
            content_ranges = content_range.split("=")[-1]
            range_start, range_end, *_ = map(str.strip, (content_ranges + "-").split("-"))
            range_start = max(0, int(range_start)) if range_start else 0
            range_end = min(video_size - 1, int(range_end)) if range_end else video_size - 1
            content_length = (range_end - range_start) + 1
            video = self.ranged(video, range_start, range_end, content_length)
            status_code = 206
            headers['Content-Range'] = f'bytes {range_start}-{range_end}/{video_size}'
        return video, status_code, content_length, headers