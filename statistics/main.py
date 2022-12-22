from fastapi import FastAPI

from statistics.models import Stats
from statistics.registry import DynamoDBRegistry

app = FastAPI()


@app.get("/{user_id}/pages/", response_model=Stats, response_model_include={"user_id", "pages"})
async def get_pages(user_id: int):
    pages_count = await DynamoDBRegistry.get_table_data(user_id, 'pages')
    return {"user_id": user_id, "pages": pages_count}


@app.get("/{user_id}/posts/", response_model=Stats, response_model_include={"user_id", "posts"})
async def get_posts(user_id: int):
    posts_count = await DynamoDBRegistry.get_table_data(user_id, 'posts')
    return {"user_id": user_id, "posts": posts_count}


@app.get("/{user_id}/likes/", response_model=Stats, response_model_include={"user_id", "likes"})
async def get_likes(user_id: int):
    likes_count = await DynamoDBRegistry.get_table_data(user_id, 'likes')
    return {"user_id": user_id, "likes": likes_count}


@app.get("/{user_id}/followers/", response_model=Stats, response_model_include={"user_id", "followers"})
async def get_followers(user_id: int):
    followers_count = await DynamoDBRegistry.get_table_data(user_id, 'followers')
    return {"user_id": user_id, "followers": followers_count}


@app.get("/{user_id}/follow_requests/", response_model=Stats, response_model_include={"user_id", "follow_requests"})
async def get_follow_requests(user_id: int):
    follow_requests_count = await DynamoDBRegistry.get_table_data(user_id, 'follow_requests')
    return {"user_id": user_id, "follow_requests": follow_requests_count}
