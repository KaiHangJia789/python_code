from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader(r"data/python基础.txt",encoding="utf-8")

documents = loader.load()

splititer = RecursiveCharacterTextSplitter(
    chunk_size=300,        # 每个文本块的最大长度
    chunk_overlap=200,      # 文本块之间的重叠长度
    separators=["\n\n", "\n", " ", "，", "。", "  ","?","？","!","！",".","。",":"],  # 分割文本的分隔符列表
    length_function=len,    #计算文本长度的函数，默认为len(text)
)

split_docs = splititer.split_documents(documents)


print(len(split_docs))
for doc in split_docs:
    print(doc.page_content)
    print("==="*20)