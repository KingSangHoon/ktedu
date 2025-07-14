import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.azure_endpoint = os.getenv("OPENAI_AZURE_ENDPOINT")
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")

response = openai.chat.completions.create(
    model = "dev-sh-gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are helpful assistant."},
        {"role": "user", "content": "이순신이 누구야?"}        
    ]
)

print(response.choices[0].message.content)