import databases
import sqlalchemy
from fastapi import FastAPI

app = FastAPI()

TEST_DB_URL = "sqlite:///test.db"
database = databases.Database(TEST_DB_URL, force_rollback=True)
engine = sqlalchemy.create_engine(TEST_DB_URL)
metadata = sqlalchemy.MetaData()
metadata.create_all(engine)
app.state.database = database


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()
