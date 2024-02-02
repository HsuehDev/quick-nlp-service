from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.nlp_service.routes import router as nlp

app = FastAPI(title = 'Wulab Openai 服務平台',description = '透過 api 快速調用 openai 服務')
api_router = APIRouter()   

api_router.include_router(nlp) 

app.include_router(api_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)