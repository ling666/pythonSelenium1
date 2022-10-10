# coding=utf-8
from selenium import webdriver
import time
import random
from base.find_element import FindElement

class RegisterFuction(object):
    def __init__(self,url,i):
        self.driver = self.getDriver(url,i)
    # 获取driver并且打开URL
    def getDriver(self,url,i):
        if i ==1:
            driver = webdriver.Chrome()
        elif i ==2:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Edge()
        driver.get(url)
        driver.maximize_window()
        return driver
    # 输入用户信息
    def sendUserInfo(self,key,data):
        self.getUserElement(key).send_keys(data)


    # 定位用户信息，获取element
    def getUserElement(self,key):
        # 需要通过find_element 中FindElement类中的getElement，find的时候需要有一个driver
        findElement = FindElement(self.driver)
        userElement = findElement.getElement(key)
        return userElement

    # 获取随机数
    def getRangeUser(self):
        userInfo = "".join(random.sample('1234567890abcdefg', 5))
        return userInfo

    #以下是验证码处理的代码
    # # 获取图片
    # def getCodeImage(self,fileName):
    #     self.driver.save_screenshot(fileName)
    #     codeElement = self.getUserElement("codeImage")  # 定位到验证码图片
    #     left = codeElement.location['x']
    #     top = codeElement.location['y']
    #     right = codeElement.size['width'] + left
    #     height = codeElement.size['height'] + top  # 到这就把图片描绘出来了，需要下载一个库pillow
    #     im = Image.open(fileName)
    #     img = im.crop((left, top, right, height))  # 按照指定坐标裁剪图片
    #     img.save(fileName)
    #
    # # 解析图片获取验证码
    # def codeOnline(self,fileName):
    #     self.getCodeImage(fileName)
    #     r = ShowapiRequest("http://route.showapi.com/184-4", "499756", "29fb13c1d7dd44cc871b6f37a2430287")
    #     r.addFilePara("image", fileName)
    #     r.addBodyPara("typeId", "35")  # 35识别英文数字混合，5位
    #     r.addBodyPara("convert_to_jpg", "0")
    #     r.addBodyPara("needMorePrecise", "0")
    #     res = r.post()
    #     print(res.text)
    #     captchatext = res.json()['showapi_res_body']['Result']
    #     return captchatext

    def main(self):
        userNameInfo = self.getRangeUser()
        userEmail = userNameInfo + "@163.com"
        fileName = "H:/test.png"
        # codeText = self.codeOnline(fileName)
        print("请输入你看到的验证码")
        codeText = input()
        self.sendUserInfo("userEmail",userEmail)
        self.sendUserInfo("userName",userNameInfo)
        self.sendUserInfo("password","12345678")
        self.sendUserInfo("codeText",codeText)
        self.getUserElement("registerButton").click()
        codeError = self.getUserElement("codeTextError")
        if codeError == None:
            print("注册成功")
        else:
            self.driver.save_screenshot("H:/tu/codeError.png")
            print("注册失败，验证码错误")
        time.sleep(5)
        self.driver.close()
if __name__ == '__main__':
    # for i in range(3):
        registerFuction = RegisterFuction("http:\\www.5itest.cn/register",1)
        registerFuction.main()
