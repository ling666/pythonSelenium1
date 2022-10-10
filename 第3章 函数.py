#def语句和参数
'''
def hello(name):  #使用def创建一个hello函数变元为name
    print('Hello' + name)

hello('宇铃')   #函数返回后就会把变量销毁
hello('小红')
'''

#返回值和return语句
'''
import random
def getEvaluate(evaluateMark):
    if evaluateMark == 1:
        return '非常不满意'
    elif evaluateMark ==2:
        return '不满意'
    elif evaluateMark ==3:
        return '满意'
    elif evaluateMark ==4:
        return '比较满意'
    elif evaluateMark ==5:
        return '满意'
    elif evaluateMark ==6:
        return '非常满意'
r = random.randint(1,6)
userEvaluate = getEvaluate(r)
print(r)
print(userEvaluate)
'''

#关键字参数和print()
#print()函数有可选的变元end和sep
'''
print('hello',end='')  #hello后面不再打印换行而是打印一个空的字符串
print('world')
print('cats','dogs','mice')
print('cats','dogs','mice',sep=',')
'''

#局部和全局作用域
'''
def spam():
    eggs = 3
    print(eggs)
spam()
'''
#全局变量可在局部作用域中读取
'''
def spam():
    eggs = 2
    print(eggs)
eggs1 = 8
spam()
print(eggs1)
'''
#global语句,在函数内可以使用global语句修改全局变量
'''
def spam():
    global eggs
    eggs = "spam"
eggs = 'global'
spam()
print(eggs)
'''
#不能在局部变量前使用变量，以下是错误代码
'''
def spam():
    print(eggs)
    eggs = 'spam'
eggs = 'global'
spam()
'''
#异常处理thy 和 except,可能出错的语句放在try子句中，如果发生错误，程序跳转到except子句开始处
'''
def spam(divideBy):
    return 42 / divideBy
try:
    print(spam(2))
    print(spam(4))
    print(spam(0))
    print(spam(6))
except ZeroDivisionError:
    print('some error')
'''

#输入验证
print('请输入')
try:
    userInput = int(input())
except ValueError:
    print('请输入一个整数')


