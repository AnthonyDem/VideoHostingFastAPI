from pydantic import BaseModel
from typing import List


class UserSchema(BaseModel):
    id: int
    first_name: str
    last_name: str = None
    country: str = None
    email: str = None
    phone: int = None


class UploadVideoSchema(BaseModel):
    title: str
    description: str
    tags: List[str] = None


class GetVideoSchema(BaseModel):
    video: UploadVideoSchema
    user: UserSchema
