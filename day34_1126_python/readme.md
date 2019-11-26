# 模块
- 普通文件.py
    - 编写模块有如下内容
        - 函数(单一功能)
        - 类
        - 测试代码
- 模块名-->文件名
- import module_name
- 调用：　module_name.function_name
- 调用：　module_name.class_name
- import moudle_name as alias
- alias.fuction_name
- alias.class_name
- from module_name import func_name, class_name
- 调用：　fucnc_name
- 调用：　class_name
# 模块搜索路径和存储
- import sys
- sys.path 属性　搜索路径

# 包　
- .py文件的文件夹
    - 用来将模块包含在一起的文件夹就是包。
    - 自定义包的结构
    ```
    ---包package_name
        |----__init__.py 
        |---模块1
        |---模块2
        |----子包
              |---__init__.py
              |---模块1
              |---模块2
    ```
- 包的导入操作
    - import package_name 可以使用__init__.py中的内容
    - 调用 package_name.func_name
    - 调用　package_name.class_name.func_name()

    - import package_name.module常用写法 规避 __init__.py 模块
    - 使用方法：　package.module.func_name
    -           package.module.class_fun()
    -           package.module.class.var
    - from package_name import module  # 不执行 __init__.py
    -　使用方法; module.func_name()
    -           module.class_fun()
    -          module.class.var
    - from package import * 导入　__init__ 文件中所有函数和类
    - from package.module import *  导入包中指定模块的所有内容。
    - '__all__'的用法：
    - 在使用from package import *， * 可以导入的内容。

# 异常
- 异常：　语法与逻辑正确前提下，出现问题；偶然会出现问题，异常不可避免，例如读文件时候；
- 错误
- python  中　异常是一个类：　异常系统规定好的；可以处理和使用；
- 异常分类：　AssertError AttributeError EOFError IndexDrror KeyError NameError RuntimeError MemoryError  UnicodeEncodeError ValueError ZeroDivisionError......
- 异常处理
```
try:
    操作
except 异常类型1:
    解决方案
except 异常类型2:
    解决方案
else:
    如果没有出现异常，将会执行此处代码
finally:
    有没有异常都要执行代码
```

# 模块
# Django
- utf-8 编码 1******* 
            110***** 10******
            1110**** 10****** 10******
- django 1.8
- python 3.6
http://usyiyi.cn  yiyibooks.cn
- django架站16堂课






