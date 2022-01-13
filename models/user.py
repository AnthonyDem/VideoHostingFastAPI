import ormar
from db import database, metadata


class User(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True, autoincrement=True)
    first_name: str = ormar.String(max_length=250)
    last_name: str = ormar.String(max_length=250, nullable=True)
    country: str = ormar.String(max_length=250, nullable=True)
    email: str = ormar.String(max_length=250, nullable=True)
    phone: str = ormar.String(max_length=250, nullable=True)