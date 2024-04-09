from app.nlp_service.strategies.strategy import NLPInterface
from app.nlp_service.strategies.openai_strategy import OpenAIStrategy
# from app.nlp_service.strategies.llama2_strategy import LLaMa2Strategy
from app.nlp_service.strategies.tgi_strategy import TGIStrategy
from app.nlp_service.strategies.taiwan_tgi_strategy import TaiwanTGIStrategy

nlp_strategies = {
    # "huggingface": self.huggingface_nlp_service,
    "gpt-35-turbo": OpenAIStrategy(),
    "gpt-35-turbo-16k": OpenAIStrategy(),
    "gpt-35-turbo-instruct": OpenAIStrategy(),
    "gpt-4": OpenAIStrategy(),
    "gpt-4-32k": OpenAIStrategy(),
    
    'wulab': TGIStrategy(),
    'taiwan-llama' : TaiwanTGIStrategy()
    # "llama-2": LLaMa2Strategy(),
}
