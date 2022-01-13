import ormar
import datetime

from typing import Optional, List
from db import metadata, database
from models.user import User


class Video(ormar.Model):
    class Meta:
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True, autoincrement=True)
    user: Optional[User] = ormar.ForeignKey(User)
    title: str = ormar.String(max_length=250)
    description: str = ormar.Text(nullable=True)
    file: str = ormar.String(max_length=1000)
    created_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    likes_count: int = ormar.Integer(default=0)
    views_count: int = ormar.Integer(default=0)
    tags: List[str] = ormar.JSON(default=dict)
