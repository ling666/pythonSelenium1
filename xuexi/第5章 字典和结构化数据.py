# #字典用{}表示，里面由键值对组成，键值都可以是任意字符类型
# myCat = {'size':'fat','color':'gray',20:'loud','age':18}
# print(myCat['size'])
# print('my cat has ' + myCat['color'] + ' fur')
# print('my cat disposition is ' + myCat[20] )
# print('my cat age is ' + str(myCat['age']) )

# brithdays = {'小红':'12.1','小黄':'10.3','小绿':'8.6'}
# while True:
#     print('请输入你要查找的名字：')
#     name = input()
#     if name == '':
#         print('名字不能为空请重新输入')
#         continue
#     if name in brithdays:
#         print(brithdays[name] + ' 是' + name + '的生日')
#         break
#     else:
#         print('我没有关于' + name + '的信息')
#         print('他的生日是多少？')
#         bDays = input()
#         if bDays == '':
#             print('生日不能为空')
#         else:
#             brithdays[name] = bDays
#             print('生日数据更新成功')

#3个字典方法keys() values()  items() 可以返回dict_列表中的键、值、键值。字典里的值不能被修改。items()返回的是键值的元组列表
# dict.keys() dict.values() dict.item()可以用于for循环
# myCat = {'size':'fat','color':'gray',20:'loud','age':18}
# for i in myCat.keys():
#     print(i)
# print(myCat.items())
# print(myCat.keys())
# print(myCat.values())
# print(list(myCat.items())) #返回的dict_item值传递给list返回一个列表
#
# #多重赋值将键值赋值给不同的变量
# myCat = {'size':'fat','color':'gray',20:'loud','age':18}
# for i,j in myCat.items():
#     print('key: ' +str(i)  + ' value: ' + str(j))

#检查字典中是否存在键值
# myCat = {'size':'fat','color':'gray',20:'loud','age':18}
# if 'color' in myCat.keys():
#     print(myCat['color'])
# else:
#     print('color 不在字典里')
# if 'fatw' not in myCat.values():
#     print('yes')
# if 'age'  in myCat:
#     print('yes')

# #get()方法检查键不存在时返回备用值
# myCat = {'size':'fat','color':'gray'}
# print('我猫的颜色是' + myCat.get('color',0))
# print('我猫的name是' + myCat.get('name','Tom'))

#setdefault()方法，如果没有该键则给它默认值，存入字典中
# myCat = {'size':'fat','color':'gray'}
# print(myCat.setdefault('age',4))
# print(myCat.setdefault('age',5))
# print(myCat)

# #计算字符出现次数
# massage = 'It was a bright cold day in April, and clocks were striking thirteen.'
# count = {}
# for character in massage:
#     count.setdefault(character,0)
#     count[character] =count[character] + 1
# print(count)

# #漂亮的打印
# import pprint
# massage = 'It was a bright cold day in April, and clocks were striking thirteen.'
# count = {}
# for character in massage:
#     count.setdefault(character,0)
#     count[character] =count[character] + 1
# pprint.pprint(count)

# # #字棋盘
# theBoard = {'top-L':' ','top-M':' ','top-R':' ',
#             'mid-L':' ','mid-M':' ','mid-R':' ',
#             'low-L':' ','low-M':' ','low-R':' '
#             }
# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
# turn = 'X'
# for i in range(9):
#     printBoard(theBoard)
#     print('请输入' + turn + '棋的位置')
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = 'O'
#     else:
#         turn = 'X'
# printBoard(theBoard)

# #嵌套的字典和列表
# allGuests = {'小红':{'苹果':5,'香蕉':12},
#              '小芳':{'菠萝':1,'苹果':2},
#              '小熊':{'杯子':3,'菠萝':1}}
# def totaBrought(guests,item):
#     numBrought = 0
#     for k,v in guests.items():
#         numBrought = numBrought + v.get(item,0)
#     return numBrought
# print('东西数量如下:')
# print('苹果' + str(totaBrought(allGuests,'苹果')))
# print('香蕉' + str(totaBrought(allGuests,'香蕉')))
# print('菠萝' + str(totaBrought(allGuests,'菠萝')))
# print('杯子' + str(totaBrought(allGuests,'杯子')))

#练习
# spam = {'动物':'cat'}
# if 'cat' in spam:
#     spam['cat'] = '土豆'
# print(spam['cat'])

# spam = {'动物':'cat'}
# print(spam.get('cat','土豆'))
# print(spam)

# spam = {'动物':'cat'}
# print(spam.setdefault('cat','土豆'))
# print(spam)

#好玩游戏的物品清单
qingDan = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory():
    print('请输入你的物品：')
    wu = input()
    print('请输入你物品的数量：')
    shu = int(input())
    return wu,shu
wuPin = displayInventory()
print(wuPin)
