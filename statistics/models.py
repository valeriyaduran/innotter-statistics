from pydantic import BaseModel


class Stats(BaseModel):
    id: int
    user_id: str
    posts: int = 0
    likes: int = 0
    followers: int = 0
    follow_requests: int = 0

