from ..models import AgentOutput
from ..services.ai_client import AIClient
from .state import AgentState


def respond(input_text: str, state: AgentState) -> AgentOutput:
    # deterministic stubbed response for scaffold
    client = AIClient()
    res = client.generate(
        {"title": "Sample response", "summary": "This is a deterministic sample response."}
    )
    state.push("assistant", res.get("summary", ""))
    return AgentOutput(title=res.get("title"), summary=res.get("summary"))
