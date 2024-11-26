#循环语句
#while语句
a,b=0,1
while a<100:
    print(a,end=",")
    a,b=b,a+b

count=0
while count<5:
    print(count)
    count+=1#+=为运算符，使用kimi查看更多运算符用法

count=0
while count<5:
    print(count)
    count+=1
    if count>=5:
        break#使用break退出循环

count=0
while count<5:
    count+=1
    if count%2==0:
        continue#使用continue跳过迭代，直接进入下一次循环
    print(count)


#for语句
words=["cat","window","defenstrate"]
for w in words:#for语句
    print(w,len(w))


users={"hans":"active","eleonore":"inactive","景太郎":"active"}#创建了一个字典，将其赋值给一个名为users的变量
#策略一：迭代 ?????????????????????????????????????????????????????????????????????????????????????????
for user,status in users.copy().items():
    if status=="inactive":
        del users[user]
#策略二：新建 ?????????????????????????????????????????????????????????????????????????????????????????
active_users={}
for user,status in users.items():
    if status=="active":
        active_users[user]=status


       
#break语句，用于打破while或for循环
for n in range(2,10):
    for x in range(2,n):
        if n % x==0:
            print(f"{n}equals{x}*{n//x}")#f-string格式化字符串字面量
            break




#continue语句，用于继续循环的下一次迭代
for num in range(2,10):
    if num%2==0:
        print(f"find an even number{num}")#even number偶数
        continue
    print(f"find an odd number{num}")#odd number奇数




#else语句
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,"equals",x,"*",n//x)
            break
        else:
            print(n,"is a prime number")#prime number素数，参考kimi





#条件语句
#if-elif-else语句
age=17
if age>=18:
    print("you are an adult")#if语句注意缩进，一般缩进4个字符
else:
    print("you are not an adult")


score=85
if score>=90:
    print("A")
elif score>=80:
    print("B")
else:
    print("C")


x=int(input("please enter an integer:"))#使用了函数input（）“提示用户输入一个整数”和函数int（），将输入的字符串转换为整数，并将赋值给变量x
if x<0:
    x=0#如果输入的数字为负数小于0，则复制为零，同时展示下一行代码提示的内容“negative changed to zero”
    print("negative changed to zero")
elif x==0:
    print("zero")#如果输入的数字是0，展示“zero”
elif x==1:
    print("single")#如果输入的数字为1，展示“single”
else:
    print("more")#如果都不是，则展示“more”




#pass语句
while true:
    pass#pass   是一个空操作语句，表示不做任何事情




