import pytest

from neoclient.types import ChatCompletion

@pytest.mark.integration
def test_chat_completions(client):
    model = "test"
    messages = [
        {
            "role": "user",
            "content": "Hello world!"
        }]
    temperature = 0.0
    max_tokens = 17

    response = client.chat_completions.create(model=model, messages=messages, temperature=temperature, max_tokens=max_tokens)
    assert isinstance(response, ChatCompletion)
