from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path=r"data/第一阶段2.pdf",
    mode = 'page',#默认是Page模式，每一页面形成一个Document对象，设置为'element'则每个元素形成一个Document对象
                    #single则将整个PDF文件作为一个Document对象
    password=None   #password为PDF文件的密码，默认为None
)

i = 0
for doc in loader.lazy_load():
    i+=1
    print(doc)
    print(f"总共加载了{i}个Document对象")