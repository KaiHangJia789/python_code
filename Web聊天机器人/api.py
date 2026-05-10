# api.py
import os
from openai import OpenAI

def get_chat_response(messages):
    """
    发送消息列表给 DeepSeek API，返回助手的回复内容。
    """
    client = OpenAI(
        api_key=os.environ.get("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com"
    )
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        stream=False
    )
    return response.choices[0].message.content