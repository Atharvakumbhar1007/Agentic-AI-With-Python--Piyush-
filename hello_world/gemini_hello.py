from google import genai

client = genai.Client(
    api_key="AQ.Ab8RN6Ix-CCnlLz4U8zsipRE1RzKBiMcIk4JJXNKqlGPXzxcKw"
)

response = client.models.generate_content(
    model="gemini-3.6-flash", contents="Explain how AI works in a few words"
)

print(response.text)