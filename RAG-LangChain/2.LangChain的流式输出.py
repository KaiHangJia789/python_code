from langchain_community.llms import Tongyi
from dotenv import load_dotenv
import os
load_dotenv()

model = Tongyi(model="qwen-turbo")
res = model.invoke(input="你是谁能做是什么？")

for chunk in res:
    print(chunk,end="",flush=True)