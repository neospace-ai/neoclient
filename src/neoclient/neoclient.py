import os
import requests

from dotenv import load_dotenv
from typing import Dict
from neoclient.resources import ChatCompletions, Completions

load_dotenv()

class Neoclient:
    def __init__(self, base_url=None, api_key=None) -> None:
        """Construct a new neoclient instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `base_url` from `NEOINFER_URL`
        - `api_key` from `NEOINFER_API_KEY`
        """
        self.base_url = base_url or os.getenv("NEOINFER_URL")
        self.api_key = api_key or os.getenv("NEOINFER_API_KEY")
        if not self.base_url or not self.api_key:
            raise ValueError("NEOINFER_URL and NEOINFER_API_KEY must be set as arguments or environment variables")
        self.completions = Completions(self)
        self.chat_completions = ChatCompletions(self)


    def _post(self, endpoint: str, payload: Dict):
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        response = requests.post(f"{self.base_url}/{endpoint}", json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
