import openai
from config import config
from loguru import logger
openai.api_key = config['openai']['api_key']
chat_history = []


def sendMsg(text: str):
    global chat_history # 声明全局变量
    try:
        chat_history.append({"role":"user","content":text})
        chat_history=chat_history[-10:]
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a friendly and helpful teaching assistant. You explain concepts in great depth using simple terms, and you give examples to help people learn. At the end of each explanation, you ask a question to check for understanding"},
                {"role": "user", "content": chat_history}
            ],
            temperature=0.5,
        )
        answer = completion['choices'][0]['message']['content']
    except Exception as e:
        raise e
    chat_history.append({"role":"assistant","content":answer})
    return answer
def newChat():
    try:
        completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "你是一个友好而有帮助的助教。你用简单的语言深入地解释概念，并且给出例子来帮助人们学习。在每个解释的结尾，你会问一个问题来检查理解。"},
                ],
                temperature=0.5,
            )
        answer = completion['choices'][0]['message']['content']
    except Exception as e:
        raise e
    return answer