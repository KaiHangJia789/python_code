# langchain_community
from langchain_community.llms import Tongyi
from dotenv import load_dotenv#加载环境变量
import os#操作系统

load_dotenv()#从.env中获取阿里云API Key


#不用qwen3-max,是因为qwen3-max是聊天模型,qwen-max是大语言模型
model = Tongyi(model="qwen-turbo")


#调用invoke方法,传入问题,得到答案
res = model.invoke(input="你是谁能做是什么？")
print(res)