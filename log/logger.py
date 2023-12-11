import logging

def log():
    # 创建日志器  这个日志器就写入了日志信息
    logger = logging.getLogger()
    # 设置日志级别
    logger.setLevel(logging.INFO)
    # 没有handlers处理器，执行if语句
    if not logger.handlers:
        # 控制台输出
        sh = logging.StreamHandler()
        # 将日志信息放入控制台
        logger.addHandler(sh)

        # 文件输出
        fh = logging.FileHandler('file.log', encoding='utf-8')
        # 把日志信息添加到文件中
        logger.addHandler(fh)

        # 设置格式  创建格式器
        fmt = '%(asctime)s|%(filename)s:%(lineno)d|%(funcName)s|[%(levelname)s]|%(message)s'
        formater1 = logging.Formatter(fmt)

        # 给控制台加格式
        sh.setFormatter(formater1)
        # 给日志文件加格式
        fh.setFormatter(formater1)
    return logger

