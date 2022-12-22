from fastapi import HTTPException

from statistics.db import get_table


async def check_user_id(user_id):
    table = await get_table()
    try:
        await table.get_item(
            Key={
                "user_id": user_id
            }, )['Item']['user_id']
    except KeyError:
        raise HTTPException(status_code=404, detail="Item not found")
