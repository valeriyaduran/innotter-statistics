from fastapi import HTTPException

from statistics.db import get_table


async def check_user_id(user_id):
    table = await get_table()
    try:
        table.get_item(
            Key={
                "user_id": user_id
            }, )['Item']['user_id']
    except KeyError:
        raise HTTPException(status_code=404, detail="Item not found")


async def check_data_by_field_exists(user_id, field):
    table = await get_table()
    try:
        table.get_item(
            Key={
                "user_id": user_id
            }, )['Item'][field]
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Data for {field} not found")