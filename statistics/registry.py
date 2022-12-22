from fastapi import HTTPException

from statistics.db import get_table
from statistics.handlers import check_user_id


class DynamoDBRegistry:
    to_increase_counter = {
        "post_added": "posts",
        "page_added": "pages",
        "like_added": "likes",
        "follow_request_added": "follow_requests",
        "follower_added": "followers"
    }
    to_decrease_counter = {
        "post_deleted": "posts",
        "like_removed": "likes",
        "follow_request_removed": "follow_requests"
    }

    @staticmethod
    async def get_table_data(user_id, field):
        await check_user_id(user_id)
        table = await get_table()
        item = table.get_item(
            Key={
                "user_id": user_id
            }
        )
        return item['Item'][field]

    @classmethod
    async def update_table_data(cls, response):
        table = await get_table()
        if response["action"] in cls.to_increase_counter:
            table.update_item(
                Key={
                    "user_id": response["user_id"]
                },
                UpdateExpression=f"ADD {cls.to_increase_counter[response['action']]} :num",
                ExpressionAttributeValues={
                    ":num": 1
                }
            )
        elif response["action"] in cls.to_decrease_counter:
            table.update_item(
                Key={
                    "user_id": response["user_id"]
                },
                UpdateExpression=f"ADD {cls.to_decrease_counter[response['action']]} :num",
                ExpressionAttributeValues={
                    ":num": -1
                },
            )

