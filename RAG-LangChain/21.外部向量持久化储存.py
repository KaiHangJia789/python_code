from langchain_chroma import Chroma#Chroma是一个基于向量数据库的文本检索库，可以用于存储和检索文本数据，支持多种向量化方法和相似度计算方式。
from langchain_community.embeddings import DashScopeEmbeddings#DashScopeEmbeddings是一个基于OpenAI的文本嵌入模型的实现，可以将文本转换为向量表示，适用于各种自然语言处理任务。
from langchain_community.document_loaders import CSVLoader#CSVLoader是一个用于加载CSV文件的文档加载器，可以将CSV文件中的数据转换为Document对象，方便后续的文本处理和分析。

# Chroma :向量数据库

vector_store = Chroma(
    collection_name="text_collection",#指定集合名称，默认为"text_collection"
    embedding_function=DashScopeEmbeddings(),#指定使用DashScopeEmbeddings作为文本嵌入模型
    persist_directory="./data/chroma_db",#指定Chroma数据库的持久化目录，默认为"./chroma_db"
)


loader = CSVLoader(
    file_path="data/info.csv",
    encoding='utf-8',#指定CSV文件的编码格式，默认为'utf-8'
    source_column="source",#指定CSV文件中作为文档来源的列名，默认为None
)

documents = loader.load()

#向量的存储,新增 删除 检索
vector_store.add_documents(
    documents=documents,#被添加的文档列表,类型为List[Document]
    ids = [f"doc_{i}" for i in range(1, len(documents)+1)]#文档的id列表,类型为List[str]
)

#删除 传入[id,id,...]
vector_store.delete(ids=["doc_1", "doc_2"])

#检索 返回类型为List[Tuple[str, float]]，其中每个元组包含一个文档ID和一个相似度分数
results = vector_store.similarity_search(
    "Python学起来不难", #查询文本
    k=2,                #返回的文档数量
    filter={"source": "黑马程序员"}#过滤条件，指定只检索来源为"黑马程序员"的文档
)

print(results)