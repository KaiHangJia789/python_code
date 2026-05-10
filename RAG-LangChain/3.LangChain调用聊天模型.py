from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
import logging
logging.basicConfig(level=logging.DEBUG)

load_dotenv()

model = ChatTongyi(model="qwen-max", request_timeout=30)

# 测试3：完整消息
messages = [
    SystemMessage(content="你是一个边塞诗人"),
    HumanMessage(content="写一首关于春天的诗"),
    AIMessage(content="春去，西风瘦马，客输，西风瘦马"),
    HumanMessage(content="请将上句的开头替换成“春去”"),
]
for chunk in model.stream(input=messages):
    print(chunk.content, end="", flush=True)