import tg
from loguru import logger
if __name__=="__main__":
    logger.add("my_log_file.log")
    tg.startBot()