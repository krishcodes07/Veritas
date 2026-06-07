from app.core.planner import Planner
from app.core.search import SearchEngine
from app.core.reader import Reader
from app.core.extractor import Extractor

from app.models.search_result import SearchResult

from app.config.research import MAX_DOCUMENTS_TO_READ


class ResearchService:

    def __init__(self):
        self.planner = Planner()
        self.search_engine = SearchEngine()
        self.reader = Reader()
        self.extractor = Extractor()

    def run(self, query: str):

        # Step 1: Generate Research Plan
        plan = self.planner.generate_plan(query)

        search_results = []
        total_results = 0
        all_sources = []

        # Step 2: Search All Queries
        for search_query in plan.search_queries:

            print(f"\nSearching: {search_query}")

            results = self.search_engine.search(search_query)

            print(f"Found {len(results)} results")

            total_results += len(results)

            all_sources.extend(results)

            search_results.append(
                SearchResult(
                    query=search_query,
                    sources=results
                )
            )

        # Step 3: Remove Duplicate URLs
        seen = set()
        unique_sources = []

        for source in all_sources:

            if source.url not in seen:
                seen.add(source.url)
                unique_sources.append(source)

        # Step 4: Read Top Sources
        documents = []

        blocked_documents = 0
        too_short_documents = 0
        error_documents = 0

        print(
            f"\nReading top {min(len(unique_sources), MAX_DOCUMENTS_TO_READ)} sources..."
        )

        for source in unique_sources[:MAX_DOCUMENTS_TO_READ]:

            print(f"Reading: {source.url}")

            document = self.reader.read(source)

            if document.status == "blocked":
                blocked_documents += 1
                continue

            if document.status == "too_short":
                too_short_documents += 1
                continue

            if document.status.startswith("error"):
                error_documents += 1
                continue

            documents.append(document)

        # Step 5: Extract Claims
        claims = []

        print(
            f"\nExtracting claims from {len(documents)} documents..."
        )

        for document in documents:

            extracted_claims = self.extractor.extract_claims(
                document
            )

            print(
                f"Extracted {len(extracted_claims)} claims from: "
                f"{document.title}"
            )

            claims.extend(extracted_claims)

        # Step 6: Metrics
        metrics = {
            "total_queries": len(plan.search_queries),
            "total_results": total_results,
            "unique_results": len(unique_sources),

            "documents_attempted": min(
                len(unique_sources),
                MAX_DOCUMENTS_TO_READ
            ),

            "successful_documents": len(documents),
            "blocked_documents": blocked_documents,
            "too_short_documents": too_short_documents,
            "error_documents": error_documents,

            "claims_extracted": len(claims)
        }

        # Step 7: Response
        return {
            "status": "success",

            "metrics": metrics,

            "plan": plan.model_dump(),

            "search_results": [
                result.model_dump()
                for result in search_results
            ],

            "sources": [
                source.model_dump()
                for source in unique_sources
            ],

            "documents": [
                document.model_dump()
                for document in documents
            ],

            "claims": [
                claim.model_dump()
                for claim in claims
            ]
        }