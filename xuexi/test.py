#print 的用法

print('加油'+'老铁#') #字符串连接用+
print() #打印空行
print('加油'*5)  #字符串复制
print(5+1.3)  #整形和浮点型相加后是浮点型
print((40==40)and (5<6))


#input()函数
"""
ouXiangName = input()
print('我的偶像名字是'+ouXiangName)
"""

#len()函数 计算字符串的中的字符个数
'''
a = len('hello')
print(a)
'''

#str（）、int（）、float() 函数可以强制将变量值变为相应的数据类型
'''
a = str(29)
b = int(9.6)
c = float(10)
print('我今年'+a+'岁')
print(b)
print(c)
'''

#python内置函数 len()取长度，round()浮点数四舍五入
'''
a = len('hello')
print(a)
print("round (5.8685,2:)",round(5.8685,2))
'''

#if else 条件语句的使用
'''
print('请输入账号：')
name = input()
if name == '宇铃':
    print(name + '请输入你的密码：')
    password = input()
    if name == '宇铃'and password == 'myl':
        print('密码正确')
    else:
        print('密码错误')
else:
    print('账号错误')
'''
#elif 语句是“否则如果”，总是跟在if或另一条elif语句后面。
# 在前面的条件为False时检查该条件，最多只有一个子句会执行， 一旦为True，剩下的字句就会被跳过。
'''
print('请输入你的名字：')
name =input()
print('请输入你的年龄：')
age = input()
age = int(age)
if name == '宇铃':
    print('Hello 宇铃')
elif age > 80:
    print('你不是宇铃，奶奶')
elif age > 25:
    print('你不是宇铃，阿姨')
elif age > 18:
    print('你不是宇铃，小朋友')
else:           #每一个if、elif语句中的条件都为False时就执行
    print('你太小啦')
'''

#while 子句结束时，程序执行跳回到while语句开始处
'''
num =0;
while num <5:
    print('hello')
    num = num + 1
print('Thank you')
'''

#break 遇到break马上退出循环子句，用于循环内部。break只能用在while和for语句中
'''
while True:
    print('请输入你的名字')
    name = input()
    if name == '宇铃': #这个为False时跳过break语句，往后走，即回到了循环的首部
        break
print('Thank you')
'''

#continue 遇到continue马上跳回循环开始处，continue只能用在while和for语句中
'''
while True:
    print('请输入你的名字')
    name = input()
    if name != '宇铃':
        continue
    print('请输入你的密码')
    password = input()
    if password == 'myl':
        break
print('账号密码正确')
'''

#“类真”和“类假”的值。在用于条件时，0、0.0和''（空字符串）被认为是False，其他被认为是True
'''
name = ''
while not name:
    print('请输入你的名字')
    name = input()
print('你有多少位客人')
numOfGuests = int(input())
if numOfGuests:
    print('请确保所有客人都有自己的房间')
print('完成')
'''
#for 循环可以让代码块执行固定次数，一般用for i in range(5):
'''
print('你的名字是')
for i in range(5):
    print('宇铃 打印第'+ str(i) + '次')
'''

#for语句从1加到100
'''
sum = 0
for i in  range(101):
    sum = sum + i
print(sum)
'''
'''
sum = 0
i = 0
while i < 101:
    sum = sum + i
    i = i + 1
print(sum)
'''
#打印出43210
'''
for i in range(5,-1,-1):
    print(i)
'''

#import 导入模块可以导入一个可以导入多个用逗号隔开
'''
import random
for i in range(5):
    print(random.randint(2,15))
'''

#用sys.exit()提前结束程序
'''
import sys
while True:
    print('请输入:')
    response = input()
    if response == 'exit':
        sys.exit()
    print('你输入的是' + response)
'''

#第2章习题9
'''
print('请输入spam的值')
spam = int(input())
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greeting')
'''
#第2章习题13
'''
for i in range(1,11):
    print(i)
'''
'''
i = 1
while i>=1 and i<=10:
    print(i)
    i = i + 1
'''