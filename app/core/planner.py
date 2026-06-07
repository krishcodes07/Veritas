class Planner:
    def generate_plan(self, query: str) -> dict:
        return {
            "main_question": query,
            "search_queries": [
                query
            ]
        }