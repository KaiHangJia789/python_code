"""
streamlit run "RAG-LangChain\RAG项目案例\app_qa.py"
"""
from click import prompt
import streamlit as st
from rag import RagService
import config_data as config

#标题
st.title('智能客服')
st.divider()       #分割线

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "欢迎来到智能客服，请输入问题。"}
    ]

if "rag" not in st.session_state:       #创建rag服务
    st.session_state["rag"] = RagService()

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])


#在页面下方提供用户输入栏
prompt = st.chat_input()
if prompt:

    #在页面输出用户的消息
    st.chat_message("user").write(prompt)
    st.session_state["messages"].append({"role": "user", "content": prompt})

    with st.spinner("正在思考..."):
        res_stream = st.session_state["rag"].chain.stream({"input": prompt},config.session_config)
        result= st.chat_message("assistant").write_stream(res_stream)
        st.session_state["messages"].append({"role": "assistant", "content": result})
