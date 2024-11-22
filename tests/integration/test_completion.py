import pytest

from neoclient.types import Completion

@pytest.mark.integration
def test_completions(client):
    model = "test"
    prompt = "Hello world!"
    temperature = 0.0
    max_tokens = 17

    response = client.completions.create(model=model, prompt=prompt, temperature=temperature, max_tokens=max_tokens)
    assert isinstance(response, Completion)
