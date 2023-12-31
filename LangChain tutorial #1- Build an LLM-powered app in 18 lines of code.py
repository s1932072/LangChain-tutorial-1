import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 Quickstart App')



def generate_response(input_text):
    # ローカルのLLMエンドポイントに接続するための設定
    llm = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed", temperature=0.7)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('Enter text:', '日本の首都はどこですか?')
    submitted = st.form_submit_button('Submit')
    # OpenAI APIキーのバリデーションをコメントアウト
    # if not openai_api_key.startswith('sk-'):
    #     st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted:
        generate_response(text)