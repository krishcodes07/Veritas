import requests

from app.config.settings import SERPER_API_KEY
from app.config.research import MAX_RESULTS_PER_QUERY
from app.models.source import Source


class SearchEngine:

    URL = "https://google.serper.dev/search"

    def search(self, query: str, limit: int = MAX_RESULTS_PER_QUERY):

        payload = {
            "q": query
        }

        headers = {
            "X-API-KEY": SERPER_API_KEY,
            "Content-Type": "application/json"
        }

        response = requests.post(
            self.URL,
            headers=headers,
            json=payload,
            timeout=30
        )

        data = response.json()

        results = []

        for item in data.get("organic", [])[:limit]:

            results.append(
                Source(
                    title=item.get("title", ""),
                    url=item.get("link", ""),
                    snippet=item.get("snippet", "")
                )
            )

        return results