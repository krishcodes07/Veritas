import requests

from app.models.document import Document
from app.models.source import Source

from app.utils.html_cleaner import clean_html
from app.utils.page_detector import is_blocked_page

from app.config.research import (
    MAX_DOCUMENT_CHARS,
    MIN_DOCUMENT_LENGTH
)


class Reader:

    def read(self, source: Source):

        try:

            response = requests.get(
                source.url,
                timeout=20,
                headers={
                    "User-Agent": (
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                    )
                }
            )

            text = clean_html(response.text)

            if is_blocked_page(text):

                return Document(
                    url=source.url,
                    title=source.title,
                    content="",
                    content_length=0,
                    status="blocked"
                )

            if len(text) < MIN_DOCUMENT_LENGTH:

                return Document(
                    url=source.url,
                    title=source.title,
                    content="",
                    content_length=0,
                    status="too_short"
                )

            return Document(
                url=source.url,
                title=source.title,
                content=text[:MAX_DOCUMENT_CHARS],
                content_length=len(text),
                status="success"
            )

        except Exception as e:

            return Document(
                url=source.url,
                title=source.title,
                content="",
                content_length=0,
                status=f"error: {str(e)}"
            )