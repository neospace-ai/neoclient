import pytest
from neoclient import Neoclient

@pytest.mark.unit
def test_env_variables(monkeypatch):
    monkeypatch.setenv("NEOINFER_URL", "http://localhost:8000")
    monkeypatch.setenv("NEOINFER_API_KEY", "test_key")

    client = Neoclient()
    assert client.base_url == "http://localhost:8000"
    assert client.api_key == "test_key"


@pytest.mark.unit
def test_post_request(mocker):
    mock_response = mocker.patch("requests.post")
    mock_response.return_value.status_code = 200
    mock_response.return_value.json.return_value = {"data": "success"}

    client = Neoclient(base_url="https://api.example.com", api_key="test_key")
    response = client._post("v1/test", {"key": "value"})
    assert response["data"] == "success"