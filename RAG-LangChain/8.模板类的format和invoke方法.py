from langchain_core.prompts import ChatPromptTemplate
from langchain_core .prompts import PromptTemplate
from langchain_core .prompts import FewShotPromptTemplate

"""
PromptTemplate-->StringPromptTemplate-->BasePromptTemplate-->RunnableSerializable-->Runnable
ChatPromptTemplate-->StringPromptTemplate-->BasePromptTemplate-->RunnableSerializable-->Runnable
FewShotPromptTemplate-->BaseChatPromptTemplate-->BasePromptTemplate-->RunnableSerializable-->Runnable

"""
template = PromptTemplate.from_template("请翻译以下文本:{text}")
res = template.format(text="Hello World")  
print(res,type(res))

res2 = template.invoke(input={"text":"Hello World"})
print(res2,type(res2))