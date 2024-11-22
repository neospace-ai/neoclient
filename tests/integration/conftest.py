import os
import pytest

@pytest.fixture
def client():
    from neoclient import Neoclient
    return Neoclient(base_url=os.getenv("NEOINFER_URL"), api_key=os.getenv("NEOINFER_API_KEY"))
