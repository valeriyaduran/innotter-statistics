from fastapi import FastAPI

from statistics.db import initialize_db
from statistics.models import Stats

app = FastAPI()
db = initialize_db()


@app.get("/pages/", response_model=Stats)
async def get_pages(stats: Stats):
    return stats.pages


@app.get("/posts/", response_model=Stats)
async def get_posts(stats: Stats):
    return stats.posts


@app.get("/likes/")
async def get_likes(stats: Stats):
    return stats.likes


@app.get("/followers/")
async def get_followers(stats: Stats):
    return stats.followers


@app.get("/follow_requests/")
async def get_follow_requests(stats: Stats):
    return stats.follow_requests