from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="deepseek-chat", request_timeout=30,max_retries=3)

# 测试3：完整消息
messages = [
    ("system","你是一个边塞诗人"),
    ("human","写一首关于春天的诗"),
    ("ai","春去，西风瘦马，客输，西风瘦马"),
    ("human","按照上一个回复的格式，写一首关于夏天的诗"),
]
for chunk in model.stream(input=messages):
    print(chunk.content, end="", flush=True)