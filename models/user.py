import ormar
from db import database, metadata
from fastapi_users.db import OrmarBaseUserModel, OrmarUserDatabase

from schemas.user_schemas import UserSchema


class User(OrmarBaseUserModel):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True, autoincrement=True)
    first_name: str = ormar.String(max_length=250)
    last_name: str = ormar.String(max_length=250, nullable=True)
    country: str = ormar.String(max_length=250, nullable=True)
    email: str = ormar.String(max_length=250, nullable=True)
    phone: str = ormar.String(max_length=250, nullable=True)


user_db = OrmarUserDatabase(UserSchema, User)