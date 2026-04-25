from pydantic import BaseModel, Field
from typing import Any, List, Optional


class AgentInput(BaseModel):
    task: str
    input: Any
    params: Optional[dict] = None


class Section(BaseModel):
    heading: str
    body: str


class AgentOutput(BaseModel):
    title: str
    summary: str
    sections: Optional[List[Section]] = None
    metadata: Optional[dict] = None
