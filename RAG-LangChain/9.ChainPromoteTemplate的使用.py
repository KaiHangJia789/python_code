from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi
chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("ai","你是一个诗人"),
        MessagesPlaceholder("history"),# 历史消息
        ("human","再来一首唐诗"),
    ]
)

history_data = [
    ("human","请写一首七言律诗"),
    ("ai","静夜思(李白)\n\n床前明月光,\n疑是地上霜,\n举头望明月,\n低头思故乡."),
    ("human","请写一首五言律诗"),
    ("ai","西风瘦马(唐·王安石)\n\n西风瘦马，一去不回。\n西风瘦马，一去不回。\n西风瘦马，一去不回。\n西风瘦马，一去不回。"),

]

#返回类型 StringPromptValue 需用to_string()方法转换为字符串
prompt_text = chat_prompt_template.invoke(input={"history":history_data}).to_string()

model = ChatTongyi(model="qwen3-max")

res = model.invoke(prompt_text)
print(res.content)
