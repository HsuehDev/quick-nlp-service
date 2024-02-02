from typing import List, Optional
from app.nlp_service.strategies.strategy import NLPInterface
from app.component.chat import Params, Response

import os

from transformers import AutoTokenizer
import transformers
import torch

class LLaMa2Strategy(NLPInterface):
    def __init__(self) -> None:
        self.model_endpoint:str = "Extrabass/llama-2-7b-chat-hf-plant-qa"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_endpoint)
        
        self.pipeline = transformers.pipeline(
            "text-generation",
            model=self.model_endpoint,
            torch_dtype=torch.float32,
            device_map="auto",
        )


    def process_text(self, params: Params) -> Response:            
        ### 利用 pipeline 調用模型       
        sequences = self.pipeline(
            f"[INST]Question:hello[/INST]",
            do_sample=True,
            top_k=10,
            num_return_sequences=1,
            eos_token_id=self. tokenizer.eos_token_id,
            max_length=512
        )
        
        print('response:')
        print(''.join(seq['generated_text'] for seq in sequences))
        return Response(
            purpose = '',
            input_messages = params.roles,
            response ={''.join(seq['generated_text'] for seq in sequences)}
        )
        # pass