from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="AQ.Ab8RN6Ix-CCnlLz4U8zsipRE1RzKBiMcIk4JJXNKqlGPXzxcKw",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response = client.chat.completions.create(
    model="gemini-3.6-flash",
    messages=[
        {"role": "user", "content":"Hey, I am Atharva kumbhar! Nice to meet you C an you tell your name and what soo special about you ?"}
    ]
)

print(response.choices[0].message.content)