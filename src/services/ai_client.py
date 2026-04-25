from typing import Dict


class AIClient:
    """Stubbed AI client. Replace with provider integration as needed."""

    def __init__(self):
        pass

    def generate(self, prompt: Dict) -> Dict:
        # Deterministic, safe sample output used in tests.
        return {"title": prompt.get("title", "sample"), "summary": prompt.get("summary", "sample summary")}
