from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
from ..models import AgentInput, AgentOutput
from ..agent.prompt_builder import build_prompt
from ..agent.state import AgentState
from ..agent.responder import respond

router = APIRouter()


@router.post("/respond", response_model=AgentOutput)
def agent_respond(payload: AgentInput):
    try:
        state = AgentState()
        prompt = build_prompt(payload.task, str(payload.input))
        # For the scaffold we ignore prompt and use a deterministic responder
        out = respond(str(payload.input), state)
        return out
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
