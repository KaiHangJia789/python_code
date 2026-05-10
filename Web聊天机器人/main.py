# main.py
import os
import json
from dotenv import load_dotenv
import api

# 加载 .env 文件中的环境变量
load_dotenv()

def save_history(history, filename="chat_history.json"):
    """将对话历史保存到 JSON 文件"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
        print("对话历史已保存。")
    except Exception as e:
        print(f"保存历史失败: {e}")

def load_history(filename="chat_history.json"):
    """从 JSON 文件加载对话历史，若文件不存在则返回默认 system 消息"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            history = json.load(f)
        if isinstance(history, list) and len(history) > 0:
            print("已加载上次会话。")
            return history
        else:
            print("开启新对话。")
            return [{"role": "system", "content": "You are a helpful assistant"}]
    except FileNotFoundError:
        print("未找到历史文件，开启新对话。")
        return [{"role": "system", "content": "You are a helpful assistant"}]
    except Exception as e:
        print(f"加载历史失败: {e}，开启新对话。")
        return [{"role": "system", "content": "You are a helpful assistant"}]

def main():
    messages = load_history()
    print("开始对话：（输入 'exit' 退出）")

    while True:
        user_input = input("用户: ")
        if user_input.lower() == 'exit':
            print("已退出...")
            save_history(messages)
            break

        messages.append({"role": "user", "content": user_input})

        try:
            assistant_reply = api.get_chat_response(messages)
            print(f"AI助手: {assistant_reply}")
            messages.append({"role": "assistant", "content": assistant_reply})
        except Exception as e:
            print(f"发生错误: {e}")
            save_history(messages)
            break

if __name__ == "__main__":
    main()