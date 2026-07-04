from ollama import Client

from app.core.config import settings
from app.llm.base import BaseLLM


class OllamaProvider(BaseLLM):

    def __init__(self):

        self.client = Client(
            host=settings.OLLAMA_BASE_URL
        )

    def generate(
        self,
        prompt: str
    ):

        response = self.client.generate(
            model=settings.OLLAMA_MODEL,
            prompt=prompt,
            options={
                "temperature": 0.1,
                "num_predict": 512
            }
        )

        return response["response"]