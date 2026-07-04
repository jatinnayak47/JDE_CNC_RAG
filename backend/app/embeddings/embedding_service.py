from sentence_transformers import SentenceTransformer

from app.core.config import settings


class EmbeddingService:

    _model = None

    @classmethod
    def get_model(cls):

        if cls._model is None:

            cls._model = SentenceTransformer(
                settings.EMBEDDING_MODEL
            )

        return cls._model

    @classmethod
    def generate_embedding(
        cls,
        text: str
    ):

        model = cls.get_model()

        embedding = model.encode(
            text,
            normalize_embeddings=True
        )

        return embedding.tolist()

    @classmethod
    def generate_embeddings(
        cls,
        texts: list[str]
    ):

        model = cls.get_model()

        embeddings = model.encode(
            texts,
            batch_size=32,
            show_progress_bar=False,
            normalize_embeddings=True
        )

        return embeddings.tolist()