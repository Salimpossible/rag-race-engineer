from pathlib import Path
from typing import Dict


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def build_prompt(task: str, user_input: str) -> Dict[str, str]:
    """Build a combined prompt using system + task prompts.

    Returns a dict with `system` and `user` keys.
    """
    base = Path(__file__).resolve().parents[3]
    prompts_dir = base / "prompts"
    system = _read(prompts_dir / "system.md")
    task_file = prompts_dir / "tasks" / f"{task}.md"
    task_prompt = _read(task_file)
    user = f"{task_prompt}\n\nInput:\n{user_input}\n"
    return {"system": system.strip(), "user": user.strip()}
