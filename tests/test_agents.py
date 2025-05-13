import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.example_agent import ExampleAgent


def test_example_agent():
    from agents.example_agent import ExampleAgent
    result = ExampleAgent().run({"log": "error found"}, {})
    assert "error" in result["findings"][0]
