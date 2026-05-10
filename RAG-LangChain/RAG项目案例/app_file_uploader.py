"""
基于Streamlit完成Web网页上传服务
pip install streamlit
"""

import streamlit as st
import time

from knowledge_base import KnowledgeBaseService
#添加网页标题
st.title("知识库更新服务")

if "service" not in st.session_state:
    st.session_state["service"] = KnowledgeBaseService()


#file_uploader
file_uploader = st.file_uploader(
    "请上传知识库文件",
    type=["txt"],
    accept_multiple_files=False,#是否允许上传多个文件
    
)

if file_uploader is not None:
    #提取文件的信息
    file_name = file_uploader.name
    file_size = file_uploader.size/ 1024 #单位KB
    file_type = file_uploader.type

    st.subheader(f"文件名:  {file_name}")
    st.write(f"格式: {file_type} | 文件大小:  {file_size:.2f}KB")

    #get_value -> bytes ->decode('utf-8') -> str
    text = file_uploader.getvalue().decode("utf-8")

    with st.spinner("正在处理..."):     #转圈动画
        time.sleep(1)
        text_1 = st.session_state["service"].upload_by_str(text,file_name)
        st.write(text_1)