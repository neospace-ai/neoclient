from pydantic import BaseModel
from typing import List
from typing_extensions import Literal

from neoclient.types import ChatCompletionChoice, Usage

class ChatCompletion(BaseModel):
    """
    Represents the response from a model after processing a chat completion request.

    Attributes:
        id (str): A unique identifier for the chat completion request.

        choices (List[ChatCompletionChoice]): A list of chat completion choices generated by 
            the model. Each choice contains the generated messages and other relevant details.

        created (int): The Unix timestamp (in seconds) of when the chat completion request 
            was processed.

        model (str): The identifier of the model used to generate the chat completion.

        object (Literal["chat.completion"]): The type of object, which is always "chat.completion".

        usage (Usage): Token usage statistics for the chat completion request, including the number 
            of tokens used in the prompt and completion.
    """
    id: str
    """A unique identifier for the chat completion request."""

    choices: List[ChatCompletionChoice]
    """A list of chat completion choices generated by the model."""

    created: int
    """The Unix timestamp (in seconds) of when the chat completion request was processed."""

    model: str
    """The identifier of the model used to generate the chat completion."""

    object: Literal["chat.completion"]
    """The type of object, which is always "chat.completion"."""

    usage: Usage
    """Token usage statistics for the chat completion request."""
