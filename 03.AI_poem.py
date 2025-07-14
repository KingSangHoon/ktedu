import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.azure_endpoint = os.getenv("OPENAI_AZURE_ENDPOINT")
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")

while True:

    subject = input("주제를 입력하세요: ")
    content = input("시를 작성할 내용 입력: ")

    if subject.lower() == "exit":
        print("종료")
        break

    response = openai.chat.completions.create(
        model = "dev-sh-gpt-4o-mini",
        temperature= 0.7,
        max_tokens=300,
        messages=[
            {"role": "system", "content": "You are helpful AI poem."},
            {"role": "user", "content": "주제 : " + subject + 
                                        "\n 내용 : " + content +
                                        "\n 시를 작성해 주세요."}        
        ]
    )

    print(response.choices[0].message.content)
