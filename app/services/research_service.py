from app.core.planner import Planner
from app.core.search import SearchEngine

from app.models.search_result import SearchResult


class ResearchService:

    def __init__(self):
        self.planner = Planner()
        self.search_engine = SearchEngine()

    def run(self, query: str):

        plan = self.planner.generate_plan(query)

        search_results = []

        total_results = 0

        all_sources = []

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

        # Deduplicate
        seen = set()
        unique_sources = []

        for source in all_sources:

            if source.url not in seen:
                seen.add(source.url)
                unique_sources.append(source)

        metrics = {
            "total_queries": len(plan.search_queries),
            "total_results": total_results,
            "unique_results": len(unique_sources)
        }

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
            ]
        }