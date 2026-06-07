from pydantic import BaseModel


class ResearchPlan(BaseModel):
    main_question: str
    sub_questions: list[str]
    search_queries: list[str]