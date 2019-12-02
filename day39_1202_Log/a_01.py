import logging

# logging.debug('This is a debug log')
# logging.info('Info log')
# logging.error(' Thi is a error log')

# logging.log(logging.DEBUG,'This is a debug log.')
# logging.log(logging.CRITICAL,'This is a critical log')


# 配置
# 输出格式
LOG_FORMAT = '%(asctime)s------%(levelname)s------%(message)s'

logging.basicConfig(level='DEBUG',filename='logging.log',format=LOG_FORMAT)
logging.debug('This is a debug log')
logging.info('Info log')
logging.error(' Thi is a error log')

logging.log(logging.DEBUG,'This is a debug log.')
logging.log(logging.CRITICAL,'This is a critical log')

# filename  Specifies that a FileHandler be created, using the specified
#               filename, rather than a StreamHandler.
#     filemode  Specifies the mode to open the file, if filename is specified
#               (if filemode is unspecified, it defaults to 'a').
#     format    Use the specified format string for the handler.
#     datefmt   Use the specified date/time format.
#     style     If a format string is specified, use this to specify the
#               type of format string (possible values '%', '{', '$', for
#               %-formatting, :meth:`str.format` and :class:`string.Template`
#               - defaults to '%').
#     level     Set the root logger level to the specified level.
#     stream    Use the specified stream to initialize the StreamHandler. Note
#               that this argument is incompatible with 'filename' - if both
#               are present, 'stream' is ignored.
#     handlers  If specified, this should be an iterable of already created
#               handlers, which will be added to the root handler. Any handler
#               in the list which does not have a formatter assigned will be
#               assigned the formatter created in this function.

