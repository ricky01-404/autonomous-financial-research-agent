from fastapi import FastAPI
from pydantic import BaseModel

from app.main import financial_agent

app = FastAPI(
    title="Autonomous Financial Research Agent"
)


class ResearchRequest(BaseModel):

    query: str


@app.get("/")
def home():

    return {
        "message": "Financial Research Agent API Running"
    }


@app.post("/research")
def research(request: ResearchRequest):

    result = financial_agent(request.query)

    return {
        "query": request.query,
        "report": result
    }