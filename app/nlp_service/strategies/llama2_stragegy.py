from typing import List, Optional
from app.nlp_service.strategies.strategy import NLPInterface
from app.component.chat import Params, Response

import os

class LLaMa2Strategy(NLPInterface):
    def process_text(self, params: Params) -> Response:    
        
        # insert_data_to_mongodb("huggingface", "text", "result")
        pass