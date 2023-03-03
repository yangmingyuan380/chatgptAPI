import openai
from config import config
from loguru import logger
openai.api_key = config['openai']['api_key']
chat_history = []


def sendMsg(text: str):
    global chat_history # 声明全局变量
    try:
        chat_history.append("You: " + text)
        chat_history=chat_history[-10:]
        prompt="\n".join(chat_history)
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a friendly and helpful teaching assistant. You explain concepts in great depth using simple terms, and you give examples to help people learn. At the end of each explanation, you ask a question to check for understanding"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
        )
        message = completion['choices'][0]['message']['content']
    except Exception as e:
        raise e
    chat_history.append("Bot: " + message)
    return message
