import json

from app.chunking.chunk_service import ChunkService
from app.chunking.text_cleaner import TextCleaner
from app.core.config import settings
from app.ingestion.loaders.loader_factory import LoaderFactory


class IngestionService:

    REGISTRY_FILE = "data/registry.json"

    @staticmethod
    def parse_document(document_id: str):

        with open(
            IngestionService.REGISTRY_FILE,
            "r"
        ) as file:

            registry = json.load(file)

        if document_id not in registry:
            raise Exception(
                f"Document {document_id} not found"
            )

        document_info = registry[
            document_id
        ]

        file_path = document_info[
            "path"
        ]

        loader = LoaderFactory.get_loader(
            file_path
        )

        # Extract raw text
        content = loader.load(
            file_path
        )

        # Clean extracted text
        content = TextCleaner.clean(
            content
        )

        # Generate chunks
        chunks = ChunkService.chunk_document(
            document_id=document_id,
            text=content,
            chunk_size=settings.CHUNK_SIZE,
            overlap=settings.CHUNK_OVERLAP
        )

        return {
            "document_id": document_id,
            "filename": document_info[
                "filename"
            ],
            "content": content,
            "chunk_count": len(
                chunks
            ),
            "chunks": chunks
        }