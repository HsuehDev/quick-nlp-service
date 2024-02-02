from app.component.chat import Response, RoleItem
from typing import List
import pymongo
import json
import os

# def save_response_data(purpose, messages, json_data):
def save_response_data(response: Response) -> None:
    MONGODB_HOST:str = os.environ.get('MONGODB_HOST')
    MONGODB_DATABASE:str = os.environ.get('MONGODB_DATABASE')
    MONGODB_COLLECTION:str = os.environ.get('MONGODB_COLLECTION')
    
    purpose: str = response.purpose
    messages: List[RoleItem] = response.input_messages
    json_data: dict = response.response

    mongo_client = pymongo.MongoClient(MONGODB_HOST)

    db = mongo_client[MONGODB_DATABASE]
    collection = db[MONGODB_COLLECTION] 

    response_data = {
        "id": json_data.get("id"),
        "object": json_data.get("object"),
        "created": json_data.get("created"),
        "model": json_data.get("model"),
        "purpose": purpose,
        "prompt": json.dumps([item.dict() for item in messages], indent=2),
        "choices": json_data.get("choices"),
        "usage": json_data.get("usage"),
    }

    # 將 JSON 數據插入到集合中
    insert_result = collection.insert_one(response_data)

    # 關閉 MongoDB 連接
    mongo_client.close()
