import yaml
from loguru import logger
def initConfig():
    try:
        with open('application.yaml', 'r', encoding='utf-8') as f:
            config = yaml.load(f.read(), Loader=yaml.FullLoader)
    except:
        logger.error("配置文件读取失败")
    return config
config = initConfig()