from pydantic import BaseModel


class Stats(BaseModel):
    user_id: int
    pages: int = 0
    posts: int = 0
    likes: int = 0
    followers: int = 0
    follow_requests: int = 0
