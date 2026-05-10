from tkinter.ttk import Separator

from ollama import chat


md5_path = r"RAG-LangChain/RAG项目案例/md5.text"

#Chroma
collection_name = "rag"
persist_directory = "RAG-LangChain/RAG项目案例/chroma_db"


#spliter
chunk_size = 500
chunk_overlap = 50
Separators = ["\n\n", "\n", " ", ".","。","！","？","；","，",",","?","!",""]
max_split_char_number = 500

#
similarity_threshod = 1    #返回检索匹配的文档数量

embedding_model_name = "text-embedding-v4"
chat_model_name = "qwen3-max"


#配置session id
session_config = {
    "configurable":
    {
        "session_id": "user_001",
    },        
}