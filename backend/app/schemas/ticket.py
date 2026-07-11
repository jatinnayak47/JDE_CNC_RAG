from pydantic import BaseModel
from typing import Optional


class Ticket(BaseModel):
    ticket_id: str

    ticket_type: str = ""
    priority: str = ""
    state: str = ""
    assignment_group: str = ""
    short_description: str = ""
    region: str = ""
    location: str = ""
    assignee: str = ""

    embedding: Optional[list[float]] = None