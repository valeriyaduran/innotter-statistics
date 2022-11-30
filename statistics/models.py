from pydantic import BaseModel


class Stats(BaseModel):
    id: str
    user_id: str
    name: str
    likes: int = 0
    followers: int = 0
    follow_requests: int = 0

