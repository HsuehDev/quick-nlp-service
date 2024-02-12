from app.nlp_service.strategies.strategy import NLPInterface
from app.nlp_service.strategies.openai_strategy import OpenAIStrategy
from app.nlp_service.strategies.llama2_strategy import LLaMa2Strategy
from app.nlp_service.strategies.tgi_strategy import TGIStrategy

nlp_strategies = {
    # "huggingface": self.huggingface_nlp_service,
    "gpt-35-turbo": OpenAIStrategy(),
    "gpt-35-turbo-16k": OpenAIStrategy(),
    "gpt-35-turbo-instruct": OpenAIStrategy(),
    "gpt-4": OpenAIStrategy(),
    "gpt-4-32k": OpenAIStrategy(),
    
    'llama-2-7b': TGIStrategy(),
    # "llama-2": LLaMa2Strategy(),
}
