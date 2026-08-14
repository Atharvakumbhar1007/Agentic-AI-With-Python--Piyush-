from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

print("API key found:", bool(os.getenv("OPENAI_API_KEY")))

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Hey I am Atharva! Nice to meet you..."
        }
    ]
)

print(response.choices[0].message.content)