import os
from openai import OpenAI
import json


def save_history(history,filename = "chat_history.json"):
    #将对话历史保存到Json文件
    try:
        with open(filename,'w',encoding='utf-8') as f:
            json.dump(history,f,ensure_ascii=False,indent=2)
        print("对话历史以保存..")

    except Exception as e:
        print(f"保存历史失败:   {e}")


def load_history(filename="chat_history.json"):
    #从Json文件加载对话历史
    try:
        with open(filename,'r',encoding='utf-8')as f:
            history = json.load(f)
        if isinstance(history,list) and len(history) > 0:
            print("已加载上次会话。")
            return history

        else:
            print("开启新对话。")
            return [{"role":"system","content":"You are a helpful assistant"}]
    except FileExistsError:
        #文件不存在,返回默认system消息
        print("未找到历史文件,开启新对话")
        return [{"role":"system","content":"You are a helpful assistant"}]
    except Exception as e:
        print(f"加载历史失败:{e}, 开启新对话.")
        return [{"role":"system","content":"You are a helpful assistant"}]

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

#初始化消息历史
messages = load_history()   


print("开始对话:(输入'exit'退出)")
while True:
    #获取用户输入
    user_input = input("用户:   ")
    if user_input.lower() == 'exit':
        print("已退出...")
        save_history(messages)
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
        save_history(messages)
        break
