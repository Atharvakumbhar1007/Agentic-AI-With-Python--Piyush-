# Few short prompting
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="AQ.Ab8RN6JqjQCn45c1PjXdlt3dfTa509QTY52TfQutwjlxMY4yoQ",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

#Few shot prompting: Directly giving the inst to the model and few eaxamples to the models
SYSTEM_PROMPT = """You should only and only answer the coding related questions. 
Do not answer anything else.Your name is Athex. If user asks something 
other than coding, just say sorry.
Examples:
Q: Can you explain the a + b whole square?
A: Sorry, I can only help with Coding related Questions.

Q:Hey, Write a code in python for  adding two numbers
A: def add(a,b):
return a + b

"""

response = client.chat.completions.create(
    model="gemini-3.6-flash",
    messages=[
        {"role":"system", "content": SYSTEM_PROMPT},
        {"role": "user", "content":"Hey, Can you write a python code to translate the to Hindi"}
    ]
)

print(response.choices[0].message.content)