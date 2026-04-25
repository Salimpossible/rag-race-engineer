from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
from ..models import AgentInput, AgentOutput
from ..agent.state import AgentState
from ..agent.responder import respond

router = APIRouter()


@router.post("/respond", response_model=AgentOutput)
def agent_respond(payload: AgentInput):
    try:
        state = AgentState()
        out = respond(str(payload.input), state, task=payload.task)
        return out
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
