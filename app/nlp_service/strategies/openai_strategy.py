from app.nlp_service.strategies.strategy import NLPInterface

from typing import List, Optional
from app.component.chat import Params, Response
import os
import openai

class OpenAIStrategy(NLPInterface):
    def process_text(self, params: Params) -> Response: 
        openai.api_type = os.environ.get('OPENAI_API_TYPE')
        openai.api_base = os.environ.get('OPENAI_API_ENDPOINT')
        openai.api_key = os.environ.get('OPENAI_API_KEY')
        
        messages = [{"role": row.role, "content": row.content} for row in params.roles[-params.past_messages:]]
        
        stop_list = params.stop.split('-') if params.stop else None

        response = openai.ChatCompletion.create(
            engine=params.engine,
            messages=messages,
            temperature=params.temperature,
            max_tokens=params.max_tokens,
            top_p=params.top_p,
            frequency_penalty=params.frequency_penalty,
            presence_penalty=params.presence_penalty,
            stop=stop_list)
        
        return Response(
            purpose = params.purpose,
            input_messages = messages,
            response = response
        )
