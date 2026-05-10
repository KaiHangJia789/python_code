import re

from vector_stores import VectorStoreService
from langchain_community.embeddings import DashScopeEmbeddings
import config_data as config
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models.tongyi  import ChatTongyi
from langchain_core.documents import Document
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from file_history_store import get_history
#RunnableWithMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.runnables import RunnableLambda#运行时
from config_data import session_config


def print_prompt(prompt):
    print(prompt.to_string())
    print("=" * 50)
    return prompt


class RagService(object):
    def __init__(self):
        # 修改: 使用 embedding_model_name 而不是 chat_model_name
        self.vector_service = VectorStoreService(
            DashScopeEmbeddings(model=config.embedding_model_name))

        self.prompt_template = ChatPromptTemplate.from_messages([
        
            ("system", "以我提供的已知参考资料为主，"
             "简洁和专业的回答我的问题.参考资料为:{content}."),
             ("system","并且我提供用户的对话历史记录,如下:"),
             MessagesPlaceholder("history"),
             ("user","请回答我的问题:{input}")
        ])

        self.chat_model = ChatTongyi(model = config.chat_model_name)

        self.chain= self.__get_chain()

    
    def __get_chain(self):
        """
        获取最终链"""
        retriever = self.vector_service.get_retriever()
        def format_document(docs: list[Document]):
            if not docs:
                return "无相关参考资料"
            
            formatted_str = ""
            for doc in docs:
                formatted_str += f"文档片段:{doc.page_content}\n文档元数据:{doc.metadata}\n\n"
            return formatted_str
        
        def temp1(value:dict)->str:
            return value["input"]

        # 修改: 直接使用 value 字典，不再尝试嵌套访问
        def temp2(value):
            # value 结构应为 {"question": ..., "reference": ..., "input": ...}
            new_value = {
                "input": value["question"],  # 用户输入的问题
                "content": value["reference"],  # 检索到的参考资料
                "history": value.get("history", [])  # 对话历史（由 RunnableWithMessageHistory 自动注入）
            }
            return new_value
        
        chain = (
            {
                "question": RunnablePassthrough(),       #获取问题
                "reference": RunnableLambda(temp1) | retriever | format_document #检索数据库
            } 
            | RunnableLambda(temp2) 
            | self.prompt_template      #构建提示词
            | print_prompt                        
            | self.chat_model
            | StrOutputParser()
        )

        conversation_chain = RunnableWithMessageHistory(
            chain,
            get_history,
            input_messages_key="input",
            history_messages_key="history",
            
            )
        return conversation_chain
    
if __name__ == "__main__":
    

    rag= RagService()
    
    answer = rag.chain.invoke({"input":"春天应该穿什么衣服"},session_config)
    print(answer)