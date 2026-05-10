import os,json
from typing import Sequence#列表
from langchain_core.messages import message_to_dict,messages_from_dict,BaseMessage#消息对象和消息字典的转换函数,BaseMessage是消息对象的基类
from langchain_core.chat_history import BaseChatMessageHistory#会话历史基类
from langchain_community.chat_models import ChatTongyi  # 添加ChatTongyi的导入
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate,MessagesPlaceholder#模板
from langchain_core.output_parsers import StrOutputParser#输出解析器
from langchain_core.runnables import RunnableWithMessageHistory#让链自动读取 / 保存记录
from langchain_core.chat_history import InMemoryChatMessageHistory#在内存中保存会话历史
#message_to_dict:单个消息对象-->消息字典
#messages_from_dict:[字典,字典,...]-->[消息,消息,...]
#BaseChatMessageHistory:会话历史基类

class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self,session_id,storage_path):
        self.session_id = session_id#会话id
        self.storage_path = storage_path#不同会话id的存储路径

        #完整的文件路径
        self.file_path = os.path.join(self.storage_path,self.session_id)

        #确保文件夹存在
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def add_message(self,messages: Sequence[BaseMessage]) ->None:
        #Sequence序列类型,可以是列表,元组等
        all_messages = list(self.messages)#获取已有消息
        all_messages.append(messages)#添加新消息

        #数据同步写入本地文件中
        #类对象写入文件->二进制
        #为方便,可以将BaseMessage对象转换为字典,然后写入文件
        #message_to_dict:单个消息对象(BaseMessage)-->消息字典
        # new_messages = []
        # for message in all_messages:
        #     message_dict = message_to_dict(message)
        #     new_messages.append(message_dict)

        new_messages = [message_to_dict(message) for message in all_messages]

        #将消息列表转换为JSON字符串,并写入文件
        with open(self.file_path,"w",encoding="utf-8") as f:
            json.dump(new_messages,f)

    @property   #@property装饰器,将方法变为属性
    def messages(self) -> Sequence[BaseMessage]:
        #当前文件内:List[字典]
        try:
            with open(self.file_path,"r",encoding="utf-8") as f:
                messages_dict = json.load(f)#返回值是:List[字典]
                #将消息字典转换为消息对象
                return messages_from_dict(messages_dict)
        except FileNotFoundError:  # 文件不存在
            return []

            #清空会话
    def clear(self) ->None:
        with open(self.file_path,"w",encoding="utf-8") as f:
            json.dump([],f)

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
    return FileChatMessageHistory(session_id,"./langchain_chat_history")#每个会话id对应一个文件,存储在./chat_history文件夹中  

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
    # res = conversation_chain.invoke({"input":"总共有多少只动物?"},config=session_confg)
    # print("第3次:",res)