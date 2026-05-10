import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

#初始化消息历史
messages = [
    {'role':"system","content":"You are a helpful assistant"}
        ]

print("开始对话:(输入'exit'退出)")
while True:
    #获取用户输入
    user_input = input("用户:   ")
    if user_input.lower() == 'exit':
        print("已退出...")
        break

    #将用户的消息加入历史
    messages.append({"role":"user","content":user_input})

    #调用   API
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",  
            messages=messages,
            stream=False
        )

        #提取助手回复
        assistant_reply = response.choices[0].message.content
        print(f"AI助手: {assistant_reply}")

        #将AI助手回复加入历史
        messages.append({"role":"assistant","content":assistant_reply})
    except Exception as e:
        print(f"发生错误:   {e}")
        break
