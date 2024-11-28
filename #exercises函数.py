#函数

#定义一个带参数的函数
def fib(n):#def 定义了一个名叫fib（n）的函数，参数n
    """print a fibonacci series less than n."""#函数文档字符串，描述函数功能
    a,b=0,1#初始化两个变量，赋值0，1
    while a<n:#只要a<n,执行循环
        print(a,end=" ")#设置end=" ",数字之间用空格隔开
        a,b=b,a+b
    print()#打印一个空行,以便后续输出不会连在一起
#调用函数    
fib(2000)
fib(3000)

#定义一个不带参数的函数
def greeting():
    """"return a greeting message."""
    return "Hello,World!"
print(greeting())



fib#显示fib的定义信息
f=fib#将函数赋值给变量f
f(100)

fib(0)#没有返回值
print(fib(0))#返回"none"


def fib2(n):
    """"return a list containing the fibonacci series up to n."""
    result=[]
    a,b=0,1
    while a<n:
        result.append(a)
        a,b=b,a+b
    return result#return语句返回函数的值
print(fib2(100))#在 Python 中，函数调用会执行函数体中的代码并返回结果，但除非你显式地打印这个结果，否则你不会在控制台上看到任何输出。因此，这里需要print语句

#理解默认参数，看不懂？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？/
def ask_ok(prompt,retries=4,reminder="please try again!"):
    while True:
        reply=input(prompt)
        if reply in {"y","ye","yes"}:
            return True
        if reply in {"n","no","nop","nope"}:
            return False
        retries=retries - 1
        if retries<0:
            raise ValueError("invalid user response")
        print(reminder)


#换个姿势再次理解默认参数
def greet(name,message="hello"):#作用：在调用函数时如果省略了该函数，会自动使用默认函数
    print(f"{message},{name}!")
greet("alice")
greet("bob","goodbye")


i=5
def f(arg=i):#默认函数只在函数定义时计算一次，一次这里默认参数设定为初始5，后面在调用的时候使用6不会产生影响
    print(arg)
i=6
f()

#默认参数的副作用
def f(a,L=[]):#副作用->使用可变对象（例如列表）作为默认参数时，注意默认参数只在函数定义时被评估一次，而不是每次调用时
    L.append(a)
    return L

print(f(1))#默认参数被定义a=1,L=[1],在这之后的调用中不会改变
print(f(2))
print(f(3))

#策略：将默认参数设置为none，在函数体内部检查并初始化它
def f(a,L=None):
    if L is None:#在函数体内部检查并初始化它
        L=[]
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))


#关键字参数
def parrot(voltage,state="a stiff",action="voom",type="norwegian blue"):
    print("-- this parrot wouldn't",action,end=" ")
    print("if you put",voltage,"volts through it.")
    print("lovely plumage,the",type)
    print("-- it's",state,"!")
#调用函数
parrot(1000)
parrot(voltage=1000)#位置参数
parrot(voltage=1000,action="v00000m")#2个关键字参数
parrot(action="v00000m",voltage=10000)#2个关键字参数
parrot("a million","bereft of life","jumpt")#位置参数
parrot("a thousand",state="pushing up the daisies")#1个位置参数+1个关键字参数；关键字参数必须在位置参数之后！！！

# *args 允许函数接受任意数量的位置参数 *kwargs 允许函数接受任意数量的关键字参数
#模拟了奶酪店场景，顾客询问是否有奶酪，店员回复，并附上了更多信息
def cheeseshop(kind,*arguments,**keywords):#*args 允许函数接受任意数量的位置参数 *kwargs 允许函数接受任意数量的关键字参数
    print("--do you have any",kind,"?")
    print("--i'm sorry,we're all out of",kind)
    for arg in arguments:#遍历所有位置参数，并打印每个参数。aruments是一个元祖，包含了所有传递给函数的位置参数（不包括kind）
        print(arg)
    print("-"*40)
    for kw in keywords:#遍历所有关键字参数，并打印每个键及对应的值。keywords是一个字典，包含所有传递给函数的关键字参数。
        print(kw,":",keywords[kw])
#调用函数
cheeseshop("limburger","it's very runny, sir.","it's really very,very runny,sir.",shopkeeper="jonhn cleese",client="john cleese",sketch="cheese shop sketch")


#仅位置参数和仅关键字参数
def standard_arg(arg):
    print(arg)
    return""

def pos_only_arg(arg,/):#仅位置参数
    print(arg)
    return""

def kwd_only_arg(*,arg):#仅关键字参数
    print(arg)
    return""

def combined_example(pos_only,/,standard,*,kwd_only):#混合参数
    print(pos_only,standard,kwd_only)
    return""
#调用函数
print(standard_arg(2))#使用位置参数调用
print(standard_arg(arg=2))#使用关键字参数调用

print(pos_only_arg(1))

print(kwd_only_arg(arg=3))

print(combined_example(1,2,kwd_only=3))
print(combined_example(1,standard=2,kwd_only=3))

#任意参数列表
def concat(*args,sep="/"):
    return sep.join(args)#字符串join（）方法，详见kimi
#调用函数
print(concat("earch","mars","venus"))
print(concat("earth","mars","venus",sep="."))

#解压参数列表
list(range(3,6))
args=[3,6]
print(list(range(*args)))

#文档字符串
def my_function():
    """"Do nothing,but document it.
    
    No,really,it doesn't do anything.
    """
    pass
print(my_function.__doc__)#注意下划线书写规范


#函数注释
def f(ham:str,egg:str="egggs") -> str:
    print("annotations:",f_annotations_)


#编码风格
参考网站https://peps.python.org/pep-0008/



#使用内置函数len() max() min() match() random()
#函数的高级特性，例如lambda函数、函数装饰器
