from pydantic import BaseModel

class Usage(BaseModel):
    """
    Represents the token usage statistics for a completion request.

    Attributes:
        completion_tokens (int): The number of tokens used in the generated completion.

        prompt_tokens (int): The number of tokens used in the input prompt.

        total_tokens (int): The total number of tokens used in the request, 
            calculated as the sum of `prompt_tokens` and `completion_tokens`.
    """
    completion_tokens: int
    """The number of tokens used in the generated completion."""

    prompt_tokens: int
    """The number of tokens used in the input prompt."""

    total_tokens: int
    """The total number of tokens used in the request, calculated as `prompt_tokens + completion_tokens`."""
