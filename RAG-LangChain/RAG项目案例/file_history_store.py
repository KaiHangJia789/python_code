import os,json
from typing import Sequence#列表
from langchain_core.messages import message_to_dict,messages_from_dict,BaseMessage#消息对象和消息字典的转换函数,BaseMessage是消息对象的基类
from langchain_core.chat_history import BaseChatMessageHistory#会话历史基类


#实现通过会话id获取历史消息的函数
def get_history(session_id):
    return FileChatMessageHistory(session_id,"RAG-LangChain/RAG项目案例/langchain_chat_history")#每个会话id对应一个文件,存储在./chat_history文件夹中  


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