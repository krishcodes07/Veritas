from fastapi import APIRouter

from app.models.request import ResearchRequest
from app.services.research_service import ResearchService

router = APIRouter()

research_service = ResearchService()


@router.post("/research")
async def research(request: ResearchRequest):
    return research_service.run(request.query)