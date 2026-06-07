from pydantic import BaseModel


class Document(BaseModel):
    url: str
    title: str
    content: str