from langchain_core.output_parsers import  StrOutputParser, JsonOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate

#创造所需的解析器
str_parser = StrOutputParser()
json_parser = JsonOutputParser()

#创造模型
model = ChatTongyi(model="qwen3-max")

#第一个提示词模板
first_prompt = PromptTemplate.from_template(
    "我的邻居性:{lastname},刚生了{gender},请取名,仅告知我名字无需其他内容."
    "请以json格式输出,格式如下:{{'name': '名字'}}"
)

#第二个提示词模板
second_prompt = PromptTemplate.from_template(
    "姓名:{name},请告诉我这个名字的含义."
)

#链式调用
chain = first_prompt | model | json_parser | second_prompt | model | str_parser

# res = chain.invoke({"lastname": "贾","gender": "女孩"})
# print(res)
# print(type(res))

#流式输出
for chunk in chain.stream({"lastname": "贾","gender": "女孩"}):
    print(chunk,end="",flush=True)