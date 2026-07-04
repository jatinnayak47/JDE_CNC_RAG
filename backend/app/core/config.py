from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):

    # --------------------------------
    # Application
    # --------------------------------
    APP_NAME: str = "JDE-RAG"
    API_PREFIX: str = "/api/v1"

    # --------------------------------
    # Storage
    # --------------------------------
    UPLOAD_DIR: str = "data/uploads"

    # --------------------------------
    # Chunking
    # --------------------------------
    CHUNK_SIZE: int = 512
    CHUNK_OVERLAP: int = 100

    # --------------------------------
    # Embeddings
    # --------------------------------
    EMBEDDING_MODEL: str = (
        "BAAI/bge-base-en-v1.5"
    )

    # --------------------------------
    # Qdrant
    # --------------------------------
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333

    COLLECTION_NAME: str = (
        "jde_documents"
    )

    # --------------------------------
    # LLM Provider
    # --------------------------------
    LLM_PROVIDER: str = "local"

    # --------------------------------
    # Ollama
    # --------------------------------
    OLLAMA_BASE_URL: str = (
        "http://localhost:11434"
    )

    OLLAMA_MODEL: str = "qwen3:8b"

    # --------------------------------
    # OpenAI
    # --------------------------------
    OPENAI_API_KEY: str = ""

    OPENAI_MODEL: str = "gpt-4o-mini"

    # --------------------------------
    # Gemini
    # --------------------------------
    GEMINI_API_KEY: str = ""

    GEMINI_MODEL: str = (
        "gemini-2.5-flash"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()