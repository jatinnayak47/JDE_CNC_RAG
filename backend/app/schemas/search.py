from pydantic import BaseModel


class SearchRequest(BaseModel):
    """
    Request model for semantic search.
    """

    query: str
    top_k: int = 5