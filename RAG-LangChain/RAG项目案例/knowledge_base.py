"""
知识库
"""
import os
import hashlib
from tkinter.ttk import Separator
import config_data as config
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from datetime import datetime
def check_md5(md5_str: str):
    """
    检查md5字符串是否被处理过"""
    if not os.path.exists(config.md5_path):
        #文件不存在.创建一个空文件，并返回False
        open(config.md5_path, 'w',encoding = 'utf-8').close()
        return False
    else:
        for line in open(config.md5_path,'r',encoding=  'utf-8').readlines():
            line = line.strip() #去掉换行符和首尾空格
            if line == md5_str:
                return True     #被处理过
        return False

def save_md5(md5_str: str):
    """将传进的md5字符串保存到文件中"""
    with open(config.md5_path,'a',encoding='utf-8') as f:
        f.write(md5_str + '\n')

def get_string_md5(inpout_str: str,encoding = 'utf-8'):
    """将传入的字符串转换为md5字符串"""

    #将字符串转化为字节串
    input_bytes = inpout_str.encode(encoding)

    #创建md5对象
    md5_obj = hashlib.md5()         #创建md5对象
    md5_obj.update(input_bytes)     #更新对象
    md5_str = md5_obj.hexdigest()   #获取md5值

    return md5_str


class KnowledgeBaseService(object):
    """知识库服务类"""

    def __init__(self):
        os.makedirs(config.persist_directory, exist_ok=True)
        self.chroma = Chroma(
            collection_name=config.collection_name,#数据库表名
            embedding_function=DashScopeEmbeddings(model="text-embedding-v4"),
            persist_directory=config.persist_directory,#数据库文件路径
        )     #chroma对象,向量储存实例
        self.spliter = RecursiveCharacterTextSplitter(
            chunk_size = config.chunk_size,         #分割后的文本最大长度
            chunk_overlap = config.chunk_overlap,   #分割后的文本之间的重叠长度
            separators=config.Separators,           #分割符
            length_function = len,                  #计算文本长度的函数
        )    #分词器实例
    def upload_by_str(self,data,filename):
        """将传进来的字符串.进行向量化 并保存到数据库中"""
        #获取md5字符串
        md5_hex = get_string_md5(data)

        if check_md5(md5_hex):
            print("文件已处理过")
            return "文件已处理过"

        if len(data) > config.max_split_char_number:
            knowledge_chunks = self.spliter.split_text(data)#分割文本
        else:
            knowledge_chunks = [data]
        
        metadata = {
            "source": filename,
            "operator": "mine",
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            
        }


        self.chroma.add_texts(     #内容加载到向量库中
            #iterale -> list/tuple
            texts = knowledge_chunks,
            metadatas = [metadata for _ in knowledge_chunks] ,#元数据
        )

        save_md5(md5_hex)
        print("上传成功")
        return "上传成功"
        

if __name__ == '__main__':
    text = KnowledgeBaseService()
    file_path = r"RAG-LangChain\RAG项目案例\data\春天衣服推荐.txt"

    with open(file_path, "r", encoding="utf-8")as f:
        file_content = f.read()
    text.upload_by_str(file_content,"春天衣服推荐")