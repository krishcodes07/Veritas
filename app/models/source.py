from pydantic import BaseModel


class Source(BaseModel):
    title: str
    url: str
    snippet: str

    source_category: str = "unknown"
    source_score: int = 0