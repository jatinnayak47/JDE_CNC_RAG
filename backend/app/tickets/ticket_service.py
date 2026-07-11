from app.tickets.ticket_loader import TicketLoader
from app.embeddings.embedding_service import EmbeddingService
from app.vectorstore.ticket_qdrant_service import (
    TicketQdrantService
)


class TicketService:

    @staticmethod
    def build_searchable_text(ticket):

        return f"""
Ticket Number: {ticket.get("Number", "")}

Priority: {ticket.get("Priority", "")}

State: {ticket.get("State", "")}

Assignment Group: {ticket.get("Assignment group", "")}

Assigned To: {ticket.get("Assigned to", "")}

Region: {ticket.get("Region", "")}

Location: {ticket.get("Location", "")}

Short Description:
{ticket.get("Short description", "")}

Additional Information:
{ticket.get("Additional Information", "")}
"""

    @staticmethod
    def ingest_excel(file_path):

        tickets = TicketLoader.load(file_path)

        points = []

        for idx, ticket in enumerate(tickets):

            searchable_text = (
                TicketService.build_searchable_text(
                    ticket
                )
            )

            embedding = (
                EmbeddingService.generate_embedding(
                    searchable_text
                )
            )

            points.append(
                {
                    "id": idx,
                    "vector": embedding,
                    "payload": {
                        **ticket,
                        "searchable_text": searchable_text
                    }
                }
            )

        TicketQdrantService.insert_points(
            points
        )

        return {
            "tickets_processed": len(points)
        }