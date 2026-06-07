from pydantic import BaseModel

from app.models.source import Source


class SearchResult(BaseModel):
    query: str
    sources: list[Source]