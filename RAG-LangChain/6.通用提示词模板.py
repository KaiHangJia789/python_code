from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi
from dotenv import load_dotenv

load_dotenv()

prompt_template = PromptTemplate.from_template(
    "我的邻居性{lastname}刚生了{gender}，你帮我起个名字,简单回答"
)
model = Tongyi(model="qwen-max")
#调用.format方法,传入参数,得到结果
# prompt_text = prompt_template.format(lastname="贾", gender="女")

# model = Tongyi(model="qwen-max")
# res = model.invoke(input=prompt_text)
# print(res)

chain = prompt_template | model
res = chain.invoke(input={"lastname":"贾","gender":"女"})
print(res)