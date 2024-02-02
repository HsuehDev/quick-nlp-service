from typing import List, Optional
from app.nlp_service.strategies.strategy import NLPInterface
from app.component.chat import Params, Response, RoleItem
from app.component.formatter import Formatter

import os

from transformers import AutoTokenizer
import transformers
import torch

class LLaMa2Strategy(NLPInterface):
    def __init__(self) -> None:
        self.model_endpoint:str = "model/chinse-alpaca-2-7b"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_endpoint)
        
        self.pipeline = transformers.pipeline(
            "text-generation",
            model=self.model_endpoint,
            torch_dtype=torch.float32,
            device_map="auto",
        )

    def process_text(self, params: Params) -> Response:    
        prompt:str = Formatter().openai_to_llama(list(params.roles))
        
        ### 利用 pipeline 調用模型       
        sequences = self.pipeline(
            prompt,
            do_sample=True,
            top_k=params.top_k,
            num_return_sequences=1,
            eos_token_id=self. tokenizer.eos_token_id,
            max_length=params.max_tokens
        )
        
        response_text: str = ''.join(seq['generated_text'] for seq in sequences)
        
        result:List = [{"role": item.role, "content": item.content} for item in Formatter().llama_to_openai(response_text)]
            
        lastest_response_role: str = result[-1]["role"] if len(result) > 0 else ""
        lastest_response_content: str = result[-1]["content"] if len(result) > 0 else ""
        
        return Response(
            purpose = params.purpose,
            input_messages = params.roles,
            response = {
                "model": params.engine,
                "choices": [{
                    "message":{
                        "role": lastest_response_role,
                        "content": lastest_response_content
                    }
                }]
            }
        )
        # pass