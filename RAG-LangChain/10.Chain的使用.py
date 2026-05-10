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

model = ChatTongyi(model="qwen3-max")

# 创建链,要求每一个组件都是Runnable的接口的子类
chain = chat_prompt_template | model

#通过链去调用invoke或stream
# res = chain.invoke({"history":history_data})
# print(res.content)

# 通过链去调用stream
res_2 = chain.stream({"history":history_data})
for r in res_2:
    print(r.content,end="",flush=True) 