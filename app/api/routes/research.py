from fastapi import APIRouter

router = APIRouter()

@router.post("/research")
async def research():
    return {
        "status": "received"
    }