import json

from app.llm.service import LLMService

from app.models.claim import Claim
from app.models.document import Document


llm = LLMService()


class Extractor:

    def extract_claims(
        self,
        document: Document
    ) -> list[Claim]:

        prompt = f"""
You are an evidence extraction system.

Extract the most important factual claims.

Return ONLY JSON.

Format:

[
  {{
    "claim": "...",
    "evidence": "..."
  }}
]

Document:

{document.content[:2000]}
"""

        try:

            content = llm.generate(prompt)

            data = json.loads(content)

            claims = []

            for item in data:

                claims.append(
                    Claim(
                        claim=item["claim"],
                        evidence=item["evidence"],
                        source_url=document.url,
                        source_title=document.title
                    )
                )

            return claims

        except Exception as e:

            print("Extractor Error:", e)

            return []