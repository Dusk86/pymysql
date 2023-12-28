import logging
import time
import os

# def log(message):
#     # 创建日志器
#     logger = logging.getLogger()
#     # 控制台输出
#     streamhandler = logging.StreamHandler()
#     # 文件输出
#     filehandler = logging.FileHandler('log1.txt', encoding='utf-8')
#     # 设置控制台输出级别
#     streamhandler.setLevel(logging.INFO)
#     # 设置文件输出级别
#     filehandler.setLevel(logging.INFO)
#     # 设置输出格式
#     formatter = logging.Formatter('%(asctime)s -%(filename)s:%(lineno)d -%(funcName)s -[%(levelname)s] -%(message)s')
#     # 给控制台加格式
#     streamhandler.setFormatter(formatter)
#     # 给日志文件加格式
#     filehandler.setFormatter(formatter)
#     # 控制台添加日志
#     logger.addHandler(streamhandler)
#     # 文件添加日志
#     logger.addHandler(filehandler)
#     #
#     logger.info(message)

    # logger.removeHandler(filehandler)
    # logger.removeHandler(streamhandler)

# def log(message):
#     logger = logging.getLogger('testlog')
#
#     #  这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
#     if logger.handlers:
#         streamhandler = logging.StreamHandler()
#         streamhandler.setLevel(logging.ERROR)
#         formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
#         streamhandler.setFormatter(formatter)
#         logger.addHandler(streamhandler)
#
#     logger.info(message)


# class Log(object):
#     # 初始化
#     def __init__(self):
#         # 创建格式器并配置
#         allformatter = logging.Formatter('%(asctime)s -%(filename)s:%(lineno)d -%(funcName)s -[%(levelname)s] -%(message)s')
#         # 控制台输出
#         self.streamhandler= logging.StreamHandler()
#         # 给控制台加格式
#         self.streamhandler.setFormatter(allformatter)
#         # 创建日志
#         self.logger = logging.getLogger()
#         # 输出级别
#         self.logger.setLevel(logging.INFO)
#         # 控制台添加日志
#         self.logger.addHandler(self.streamhandler)
#
#     def debug(self, message):
#         logging.debug(message)
#     def info(self, message):
#         logging.info(message)
#     def warning(self, message):
#         logging.warning(message)
#     def error(self, message):
#         logging.error(message)
#     def critical(self, message):
#         logging.critical(message)
#
# loggingV2 = Log()


# class Log(object):
#     # 初始化
#     def __init__(self):
#         # 创建日志
#         self.logger = logging.getLogger()
#         # 创建格式
#         formatter = logging.Formatter('%(asctime)s -%(filename)s:%(lineno)d -%(funcName)s -[%(levelname)s] -%(message)s')
#         # 创建handler，写入日志文件
#         filehandler = logging.FileHandler('log1.txt', encoding='utf-8') # 文件路径
#         filehandler.setLevel(logging.INFO) # 文件输出等级
#         filehandler.setFormatter(formatter) # 文件输出格式
#         self.logger.addHandler(filehandler) # 给logger添加handler
#         # 创建handler，输出到控制台
#         consolehandler = logging.StreamHandler()
#         consolehandler.setLevel(logging.INFO) # 输出等级
#         consolehandler.setFormatter(formatter) # 输出格式
#         self.logger.addHandler(consolehandler) # 添加handler
#
#     def getlog(self):
#         return self.logger
#
# # 实例化 log
# concurrent_logger = Log()

def Log():
    # 判断有没有logging.root.handlers，有的话就全部pop，然后新添
    while len(logging.root.handlers) > 0:
        logging.root.handlers.pop()
    # 创建日志器  这个日志器就写入了日志信息
    logger = logging.getLogger()
    # 显示日志信息全面 设置日志级别
    logger.setLevel(logging.INFO)
    # 如果没有handlers处理器，才会执行下面语句
    # 需要控制台处理器
    sh = logging.StreamHandler()
    # 日志信息放入控制台中
    logger.addHandler(sh)

    # 保存在文件中 文件处理器
    fh = logging.FileHandler('log1.txt', encoding='utf-8')
    # 把日志信息添加到文件中去
    logger.addHandler(fh)

    # 日志比较丑，设置格式  创建格式器
    fmt = '%(asctime)s -%(filename)s:%(lineno)d -%(funcName)s -[%(levelname)s] -%(message)s'
    formater1 = logging.Formatter(fmt)

    # 给控制台加格式
    sh.setFormatter(formater1)
    # 给日志文件处理器加格式
    fh.setFormatter(formater1)
    return logger

































