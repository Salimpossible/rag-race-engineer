from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class AgentState:
    history: List[Dict] = field(default_factory=list)

    def push(self, role: str, content: str):
        self.history.append({"role": role, "content": content})
