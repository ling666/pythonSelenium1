#列表下标取值
'''
spam = [['my','name','is','ling'],[10,18,20,23]]
print(spam[0])
print(spam[0][3]) #第一个下标表示哪个列表，第二个下标表示该列表中的值
print(spam[1][-1])  #-1下标表示列表中的倒数第一个值，-2表示倒数第2个值，以此类推
'''

#列表切片取值,取出来的值是一个列表，冒号坐标是开始值，冒号右边是列表的长度，不包含它。
# 省略左边默认从0开始，省略右边默认到结束
'''
spam = ['my','name','is','ling']
shuZi = [10,18,20,23]
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])
print(spam[:2])
print(spam[1:])
print(len(spam)) #len()返回列表中值的个数
spam[-1] = '小红'  #赋值改变列表里面的值
print(spam[-1])
heBing = spam + shuZi  #+号可以合并两个列表
print(heBing)
fuZhi = spam * 3  # *号可以实现复制
print(fuZhi)
print(spam[2])
del spam[2]  #del可以将列表指定的值删除，后面的值往前移
print(spam)
print(spam[2])
'''
#列表用于循环
'''
catName = []
while True:
    print('请输入你的第' + str(len(catName)+1) + '只猫的名字' )
    name = input()
    if name == ' ':
        break
    catName = catName + [name]
print('猫名单如下：')
for name in catName:
    print('  ' + name)
print('请输入你要找的猫名')
fineCatName = input()
if fineCatName not in name:
    print( fineCatName + '不在名单里面，请重新确认')
else:
    print(fineCatName + '在名单里面')
'''

'''
spam = ['my','name','is','ling']
for i in range(len(spam)):
    print('下标' + str(i) + '的值是' + spam[i])
'''
#多重赋值和增强赋值
'''
spam = [18,'女','ling']
age,xingBie,name = spam
print(name)
name += ' mo'
age -= 1
print(name)
print(age)
'''
#index()方法传入一个值，如果这个值存在在列表中，则返回他的下标；如果存在重复的值则返回第一次出现的下标；不存在则报错
#append()方法在列表末尾加上一个值，没有返回值
#insert()方法在列表插入一个值，没有返回值
#remove()方法可以相应的值，如果知道下标用del，知道值用remove
'''
spam = [18,'女','ling']
a = spam.index('ling')
print(a)
spam.append('本科')
print(spam)
spam.insert(1,'迈科')
print(spam)
spam.remove('迈科')
print(spam)
'''
#sort()方法对列表进行排序
'''
spam = [5,6,2,1,8,5]
spam.sort()
print(spam)
a = ['a','y','b','B','A']
a.sort()
print(a)
'''
#字符串也可以当做列表,可以对它取值等，但字符串不是可变数据类型，不能对它进行添加删除。修改
'''
name = 'ling'
for i in name:
    print(i)
print(name[-1])
'''
#元组，如果需要一个永远不变的值的序列就可以用元组，它和字符串一样可以取值，但不能修改、添加、删除
'''
apam = ('我','是','宇','铃')
oneYuanZu = ('一个元组',)  #这样表示这个是个元组，不加逗号Python会认为，你只是在普通括号里面输入一个值
newApam = apam[1]
print(newApam)
'''
#tuple()列表值得到元组形式,list()从元组值得到列表形式
'''
spam = [5,6,2,1,8,5]
lieBiao= tuple (spam)
apam = ('我','是','宇','铃')
yuanZu = list(apam)
print(lieBiao)
print(yuanZu)
'''
#引用,变量cheese只是引用了spam，所以当修改cheese时，就是修改原始列表
'''
spam = [5,6,2,1,8,5]
cheese = spam
cheese[1] = 'hello'
print(spam)
print(cheese)
'''

#传递引用,这时列表也会被引用
'''
def eggs (someParameter):
    someParameter.append('hello')
spam = [1,5,8,4,3]
eggs(spam)
print(spam)
'''
#copy()函数可以复制列表和字典，修改其值后，不会影响它原来的列表;copy.deepcopy()复制列表中包含的列表
'''
import copy
spam = [1,5,7,6,2]
cheese = copy.copy(spam)
cheese[1] = 'hello'
print(spam)
print(cheese)
'''
#练习2
'''
spam = [2,4,6,8,10]
spam[2] = 'hello'
print(spam)
'''
#练习3-5
'''
spam = ['a','b','c','d']
zhi = spam[int (int('3'*2)/11)]
print(zhi)
print(spam[-1])
print(spam[:2])
'''
#练习6-8
'''
bacon = [3.14,'cat',11,'cat',True]
zhi = bacon.index('cat')
print(zhi)
zhi1 = bacon.append(99)
print(bacon)
zhi2 =bacon.remove('cat')
print(bacon)
'''
#练习9
'''
spam = ['a','b','c','d']
bacon = [3.14,'cat',11,'cat',True]
a = list(spam)
b =list(bacon)
c = a + b
print(c)
d = spam * 2
print(d)
print(spam)
'''
#逗号代码
'''
def douHaoDaiMa (parameter):
    sum = ''
    for i in range(len(parameter) - 1):
        a = spam[i] + ','
        sum = sum + a
    sum1 = sum + 'and ' + parameter[-1]
    return sum1
spam = ['apples','bananas','tofu','cats']
zhi = douHaoDaiMa(spam)
print(zhi)
'''
#join()函数返回一个以分隔符sep连接各个元素后生成的字符串
# 语法：sep.join(seq)  sep是连接符，seq是要脸的元素序列、字符串、元组、字典
'''
spam = ['apples','bananas','tofu','cats']
def listStr(lst):
    return ','.join(lst[:-1] + [ 'and ' + lst[-1]])
zhi = listStr(spam)
print(zhi)
'''
#字符网格
grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]
#listLen = len(grid) #9
#listCol = len(grid[0]) #6
for i in range(len(grid[0])):
#    print(grid[i])
    for j in range(len(grid)):
        print(grid[j][i],end='')
    print()
