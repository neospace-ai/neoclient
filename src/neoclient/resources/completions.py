from typing import Optional

from neoclient.types import Completion, CompletionChoice, Usage

class Completions:
    def __init__(self, client) -> None:
        self.client = client

    def create(self,
               model: str,
               prompt: str,
               max_tokens: Optional[int]=1024,
               temperature: Optional[float]=1.0,
               top_p: Optional[float]=1.0,
        ) -> Completion:
        """
        Generates a text completion for the given prompt using the specified model.

        Args:
            model (str): The ID of the model to use for generating the text completion.

            prompt (str): The input text for which the model should generate a completion.

            max_tokens (Optional[int]): The maximum number of tokens to generate in the completion.
                Default is 1024.

            temperature (Optional[float]): The sampling temperature, a value between 0 and 2. Higher
                values (e.g., 0.8) result in more random outputs, while lower values (e.g., 0.2) produce
                more focused and deterministic outputs. Default is 1.0.

                Note: It is generally recommended to adjust either `temperature` or `top_p`, but not both.

            top_p (Optional[float]): The nucleus sampling probability. The model considers tokens with
                a cumulative probability mass of `top_p`. For instance, `top_p=0.1` restricts the model
                to considering only tokens within the top 10% probability mass. Default is 1.0.

                Note: It is generally recommended to adjust either `top_p` or `temperature`, but not both.

        Returns:
            Completion: An object representing the model's response, including the generated choices,
            usage details, and metadata such as the response ID and creation time.

        Example:
            >>> completion = client.completions.create(
            ...     model="neolang-small",
            ...     prompt="Once upon a time,",
            ...     max_tokens=50,
            ...     temperature=0.7
            ... )
            >>> print(completion.choices[0].text)
        """
        payload = {
            "model": model,
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
        }
        response = self.client._post("v1/completions", payload)
        choices = [CompletionChoice(**choice) for choice in response.get("choices", [])]
        usage = Usage(**response.get("usage", {}))
        return Completion(
            id=response["id"],
            choices=choices,
            created=response["created"],
            model=response["model"],
            object=response["object"],
            usage=usage
        )