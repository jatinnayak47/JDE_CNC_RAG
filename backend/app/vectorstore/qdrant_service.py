from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

from app.core.config import settings


class QdrantService:

    _client = None

    @classmethod
    def get_client(cls):
        """
        Returns singleton Qdrant client.
        """

        if cls._client is None:

            cls._client = QdrantClient(
                host=settings.QDRANT_HOST,
                port=settings.QDRANT_PORT
            )

        return cls._client

    @classmethod
    def create_collection(
        cls,
        vector_size: int
    ):
        """
        Creates collection if it does not already exist.
        """

        client = cls.get_client()

        collections = client.get_collections()

        existing_collections = [
            collection.name
            for collection in collections.collections
        ]

        if settings.COLLECTION_NAME in existing_collections:

            print(
                f"Collection '{settings.COLLECTION_NAME}' already exists."
            )

            return

        client.create_collection(
            collection_name=settings.COLLECTION_NAME,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            )
        )

        print(
            f"Collection '{settings.COLLECTION_NAME}' created successfully."
        )

    @classmethod
    def insert_chunks(
        cls,
        chunks: list
    ):
        """
        Inserts chunks into Qdrant.
        """

        client = cls.get_client()

        points = []

        for chunk in chunks:

            point = PointStruct(
                id=chunk["chunk_id"],
                vector=chunk["embedding"],
                payload={
                    "chunk_id": chunk["chunk_id"],
                    "document_id": chunk["document_id"],
                    "chunk_index": chunk["chunk_index"],
                    "text": chunk["text"]
                }
            )

            points.append(point)

        client.upsert(
            collection_name=settings.COLLECTION_NAME,
            points=points
        )

        print(
            f"{len(points)} chunks inserted successfully."
        )

    @classmethod
    def search(
        cls,
        query_embedding: list,
        top_k: int = 5
    ):
        """
        Performs semantic vector search.
        Compatible with qdrant-client 1.18.0
        """

        if top_k < 1:
            top_k = 1

        if top_k > 20:
            top_k = 20

        client = cls.get_client()

        # Debug: verify collection contains data
        count = client.count(
            collection_name=settings.COLLECTION_NAME
        )

        print(
            f"Total vectors in collection: {count.count}"
        )

        results = client.query_points(
            collection_name=settings.COLLECTION_NAME,
            query=query_embedding,
            limit=top_k
        )

        return results.points

    @classmethod
    def count_points(cls):
        """
        Returns total vectors stored.
        """

        client = cls.get_client()

        result = client.count(
            collection_name=settings.COLLECTION_NAME
        )

        return result.count

    @classmethod
    def get_collection_info(cls):
        """
        Returns collection metadata.
        """

        client = cls.get_client()

        return client.get_collection(
            settings.COLLECTION_NAME
        )