import datetime

from pydantic import BaseModel
from typing import List
from schemas.user_schemas import UserSchema


class UploadVideoSchema(BaseModel):
    title: str
    description: str = None
    user: UserSchema
    file: str
    created_at: datetime.datetime = None
    likes_count: int = None
    views_count: int = None
    tags: List[str] = None


class GetVideoSchema(BaseModel):
    video: UploadVideoSchema
    user: UserSchema
