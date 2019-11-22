# https://www.cnblogs.com/yyds/p/6901864.html
# logging
# logging 模块提供模块基本函数记录日志
# 四大组件：
# 日志：记录关键信息，
# 日志级别：(level) 不同用户关注不同程序信息
#   - DEBUG INFO NOTICE WARNING ERROR CRITICAL ALERT EMERGENCY
# I/O操作：　不要太频繁
# LOG作用：调试，了解软件运行情况；分析定位问题
# 日志：　time 地点 level 内容
# Logging :单例模式；只有一个日志在工作。
# logging.basicConfig(**kwargs) 进行配置　只在第一次调用时候起作用；
# 不配置logger使用默认:sys.stderr 级别 WARNING 格式：level :log_name:content

import logging
# 定义自己的输出格式：
LOG_FORMAT = '%(asctime)s ===%(levelname)s+++  %(message)s'
# fromat　参数
#配置
logging.basicConfig(filename ='tuling.log',level=logging.DEBUG,format=LOG_FORMAT)

# 方式一

logging.debug('This is a debug log.')
logging.info('This is a info log.')
logging.warning('This is a warning log.')
logging.error('This is a error log.')
logging.critical('This is a criticallog')

#方式二

logging.log(logging.DEBUG,'This is a debug log.')
logging.log(logging.INFO,'This is a info log.')
logging.log(logging.WARNING,'This is a warning log.')
logging.log(logging.ERROR,'This is a error log.')
logging.log(logging.CRITICAL,'This is a critical log.')
