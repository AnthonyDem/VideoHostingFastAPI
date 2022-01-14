import datetime
import ormar
import pytest
import sqlalchemy

from test_db_utills import metadata, TEST_DB_URL
from models.user import User
from typing import Optional, List

from models.video import Video
from test_db_utills import database, metadata
from schemas.user_schemas import UserSchema
from schemas.video_schemas import UploadVideoSchema


@pytest.fixture(autouse=True, scope="module")
def create_test_database():
    engine = sqlalchemy.create_engine(TEST_DB_URL)
    metadata.create_all(engine)
    yield
    metadata.drop_all(engine)


@pytest.fixture(scope="module")
def create_user():
    return User.objects.create(first_name="Anthony", email="thony.dem@gmail.com")


@pytest.mark.asyncio
async def test_fields_is_not_required_if_nullable(create_user):
    class Video(ormar.Model):
        class Meta:
            tablename = "video"

        id: int = ormar.Integer(primary_key=True, autoincrement=True)
        user: Optional[User] = ormar.ForeignKey(User)
        title: str = ormar.String(max_length=250)
        description: str = ormar.Text(nullable=True)
        file: str = ormar.String(max_length=1000)
        created_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
        likes_count: int = ormar.Integer(default=0)
        views_count: int = ormar.Integer(default=0)
        tags: List[str] = ormar.JSON(default=dict)
    user = create_user()
    Video(user=user, file="test_file.mp4", title="test title")


@pytest.mark.asyncio
async def test_values_after_init(create_user):
    async with database:
        user = create_user()
        video1 = Video(user=user, file="test_file.mp4", title="test title")
        assert 'test' in video1.json()