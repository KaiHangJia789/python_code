from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="RAG-LangChain\stu.csv",
    encoding="utf-8",
    csv_args={
        "delimiter": ",",  #指定分隔符
        "quotechar": '"',  #指定引用字符
        #如果数据有表头，就不要下面的代码
        "fieldnames":['a','b','c']  #指定表头
    },
)

#批量加载.loader.load() -> List[Document]
# documents = loader.load()

# for document in documents:
#     print(document)

#懒加载.loader.lazy_load() -> Iterable[Document]
for document in loader.lazy_load():
    print(document)