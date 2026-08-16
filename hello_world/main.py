import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Check if API key exists
print("API key found:", bool(api_key))

# Stop the program if API key is missing
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the .env file")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Send request to Gemini
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Hello, how are you?"
)

# Print Gemini's response
print(interaction.output_text)