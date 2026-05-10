from langchain_core.vectorstores import InMemoryVectorStore#内存向量存储
from langchain_community.embeddings import DashScopeEmbeddings#DashScopeEmbeddings是一个基于OpenAI的文本嵌入模型的实现，可以将文本转换为向量表示，适用于各种自然语言处理任务。
from langchain_community.document_loaders import CSVLoader#CSVLoader是一个用于加载CSV文件的文档加载器，可以将CSV文件中的数据转换为Document对象，方便后续的文本处理和分析。

vector_store = InMemoryVectorStore(
    embedding=DashScopeEmbeddings(),#指定使用DashScopeEmbeddings作为文本嵌入模型
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
)

print(results)