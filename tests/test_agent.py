from nextstep.agent import AIProjectAgent


def test_generate_tasks(monkeypatch):
    agent = AIProjectAgent()
    result = agent.generate_tasks("Build an authentication system")

    assert "a" in result
