#Zero Short Prompting
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="AQ.Ab8RN6Ix-CCnlLz4U8zsipRE1RzKBiMcIk4JJXNKqlGPXzxcKw",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

#Zero shot prompting: Directly giving the inst to the model
SYSTEM_PROMPT = "You should only and only answer the coding related questions. Do not answer anything else. Your name is Athex. If user asks something other than coding, just say sorry."

response = client.chat.completions.create(
    model="gemini-3.6-flash",
    messages=[
        {"role":"system", "content": SYSTEM_PROMPT},
        {"role": "user", "content":"Hey, Can you tell me a"}
    ]
)

print(response.choices[0].message.content)