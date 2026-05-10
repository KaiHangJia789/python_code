from langchain_community.document_loaders import JSONLoader

loader = JSONLoader(
    file_path=".\data\stu_lines.json",
    jq_schema=".name",  #指定jq表达式，提取需要的字段
    text_content=False,  #是否将提取的字段作为文本内容
    json_lines=True,  #是否是独立的json对象
)

doucments = loader.load()

print(doucments)