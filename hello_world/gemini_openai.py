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
        {"role":"system", "content":"You are an expert in maths and only and only answer maths questions. That if the query is not related to maths just say Sorry "},
        {"role": "user", "content":"Hey, Can you help me in a + b whole square"}
    ]
)

print(response.choices[0].message.content)