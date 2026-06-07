import json

from sympy import content

from app.llm.service import LLMService
from app.models.research import ResearchPlan

llm = LLMService()

class Planner:

    def generate_plan(self, query: str) -> ResearchPlan:

        prompt = f"""
You are a research planning system.

Given a research question, generate:

1. Main Question
2. Sub Questions
3. Search Queries

Return ONLY valid JSON no extra text.

Example only in this format:

{{
  "main_question": "What is AI?",
  "sub_questions": [
    "How does AI work?"
  ],
  "search_queries": [
    "artificial intelligence overview"
  ]
}}

Here's the Research Question:
{query}
"""
        content = llm.generate(prompt)
        print("Planner Response:", content)
        data = json.loads(content)

        return ResearchPlan(**data)