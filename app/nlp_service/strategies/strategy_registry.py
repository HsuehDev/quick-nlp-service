from app.nlp_service.strategies.strategy import NLPInterface
from app.nlp_service.strategies.openai_strategy import OpenAIStrategy
from app.nlp_service.strategies.llama2_stragegy import LLaMa2Strategy

nlp_strategies = {
    # "huggingface": self.huggingface_nlp_service,
    "gpt-35-turbo": OpenAIStrategy(),
    "gpt-35-turbo-16k": OpenAIStrategy(),
    "gpt-35-turbo-instruct": OpenAIStrategy(),
    "gpt-4": OpenAIStrategy(),
    "gpt-4-32k": OpenAIStrategy(),
}
