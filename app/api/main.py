from fastapi import FastAPI
from app.api.routes.research import router as research_router

app = FastAPI(
    title="Veritas",
    version="0.1.0"
)

app.include_router(research_router)

@app.get("/")
async def root():
    return {
        "name": "Veritas",
        "status": "running"
    }