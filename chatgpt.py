import openai
from config import config
openai.api_key = config['openai']['api_key']
def sendMsg(text:str):
    try:
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": text}]
        )
        return completion['choices'][0]['message']['content']
    except Exception as e:
        raise e
    