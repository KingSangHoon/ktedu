import openai
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.azure_endpoint = os.getenv("OPENAI_AZURE_ENDPOINT")
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")

def get_openai_client(messages):
    try:
        response = openai.chat.completions.create(
        model = "dev-sh-gpt-4o-mini",
        messages= messages,
        temperature=0.7,
        max_tokens=300
        )
        return response.choices[0].message.content
    
    except Exception as e:
        st.error(f"OpenAI API 호출 중 Error : {e}")
        return None
    
st.title("Azure OpenAI 활용 !!!")
st.write("Chating Interface ~~~")

if 'messages' not in st.session_state:
    st.session_state.messages = []

if user_input := st.chat_input("메세지 입력 : "):
    st.session_state.messages.append({"role" : "user", "content" : user_input})
    st.chat_message("user").write(user_input)

    with st.spinner("응답 작성 중 ......"):
        assitant_response = get_openai_client(st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content" : assitant_response})
        st.chat_message("assistant").write(assitant_response)
