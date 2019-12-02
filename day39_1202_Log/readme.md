# LOG
# 关键信息：
- 不同用户关注不同程序信息：
- DEBUG  INFO NOTICE WARNING ERROR CRITICAL ALERT EMERGENCY
- 日志信息：
    - time
    - 地点
    - level
    - info
    - 内容
- 第三方： logging
- 日志级别： 
    - 级别可自己定义：
    - 单例模式：
    - logging封装了其他组件；logging四大组件直接定制
- logging模块级别日志
    - logging.debug(msg,*args,**kwargs)
    - logging.info()
    - logging.waringin()
    - logging.error()
    - logging.critical()
    - logging.log(level,*args,**kwargs)
    - logging.basicConfig(**kwargs)
- logging.basicConfig(**kwargs) 对root logger 进行一次性配置。
    - 不配置logger 使用默认值
        - 输出 sys.stderr
        - 级别： WARNING
        - 格式： level:log_name:content
- logging模块处理流程 
- 四大组件
    - Logger 产生日志
    - Handler 把产生日志发送到相应的目的地
    - Filter 更精细控制控制日志输出
    - Formatter 格式器
-  Logger:
    - 产生一个日志 :
        - Logger.setLevel()
        - logger.addHandler()
        - logger.addFilter()
        - logger.debug() 产生一条debug级别日志,info error
        - logger.log()
        - logger.exception()
    - 得到一个logger对象
        - 实例化
        - logging.getLogger()
    - Handler 把log发送到指定位置
        - 方法： 
            - setLevel
            - setFormat
            - addFilter, removeFilter
        - 不需要直接使用，Handler是基类
            - logging.StreamHandler
            - logging.FileHandler
            - logging.handlers.RotatingFileHandler
            - logging.handlers.TimedRotatingFileHandler
            - logging.handlers.HTTPHandler
            - logging.handlers.SMTPHandler
            - logging.NullHandler
    - Format类
        - fmt
        - datefmt
        - style
    - Filter类：
        - 可以被Handler Logger使用。


# 打招呼 
```
- Hi/ Hi
- How are you doing?/ How's it going?
- Hey,what's up?
    - 生活如何 How's
        - How's everying?               - I'm doing great              
        - How's life?                   - They are doing great
        - How's your family?            - Pretty good
        - How's your job?
        - How are your parents?
    - 花式搭讪
        - 称赞
            - Wow I really love your ......
                -Skirt Coat Shoes Hairstyle
            - Wow,that's a really cool.....
                - Camera Phone Jacket
            - 夸中文
                - Excuse me, I just heard you speaking Chinese, you are pretty good!
            - 公交车， 咖啡店
                - Excuse me, is anyone sitting here?
                - Excuse me, is this seat taken?
            - 咖啡店
                - This place is pretty cool. Do you come here often?
            - 火车站
                - Do you need a hand?
    - 自我介绍
        - Hi, nice to meet you , I'm Chris
        - I'm Chris.
        - My name is Chris.
        - 正式场合
            - Allow me to introduce myself. I'm Chris.
            - This is my business card.
        - 久仰大名
            - I have heard a lot of things about you .
            - Chris has told me all about you。
    - 回应对方自我介绍
        - I would like you to meet a freind of mine.
        - Let me introduce you to my frind Li Ning.
        - This is Li Ning, Li Ning,Chris.
    - 问对方名字
        - Excuse me, but I don't think I know your name.
        - I am sorry, bu I don't believe I know your name.
        - I'm so sorry.Could you tell me your name again?
        - nice to meet you 
        - pleased to meet you
    - 接下去问
        - So, have you lived here long?
        - Have you worked here long?
        - Do you live around here?
        - Do you come here often?
        - So , what do you do, if you don't mind me asking?
        - So what exactly is it that you do ?
        - So what do you do for a living ?
        - Can I ask you what you do ?
    - So, how did you end up in China? 为什么来中国
    - Are you used to the life in China?
    - What places have you visited in China?
    - What is your favourite city in China?
    - What do you think of China/Chinese food?
    ```
    
```



    

