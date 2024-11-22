# Neoclient library

Neoclient provides convenient access to the Neospace's inference server from any Python application.

## Installation

First, clone the Neoclient repository to your local machine, then install it in your environment in editable mode.

```sh
git clone https://github.com/neospace-ai/neoclient.git
cd neoclient
pip install -e .
```

## Usage

First, you need to define the environment variables NEOINFER_API_KEY that represents the api key of the inference server and NEOINFER_URL that represents the url where the inference server is hosted. Then, you can run the following code.

```python
import os
from neoclient import Neoclient

client = Neoclient()

chat_completion = client.chat_completions.create(
    messages=[
        {
            "role": "user",
            "content": "Hello!",
        }
    ],
    model="neolang-small",
    temperature=0.2,
    max_tokens=50,
)
```

## Requirements

Python 3.11 or higher.
