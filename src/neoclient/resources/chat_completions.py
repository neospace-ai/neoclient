from typing import Dict, List, Optional

from neoclient.types import ChatCompletion, ChatCompletionChoice, Usage

class ChatCompletions:
    def __init__(self, client) -> None:
        self.client = client

    def create(self,
               model: str,
               messages: List[Dict[str, str]],
               max_tokens: Optional[int]=1024,
               temperature: Optional[float]=1.0,
               top_p: Optional[float]=1.0,
               ignore_eos: Optional[bool]=False,
        ) -> ChatCompletion:
        """
        Generates a response from the model for the given chat conversation.

        Args:
            model (str): The ID of the model to use for generating the response.

            messages (List[Dict[str, str]]): A list of messages representing the conversation so far. 
                Each message should be a dictionary containing:
                    - 'role' (str): The role of the sender, e.g., 'system', 'user', or 'assistant'.
                    - 'content' (str): The content of the message.

            max_tokens (Optional[int]): The maximum number of tokens that the model can generate 
                in the response. Default is 1024.

            temperature (Optional[float]): The sampling temperature, between 0 and 2. Higher values 
                (e.g., 0.8) produce more random outputs, while lower values (e.g., 0.2) produce more 
                deterministic outputs. Default is 1.0.

                Note: It is generally recommended to adjust either `temperature` or `top_p`, but not both.

            top_p (Optional[float]): The nucleus sampling probability. The model considers the tokens 
                with a cumulative probability mass of `top_p`. For example, `top_p=0.1` means only tokens 
                within the top 10% probability mass are considered. Default is 1.0.

                Note: It is generally recommended to adjust either `top_p` or `temperature`, but not both.

            ignore_eos (Optional[bool]): Makes the request not stop while finding an end of sequence token.
                I.e., the model keeps genearating tokens until it generates max_tokens.

        Returns:
            ChatCompletion: An object representing the model's response, including the generated choices, 
            usage details, and metadata such as the response ID and creation time.

        Example:
            >>> chat_response = client.chat_completions.create(
            ...     model="neolang-small",
            ...     messages=[
            ...         {"role": "system", "content": "You are a helpful assistant."},
            ...         {"role": "user", "content": "What's the weather like today?"},
            ...     ],
            ...     max_tokens=50,
            ...     temperature=0.7
            ... )
            >>> print(chat_response.messages[0].content)
        """
        self._validate_messages(messages)

        payload = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
        }
        if ignore_eos:
            payload["ignore_eos"] = ignore_eos
        response = self.client._post("v1/chat/completions", payload)
        choices = [ChatCompletionChoice(**choice) for choice in response.get("choices", [])]
        usage = Usage(**response.get("usage", {}))
        return ChatCompletion(
            id=response["id"],
            choices=choices,
            created=response["created"],
            model=response["model"],
            object=response["object"],
            usage=usage
        )


    def _validate_messages(self, messages: List[Dict[str, str]]):
        valid_roles = {"system", "assistant", "user", "tool"}

        for msg in messages:
            if msg.get("role") not in valid_roles:
                raise ValueError(f"Invalid role: {msg.get('role')}. Valid roles are {valid_roles}.")
            
        if messages and messages[-1].get("role") not in {"user", "tool"}:
            raise ValueError(f"The role of the last message must be either 'user' or 'tool'.")
        
        system_count = sum(1 for msg in messages if msg.get("role") == "system")
        if system_count > 1:
            raise ValueError(f"There must be only one 'system' role.")
        
        for i in range(1, len(messages)):
            if messages[i].get("role") == messages[i - 1].get("role"):
                raise ValueError(f"Repeating roles are not allowed: {messages[i].get('role')} appears consecutively.")