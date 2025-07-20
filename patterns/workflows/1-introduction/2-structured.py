import os
import json
import requests

from openai import OpenAI
from pydantic import BaseModel

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key='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')



# --------------------------------------------------------------
# Step 1: Define the response format in a Pydantic model
# --------------------------------------------------------------


class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]


# --------------------------------------------------------------
# Step 2: Call the model
# --------------------------------------------------------------

completion = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {
            "role": "user",
            "content": "Alice and Bob are going to a science fair on Friday.",
        },
    ],
    response_format=CalendarEvent,
)

# --------------------------------------------------------------
# Step 3: Parse the response
# --------------------------------------------------------------

event = completion.choices[0].message.parsed
event.name
event.date
event.participants
