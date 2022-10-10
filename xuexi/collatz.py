def callatz(number):
    if number % 2 == 0:
        num = number // 2
        print(num)
    if number % 2 == 1:
        num = 3 * number + 1
        print(num)
    return num
print('请输入一个整数')
number = int(input())
try:
   while number !=1:
       number = callatz(number)
       continue
   print('done')
except:
    print('Error:Type error, int are allowed')