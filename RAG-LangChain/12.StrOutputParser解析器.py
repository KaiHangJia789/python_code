from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

parser = StrOutputParser()#创建一个解析器
model = ChatTongyi(model="qwen3-max")

prompt = PromptTemplate.from_template(
    "我的邻居:{lastname},刚生了{gender},请取名,仅告知我名字无需其他内容."
)

#chain = prompt | model | parser | model
#res = chain.invoke({"lastname": "张", "gender": "女孩"}).content

chain = prompt | model | parser | model | parser#多加一个parser解析器,
res = chain.invoke({"lastname": "张", "gender": "女孩"})#让模型的输出类型为str
print(res)
