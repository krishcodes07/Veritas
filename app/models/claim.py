from pydantic import BaseModel


class Claim(BaseModel):
    claim: str
    evidence: str

    source_url: str
    source_title: str