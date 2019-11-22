# logging模块处理流程
# 四大组件
# 日志器(Logger)：产生日志的一个接口
# 处理器(Handler):把产生的日志发送到相应的目的地
# 过滤器（Filter):更精细控制日志输出
# 格式器（Formatter)：对输出信息进行格式化
# 产生一个日志 Logger:  如何得到 logging.getLogger()
# setLever()
# addHandler() removeHandler()
# addFilter() removeFilter()
# debug();产生一条debug日志，同理 info error
# Handler 把log发送到指定位置
# Handler.setLevel setFormat addFilter removeFilter
# 基类：子类：StreamHandler FileHandler HTTPHandler SMTPHandler NullHandler RotatingFileHandler 
# TimedRotatingFileHandler
import logging
import logging.handlers
import datetime

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler('all.log',when='midnight',interval=1,backupCount=7)
rf_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s -%(filename)s[:%(lineno)d]-%(message)s)'))

logger.addHandler(rf_handler)
logger.addHandler(f_handler)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('Error message')
logger.critical('Critical message')