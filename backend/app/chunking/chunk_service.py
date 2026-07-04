import uuid

from llama_index.core.node_parser import (
    SentenceSplitter,
)

from app.schemas.chunk import Chunk


class ChunkService:

    @staticmethod
    def chunk_document(
        document_id: str,
        text: str,
        chunk_size: int,
        overlap: int
    ):

        splitter = SentenceSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap
        )

        text_chunks = splitter.split_text(
            text
        )

        chunks = []

        for idx, chunk_text in enumerate(
            text_chunks
        ):

            chunk = Chunk(
                chunk_id=str(
                    uuid.uuid4()
                ),
                document_id=document_id,
                chunk_index=idx,
                text=chunk_text,
                metadata={
                    "document_id": document_id,
                    "chunk_index": idx,
                    "source": document_id
                }
            )

            chunks.append(
                chunk.model_dump()
            )

        return chunks