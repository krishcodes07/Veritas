import requests
from bs4 import BeautifulSoup

from app.models.document import Document
from app.models.source import Source

from app.config.research import MAX_DOCUMENT_CHARS

class Reader:

    def read(self, source: Source) -> Document:

        try:

            response = requests.get(
                source.url,
                timeout=20,
                headers={
                    "User-Agent": "Veritas Research Bot"
                }
            )

            soup = BeautifulSoup(
                response.text,
                "lxml"
            )

            text = soup.get_text(
                separator=" ",
                strip=True
            )

            return Document(
                url=source.url,
                title=source.title,
                content=text[:MAX_DOCUMENT_CHARS]
            )

        except Exception as e:

            return Document(
                url=source.url,
                title=source.title,
                content=f"ERROR: {str(e)}"
            )