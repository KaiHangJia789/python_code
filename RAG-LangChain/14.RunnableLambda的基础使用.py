from langchain_core.output_parsers import  StrOutputParser, JsonOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

#创造所需的解析器
str_parser = StrOutputParser()

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

#函数的入参是一个AI消息对象，出参是一个字典
my_func = RunnableLambda(lambda ai_msg:{"name":ai_msg.content})

chain = first_prompt | model | my_func | second_prompt | model | str_parser

for chunk in chain.stream({"lastname": "贾","gender": "女孩"}):
    print(chunk,end="",flush=True)