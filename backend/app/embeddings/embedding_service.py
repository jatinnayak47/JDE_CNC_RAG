from sentence_transformers import SentenceTransformer

from app.core.config import settings


class EmbeddingService:

    _model = None

    @classmethod
    def get_model(cls):

        print("\n===== EMBEDDING MODEL =====")

        if cls._model is None:

            print(
                f"Loading model: "
                f"{settings.EMBEDDING_MODEL}"
            )

            cls._model = SentenceTransformer(
                settings.EMBEDDING_MODEL
            )

            print(
                "Model loaded successfully."
            )

        else:

            print(
                "Using cached model."
            )

        print("===========================\n")

        return cls._model

    @classmethod
    def generate_embedding(
        cls,
        text: str
    ):

        print(
            f"Generating embedding "
            f"for text length {len(text)}"
        )

        model = cls.get_model()

        embedding = model.encode(
            text,
            normalize_embeddings=True
        )

        print(
            "Single embedding generated."
        )

        return embedding.tolist()

    @classmethod
    def generate_embeddings(
        cls,
        texts: list[str]
    ):

        print(
            f"\nGenerating embeddings "
            f"for {len(texts)} chunks"
        )

        model = cls.get_model()

        print(
            "Starting model.encode()..."
        )

        embeddings = model.encode(
            texts,
            batch_size=64,
            show_progress_bar=True,
            normalize_embeddings=True
        )

        print(
            f"Generated {len(embeddings)} embeddings"
        )

        return embeddings.tolist()