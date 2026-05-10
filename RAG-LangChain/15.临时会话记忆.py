from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate,MessagesPlaceholder#模板
from langchain_core.output_parsers import StrOutputParser#输出解析器
from langchain_core.runnables import RunnableWithMessageHistory#让链自动读取 / 保存记录
from langchain_core.chat_history import InMemoryChatMessageHistory#在内存中保存会话历史

model = ChatTongyi(model="qwen3-max")

# prompt = PromptTemplate.from_template(
#     "你需要根据历史会话回应用户问题.对话历史:{chat_history},用户提问:{input},请给出回答."
# )
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你需要根据历史会话回应用户问题,历史会话:"),
        MessagesPlaceholder("chat_history"),#临时会话记忆
        ("human","请回答如下问题:{input}")
    ]
)


str_parser =StrOutputParser() 

base_chain = prompt | model | str_parser

store = {}      #存储会话历史的字典
#实现通过会话id获取历史消息的函数
def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

#创建一个新的链,对原有链增强功能，自动解析历史消息
conversation_chain = RunnableWithMessageHistory(
    base_chain,#增强的链
    get_history,#通过会话id,获取InMessageHistory对象
    input_messages_key="input",#用户输入的消息在输入字典中的key
    history_messages_key="chat_history"#历史消息在输入字典中的key
)

if __name__ == "__main__":
    session_confg = {
        "configurable":{
            "session_id":"user_001"
        }
    }

    res = conversation_chain.invoke({"input":"小明有一只狗"},config=session_confg)
    print("第一次:",res)
    res = conversation_chain.invoke({"input":"小美有2只猫"},config=session_confg)
    print("第2次:",res)
    res = conversation_chain.invoke({"input":"总共有多少只动物?"},config=session_confg)
    print("第3次:",res)