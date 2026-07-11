from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

from app.core.config import settings


class TicketQdrantService:

    @staticmethod
    def get_client():

        return QdrantClient(
            host=settings.QDRANT_HOST,
            port=settings.QDRANT_PORT
        )

    @staticmethod
    def create_collection():

        client = TicketQdrantService.get_client()

        collections = client.get_collections()

        existing = [
            c.name
            for c in collections.collections
        ]

        if settings.TICKET_COLLECTION_NAME in existing:
            print(
                f"{settings.TICKET_COLLECTION_NAME} already exists"
            )
            return

        client.create_collection(
            collection_name=settings.TICKET_COLLECTION_NAME,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )

        print(
            f"{settings.TICKET_COLLECTION_NAME} created"
        )

    @staticmethod
    def insert_points(points):

        client = TicketQdrantService.get_client()

        qdrant_points = []

        for point in points:

            qdrant_points.append(
                PointStruct(
                    id=point["id"],
                    vector=point["vector"],
                    payload=point["payload"]
                )
            )

        client.upsert(
            collection_name=settings.TICKET_COLLECTION_NAME,
            points=qdrant_points
        )

    @staticmethod
    def search(
        query_embedding,
        top_k=5
    ):

        client = TicketQdrantService.get_client()

        results = client.query_points(
            collection_name=settings.TICKET_COLLECTION_NAME,
            query=query_embedding,
            limit=top_k
        )

        return results.points