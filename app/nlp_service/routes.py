from fastapi import APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict

import os
import openai

from app.database.mongodb import save_response_data

from app.component.chat import RoleItem, Params, Response
from app.nlp_service.strategies.strategy import NLPInterface
from app.nlp_service.strategies.strategy_registry import nlp_strategies

router = APIRouter()

@router.post("/callapi/")
async def process_text(params: Params):
    
    nlp_service: NLPInterface = nlp_strategies.get(params.engine)
    
    # return params, model_category
    if nlp_service:
        result:Response = nlp_service.process_text(params)
        
        # print(f"result: ${result}")
        # 將結果插入到 MongoDB
        save_response_data(result)
        
        return result.response
    else:
        return {"error": "Unsupported model category."}
