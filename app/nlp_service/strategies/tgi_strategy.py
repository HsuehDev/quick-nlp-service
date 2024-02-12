from app.nlp_service.strategies.strategy import NLPInterface
from app.component.chat import Params, Response
from app.component.formatter import Formatter

from typing import List, Optional
import requests
import json
import os

class TGIStrategy(NLPInterface):
    def __init__(self) -> None:
        self.url: str = os.environ.get('TGI_API_ENDPOINT')
        
        self.header: dict = {
            'Content-Type': 'application/json'
        }
        
    def process_text(self, params: Params) -> Response: 
        try:
            url: str = ""
            input_string: str = Formatter().openai_to_llama(list(params.roles))       
            
            request_body: dict = {
                "inputs": input_string,
                "parameters": {
                    "best_of": 1,
                    "decoder_input_details": True,
                    "details": True,
                    "do_sample": True,
                    "max_new_tokens": params.max_tokens,
                    "repetition_penalty": params.repetition_penalty,
                    "return_full_text": False,
                    "seed": None,
                    "stop": ["photographer"],
                    "temperature": params.temperature,
                    "top_k": params.top_k,
                    "top_n_tokens": 5,
                    "top_p": params.top_p,
                    "truncate": None,
                    "typical_p": 0.95,
                    "watermark": True
                }
            }
            
            model_response = requests.post(
                url= url, 
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
            
        except Exception as e:
            return e

