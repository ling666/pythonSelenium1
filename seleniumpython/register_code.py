#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import random
from ShowapiRequest import ShowapiRequest
from PIL import Image
driver = webdriver.Chrome()

# 浏览器初始化
def driverInit():
    driver.get("http:\\www.5itest.cn/register")
    driver.maximize_window()
    time.sleep(5)

#判断title是否正确
def panDuanTitle():
    EC.title_contains("注册")

#获取element
def getElement(id):
    element = driver.find_element_by_id(id)
    locator = (By.CLASS_NAME, "controls")  # 定位元素，判断元素是否可见
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locator))
    # 拿到定位元素后找，然后判断是否可见，如果找到了就继续往下运行，如果没有找到就返回False
    return element

#获取随机数
def getRangeUser():
    userInfo = "".join(random.sample('1234567890abcdefg', 5))
    return userInfo

#获取图片
def getCodeImage(fileName):
    driver.save_screenshot(fileName)
    codeElement = driver.find_element_by_id("getcode_num")  # 定位到验证码图片
    left = codeElement.location['x']
    top = codeElement.location['y']
    right = codeElement.size['width'] + left
    height = codeElement.size['height'] + top  # 到这就把图片描绘出来了，需要下载一个库pillow
    im = Image.open(fileName)
    img = im.crop((left, top, right, height))  # 按照指定坐标裁剪图片
    img.save(fileName)

# 解析获取验证码
def codeOnline(fileName):
    r = ShowapiRequest("http://route.showapi.com/184-4", "499756", "29fb13c1d7dd44cc871b6f37a2430287")
    r.addFilePara("image", fileName)
    r.addBodyPara("typeId", "35")  # 35识别英文数字混合，5位
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res = r.post()
    print(res.text)
    captchatext = res.json()['showapi_res_body']['Result']
    return captchatext

# 运行主程序
def runMain():
    userNameInfo = getRangeUser()
    userEmail = userNameInfo + "@163.com"
    fileName ="H:/test.png"
    driverInit()
    panDuanTitle()
    getElement("register_email").send_keys(userEmail)
    getElement("register_nickname").send_keys(userNameInfo)
    getElement("register_password").send_keys("1234678")
    getCodeImage(fileName)
    text = codeOnline(fileName)
    getElement("captcha_code").send_keys(text)
    getElement("register-btn").click()
    driver.close()

runMain()

