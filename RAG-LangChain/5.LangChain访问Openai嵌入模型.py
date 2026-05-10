import os
from langchain_community.embeddings import DashScopeEmbeddings
from dotenv import load_dotenv

load_dotenv()   # 自动读取 .env 中的 DASHSCOPE_API_KEY

embeddings = DashScopeEmbeddings(model="text-embedding-v4")# 选择模型


# 示例：嵌入单个文本
text = "你好，世界"
vector = embeddings.embed_query(text)
print(f"向量维度: {len(vector)}")  
print(vector[:5])  

# 示例：批量嵌入多个文本
texts = ["LangChain 是一个框架", "通义千问是大语言模型"]
vectors = embeddings.embed_documents(texts)
print(f"生成了 {len(vectors)} 个向量")