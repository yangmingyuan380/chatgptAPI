from telegram.ext import Updater, CommandHandler,MessageHandler, Filters
import chatgpt
from config import config
from loguru import logger
def echo(update,mes):
    updateUserID = update.message.from_user.id
    TelegramIDs = config["tg"]["whiteID"]
    if len(TelegramIDs) != 0 and updateUserID in TelegramIDs:
        text = update.message.text
        try:
            ans = chatgpt.sendMsg(text)
        except Exception as e:
            ans = f"chatgpt出错：{e}"
        update.message.reply_text(text=ans)
    else:
        ans = f"用户 {updateUserID} 没有权限使用该机器人"
        update.message.reply_text(text=ans)
    
def start(update, context):
        update.message.reply_text('Hello World!')

def startBot():
    token = config['tg']['token']
    # 设置代理参数
    request_kwargs = {'proxy_url': 'socks5h://127.0.0.1:7890'}
    # 创建Updater对象
    try:
        updater = Updater(token=token, request_kwargs=request_kwargs) #
    except Exception as e:
         logger.error(f"创建tg机器人出错: {e}")  
    # 添加一个start命令的处理器
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
    # 启动轮询模式
    updater.start_polling()