from fastapi import FastAPI
from api.video_api import video_route
from db import database, metadata, engine

app = FastAPI()

app.state.database = database
metadata.create_all(engine)
app.include_router(video_route)


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
