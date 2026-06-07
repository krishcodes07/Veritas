from app.core.planner import Planner


class ResearchService:

    def __init__(self):
        self.planner = Planner()

    def run(self, query: str):

        plan = self.planner.generate_plan(query)

        return {
            "status": "success",
            "plan": plan.model_dump()
        }