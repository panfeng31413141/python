#数字
#int、float，除此之外还包括decimal、fraction、复数
print(2+2)
print(50-5*6)
print((50-5*6)/4)
print(8/5) # division always return a floating-point number
print(20/5)

print(17/3)
print(17//3)#//取整数
print(17%3)#%取余数

print(5**2)#幂次方，5的平方
print(2**7)#幂次方，2的7次方

width=20 #=等号给变量赋值
height=5*9
print(width*height)

print(4*3.75-1)#完全支持浮点，具有混合类型的运算符转为浮点数

tax=12.5/100
price=100.50
total=tax*price 
print(total)
print(price+total)#在python解释器，允许交互式输入，可以使用_引用上一个表达式的结果。在python命令行界面（CLI）,用于运行python脚本，_不会自动引用上一个表达式结果，需要使用变量赋值

#文本
print("spam eggs")
print('1975')
print("donsn\'t")#如果要添加引号，需要使用\转义它
print("\"yes,\"they said.")
print('"isn\'t,"they said.')

s="First line.\nSecond line."#\n断行
print(s)

print(r"c:\some\name")#不希望\开头的字符被解释成特殊字符，可以通过在引号前添加r来使用原始字符串

print("""
\            
usage:thingy[options]
    -h       display this usage message
    -H hostname   hostname to connect to
""")# 使用3个引号"""...""",实现字符串文字跨越多行????????????????????????????????????????????????????????

print(3*"un"+"ium")#使用+链接变量或变量和文字
print("py""thon")

text=("put several strings within parentheses"
      " to have them joined together")
print(text)

prefix="py"
print(prefix+"thon")#使用+链接变量或变量和文字

print(3*"un"+"ium")#使用+链接变量或变量和文字

word="python"
print(word[0])#索引字符串，第一个字符串为0
print(word[5])
print(word[-1])#索引字符串，负数从右边开始,注意负数索引从-1开始
print(word[-2])
print(word[-6])

print(word[2:5])#索引字符串切片。从第2（包括）到第5（不包括）
print(word[:2]+word[2:])#默认值：生用的第一个默认值为0，第二个默认值为字符串大小

s="supercalifragilisticexpialidocious"
print(len(s)) #返回字符串长度


#列表
squares=[1,4,9,16,25]
print(squares)
print(squares[0])#列表支持被索引
print(squares[-1])
print(squares[-3:])#列表支持被切片

print(squares+[36,49,64,81,100])#列表支持连接操作

cubes=[1,8,27,65,125]
cubes[3]=64#列表支持更改内容（字符串是不可变的）
print(cubes)

cubes.append(216)#注意这里使用点号.而不是·  #使用了list.append()方法在列表末尾添加新项目
cubes.append(7**3)
print(cubes)

rgb=["red","green","blue"]
rgba=rgb
print(id(rgb)==id(rgba))
rgba.append("alph")
print(rgb)

correct_rgba=rgba[:]
correct_rgba[-1]="alpha"
print(correct_rgba)
print(rgba)

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

letters=["a","b","c","d"]
len(letters)#len()函数

a=["a","b","c"]
n=[1,2,3]
x=[a,n]#可以嵌套列表
print(x)
print(x[0])
print(x[0][1])



#编程的第一步
#练习：编写斐波那契数列
a,b=0,1#元组解包
while a<1000:
    print(a,end=",")#关键字参数end可用于避免输出后的换行符
    a,b=b,a+b







#if条件语句
#for循环语句
#。。。。


#数据结构
#模型和包
#标准库library介绍


