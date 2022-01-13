import datetime

from pydantic import BaseModel
from typing import List
from schemas.user_schemas import UserSchema


class UploadVideoSchema(BaseModel):
    title: str
    description: str
    user: UserSchema
    file: str
    created_at: datetime.datetime
    likes_count: int
    views_count: int
    tags: List[str] = None


class GetVideoSchema(BaseModel):
    video: UploadVideoSchema
    user: UserSchema
