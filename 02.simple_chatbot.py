import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.azure_endpoint = os.getenv("OPENAI_AZURE_ENDPOINT")
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")

while True:

    question = input("질문 입력 : ")
    if question.lower() == "exit":
        print("종료")
        break

    response = openai.chat.completions.create(
        model = "dev-sh-gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are helpful assistant."},
            {"role": "user", "content": question}        
        ]
    )

    print(response.choices[0].message.content)
