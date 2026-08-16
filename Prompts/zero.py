# Zero Shot Prompting

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env file
load_dotenv()

# Get Gemini API key from .env
api_key = os.getenv("GEMINI_API_KEY")

# Check API key
print("API key found:", bool(api_key))

# Create OpenAI-compatible Gemini client
client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# System prompt
SYSTEM_PROMPT = """
You should only and only answer coding-related questions.
Do not answer anything else.
Your name is Athex.
If the user asks something other than coding, just say sorry.
"""

# Send request to Gemini
response = client.chat.completions.create(
    model="gemini-3.6-flash",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "Hey, can you tell me a joke?"
        }
    ]
)

# Print response
print(response.choices[0].message.content)