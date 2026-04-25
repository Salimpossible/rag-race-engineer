from src.agent.prompt_builder import build_prompt


def test_build_prompt_sections():
    prompt = build_prompt("generate", "Create a short summary.")
    assert "system" in prompt
    assert "user" in prompt
    assert "Create a short summary" in prompt["user"] or "Create a short summary." in prompt["user"]
