import logging
import time
import os

def Log():
    # 判断有没有logging.root.handlers，有的话就全部pop，然后新添
    while len(logging.root.handlers) > 0:
        logging.root.handlers.pop()
    # 创建日志器  这个日志器就写入了日志信息
    logger = logging.getLogger()
    # 显示日志信息全面 设置日志级别
    logger.setLevel(logging.INFO)
    # 控制台输出
    sh = logging.StreamHandler()
    # 日志信息放入控制台中
    logger.addHandler(sh)
    # 保存在文件中 文件处理器
    fh = logging.FileHandler('log1.txt', encoding='utf-8')
    # 把日志信息添加到文件中去
    logger.addHandler(fh)

    # 设置输出格式
    fmt = '%(asctime)s -%(filename)s:%(lineno)d -%(funcName)s -[%(levelname)s] -%(message)s'
    # formatter设置日志格式
    formater1 = logging.Formatter(fmt)

    # 给控制台加格式
    sh.setFormatter(formater1)
    # 给日志文件处理器加格式
    fh.setFormatter(formater1)
    return logger

































