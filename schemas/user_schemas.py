from pydantic import BaseModel
from fastapi_users import models


class UserSchema(models.BaseModel):
    id: int
    first_name: str
    last_name: str = None
    country: str = None
    email: str = None
    phone: int = None


class UserCreateSchema(UserSchema, models.BaseUserCreate):
    pass


class UserUpdateSchema(UserSchema, models.BaseUserUpdate):
    pass


class UserDBSchema(UserSchema, models.BaseUserDB):
    pass

