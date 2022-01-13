from fastapi import FastAPI
from api.video_api import video_route

app = FastAPI()
app.include_router(video_route)