from app.nlp_service.strategies.strategy import NLPInterface
from app.component.chat import Params, Response
from app.component.formatter import Formatter

from typing import List, Optional
import requests
import json
import os

class TaiwanTGIStrategy(NLPInterface):
    def __init__(self) -> None:
        self.url: str = "http://140.115.126.210:9999/generate"
        
        self.header: dict = {
            'Content-Type': 'application/json'
        }
        
    def process_text(self, params: Params) -> Response: 
        input_string: str = Formatter().openai_to_llama(list(params.roles))       
        
        request_body: dict = {
            "inputs": input_string,
            "parameters": {
                "max_new_tokens": params.max_tokens,
            }
        }
        
        model_response = requests.post(
            url= self.url, 
            headers= self.header, 
            data = json.dumps(request_body)
        )
        
        generated_text = json.loads(model_response.text).get('generated_text', '')
        
        return Response(
            purpose = params.purpose,
            input_messages = params.roles,
            response = {
                "model": params.engine,
                "choices": [{
                    "message":{
                        "role": 'assistant',
                        "content": generated_text
                    }
                }]
                }
        )

