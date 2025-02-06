from loguru import logger
import sys
from config import settings

def init_logger():
    log_level = settings.get("log.level", "INFO")
    log_file = settings.get("log.logfile", "/tmp/money_controller.log")

    logger.remove()

    logger.add(sys.stdout, level=log_level, format="{time} | {level} | {message}")

    logger.add(log_file, level=log_level, format="{time} | {level} | {message}", rotation="1 week")
    
    return logger