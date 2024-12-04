#模块和包
#区别:
#模块:单个py文件,定义一些函数、类或者变量
#包:包含多个模块的目录结构,通常用于组织大型项目

#模块的类型三种
#1)自定义模块. 2)内置模块,例如python标准库中的match、sys. 3)第三方模块,例如numpy、pandas.

#模块的导入
import fibo#import命令直接导入模块
fibo.fib(1000)
print(fibo.fib(1000))
import fibo 
fibo.fib2(1000)
print(fibo.fib2(1000))

import fibo
fibo.__name__
print(fibo.__name__)

fib=fibo.fib#给导入的模块,分配本地名称,方便经常使用
fib(500)
print(fib(500))

from fibo import fib,fib2#导入特定的函数或类:只导入模块中特定的函数或类
print(fib(500))

import fibo as fib#重命名导入:给导入的模块或成员一个别名
fib.fib(500)
print(fib.fib(500))

from fibo import fib as fibonacci#导入特定的函数或类,并重命名
fibonacci(500)
print(fibonacci(1000))

#模块的搜索

help("modules")#help()函数显示关于python对象的信息,包括内置函数
print(help("modules"))

#内置模块:
#math数学函数
#random随机数生成
#datetime日期和时间
#json编码和解码
#sys系统相关参数和函数
#os和io操作系统接口和输入/输出
#re正则表达式
#collections容器数据类型
#heapq堆队列算法
#itertools迭代器工具
#...

import fibo,sys
dir(fibo)#dir()是内置函数,用于了解一个模块包含哪些内容
print(dir(fibo))

#包

# step1 创建包
#在终端中创建(或文件系统中),相关终端命令如下:
#1.打开终端或命令行
#2.cd导航到工作目录 例如:cd /users/xupanfeng/documents/python_base
#3.创建包的根目录 例如:mkdir my_package
#4.创建__init__.py文件 例如
#cd my_package#导航到根目录下
#touch __init__.py#创建__init__.py文件,注意空格
#5.创建module1.py文件 例如touch module1.py
#-----同样方法创建子包目录和子包文件(如下)------
#6.创建sub package子目录,例如:mkdir subpackage
#7.创建子包__init__.py文件 例如
#cd subpackage
#touch __init__.py
#8.创建module2.py文件 例如touch module2.py

# step2 添加模块
#在文本编辑器(例如vs code)编写代码,相关代码如下:
#文件module1.py
def greet(name):
    print(f"hello,{name}"!)
#文件module2.py
def welcome(name):
    print("welcome,{name}!")

# step3 使用包
#从包中导入/包内引用/安装包(在其他环境中想使用包)


#查看包的结构
#方法1:tree命令,例如在终端中输入 tree my_package
#方法2:ls命令,例如在终端中输入 ls -lR my_package
#更多方法,相见kimi













