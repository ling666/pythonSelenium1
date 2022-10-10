#给用户猜一个数字，用户输入时提示用户高了还是低了
import random

trueNumber = random.randint(1,100)
print(trueNumber)
xiaoLastNum = 1
daLastNum = 100
shengYuTime =6
for guessTime in range(6):
    print('你还有' + str(shengYuTime) +'次机会，请你猜一个数字')
    guessNumber = int(input())
    shengYuTime = shengYuTime -1
    if guessNumber < trueNumber:
        print('正确数字在' + str(guessNumber) + '到'+ str(daLastNum) + '之间')
        xiaoLastNum = guessNumber
    elif guessNumber > trueNumber:
        print('正确数字在'+ str(xiaoLastNum) + '到' + str(guessNumber) + '之间')
        daLastNum = guessNumber
    else:
        break
if guessNumber == trueNumber:
    print('恭喜你中奖了')
else:
    print('你的6次机会已用完')
