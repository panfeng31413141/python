#数据结构

#列表list
#栈stack
#队列queue
#del语句
#元组tuple
#集合set
#字典dictionnary
#字符串string

#关于列表的一些方法
fruits=["orange","apple","pear","banana","kiwi","apple","banana"]
fruits.count("apple")#list.count(x)列表计数，返回x在列表中出现的次数
print(fruits.count("apple"))

fruits.index("banana")#list.index(x)列表索引，返回x在列表中第一次出现的索引位置
print(fruits.index("banana"))
fruits.index("banana",4)#list.index(x,start,end)列表索引，从start开始所以，到end结束，x在列表中出现的索引位置
print(fruits.index("banana",4))

fruits.reverse()#将列表中的元素反转
print(fruits)

fruits.sort()#list.sort()列表排序，对列表中的项目进行排序
print(fruits)

fruits.append("grape")#list.append(x)列表追加，将x追加到列表末尾
print(fruits)

fruits.extend(["mango","grape"])#list.extend()列表拓展，将一个可迭代对象的所有元素添加到列表末尾
print(fruits.extend(["mango","grape"]))

fruits.insert(2,"cherry")#list.insert(i,x)用于在列表中i位置插入元素x
print(fruits.insert(2,"cherry"))

fruits.remove("apple")#list.remove(x)移除列表中第一个匹配的元素x
print(fruits.remove("apple"))

fruits.pop()#list.pop移除列表中最后一个元素,并将其返回
print(fruits.pop())

fruits_copy=fruits.copy()#列表复制，用于返回列表的一个浅拷贝
print(fruits_copy)

fruits.clear()#清空列表中所有元素
print(fruits)

#复习列表数据结构
squares=[1,4,9,16,25]
print(squares[0])#列表支持被索引
print(squares[-3:])#列表支持被切片

print(squares+[36,49,64,81,100])#列表支持连接操作

cubes=[1,8,27,65,125]
cubes[3]=64#列表支持更改内容（字符串是不可变的）
print(cubes)

letters=["a","b","c","d","e","f","g"]
print(letters)
#replace some values
letters[2:5]=["C","D","E"]
print(letters)
#remove them
letters[2:5]=[]
print(letters)
#clear the list by replacing all the elements with an empty list
letters[:]=[]
print(letters)

a=["a","b","c"]
n=[1,2,3]
x=[a,n]#可以嵌套列表

#stack
#stack是一种后进先出的数据结构，遵循特定的顺序添加和删除元素。下面举例使用列表作为stack栈
stack=[3,4,5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack.pop())
stack.pop()
print(stack.pop())
print(stack)

#queues队列
#列表推导式
#嵌套列表推导式
#del语句

#tuples元组
#元组提供不可变的数据集合，与列表的区别，相见kimi
t=12345,54321,"hello"#定义了一个元组，元组打包
print(t[0])

u=t,(1,2,3,4,5)#元组可以嵌套
print(u)

v=([1,2,3],[3,2,1])
print(v)

empty=()#定义了一个空元组
singleton="hello",#定义只有1个项目的元组，注意末尾有个逗号
print(len(empty))
print(len(singleton))

t=12345,54321,"hello"#元组打包
x,y,z=t#序列解包，适用于右侧的任何序列
print(t)

#sets
#集合是无重复、无序的元素集合.
basket={"apple","orange","apple","pear","orange","banana"}#创建一个set
print(basket)

"orange"in basket#fast memebership testing
print("orange"in basket)

"crabgrass"in basket#fast memebership testing
print("crabgrass"in basket)

a=set("abracadabra")#使用set()函数,将一个可迭代对象转化为set集,它会创建一个包含所有唯一字符串的集合
b=set("alacazam")
print(a)
print(b)
print(a-b)#差集,letters in a but not in b
print(a|b)#并集,letters in a or b or both
print(a&b)#交集,letters in both a and b
print(a^b)#对成集,letters in a or b but not both
#介绍python中集合运算:
#差集,符号-,a-b,letters in a but not in b
#并集,符号|,a|b,letters in a or b or both
#交集,符号&,a&b,letters in both a and b
#对称集,符号^,a^b,letters in a or b but not both

a={x for x in "abracadabra" if x not in "abc"}#支持set推导式,同列表推导式
print(a)

#dictionary字典
#字典的主要操作是存储带有某个键的值并提取给定键的值.
tel={"jack":4098,"sape":4139}#创建一个字典
tel["guido"]=4127#在字典中添加键值对,在字典tel中添加一堆新的键值对"guido":4127
print(tel)

del tel["sape"]#使用del删除键值对
tel["irv"]=4127
print(tel)

list(tel)#使用list返回所有键的列表

sorted(tel)#sorted()函数会根据字典的键来排序

"guido" in tel
print("guido" in tel)
"jack" not in tel
print("jack" not in tel)

dict([("sape",4139),("guido",4127),("jack",4098)])#使用dict()函数,从键值对序列构建字典
print(dict([("sape",4139),("guido",4127),("jack",4098)]))

dict(sape=4193,guido=4127,jack=4098)
print(dict(sape=4193,guido=4127,jack=4098))#当键是简单字符串时,使用关键字参数指定的方式

#strings字符串
#quenues队列
