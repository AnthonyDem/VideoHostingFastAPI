from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from models.user import user_db
from schemas.user_schemas import UserSchema, UserCreateSchema, UserUpdateSchema, UserDBSchema
from auth import jwt_authentication, auth_backends


user_router = APIRouter()


fastapi_users = FastAPIUsers(
    user_db,
    auth_backends,
    UserSchema,
    UserCreateSchema,
    UserUpdateSchema,
    UserDBSchema
)

user_router.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix='/auth/jwt', tags=['auth']
)

user_router.include_router(
    fastapi_users.get_users_router(), prefix='/users', tags=['auth']
)