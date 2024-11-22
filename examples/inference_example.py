from neoclient import Neoclient

# Gets API Key from environment variable NEOINFER_API_KEY and base url from NEOINFER_URL
neoclient = Neoclient()

completion = neoclient.chat_completions.create(
    model="neolang-small",
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        },
    ]
)
print (completion.choices[0].message.content)