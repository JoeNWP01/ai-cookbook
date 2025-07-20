import os

from openai import OpenAI

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key='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')

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You're a helpful assistant."},
        {
            "role": "user",
            "content": "Write a limerick about the Python programming language.",
        },
    ],
)

response = completion.choices[0].message.content
print(response)
