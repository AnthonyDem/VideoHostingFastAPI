from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    first_name: str
    last_name: str = None
    country: str = None
    email: str = None
    phone: int = None
