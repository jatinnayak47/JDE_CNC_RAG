from app.core.config import settings

from app.llm.ollama_provider import (
    OllamaProvider
)


class LLMFactory:

    @staticmethod
    def get_llm():

        provider = (
            settings.LLM_PROVIDER
            .lower()
        )

        if provider == "local":

            return OllamaProvider()

        raise ValueError(
            f"Unsupported provider: {provider}"
        )