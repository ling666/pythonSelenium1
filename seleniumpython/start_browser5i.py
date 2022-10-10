from selenium import webdriver
import time
import random
from PIL import Image
#导入expected_conditions预期包判断标题是否正确：
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()  #运用什么浏览器使用什么浏览器的driver
driver.maximize_window()  #将窗口最大化
driver.get("http:\\www.5itest.cn/register")
time.sleep(5)
title1 = EC.title_contains("注册")  #title_contains包含文本则为True否则为False
#print(title1(driver))
title2 = EC.title_is("注册")
#print(title2(driver)) #title_is 匹配完全一致为True，否则为False

# #另外一种写法
# title1 = EC.title_contains('登录')(driver)
# title2 = EC.title_is('珠海市金湾区政务服务统一申办受理平台|登录')(driver)
# print(title1)
# print(title2)

#验证码处理
#先将图片裁剪下来，再使用pytesseract识别图中的文字
driver.save_screenshot("F:/imcooc.png") #保存整张网页
codeElement = driver.find_element_by_id("getcode_num") #定位到验证码图片
print(codeElement.location) #{"X":123,"Y":456}
left = codeElement.location['x']
top = codeElement.location['y']
right = codeElement.size['width']+ left
height = codeElement.size['height'] + top #到这就把图片描绘出来了，需要下载一个库pillow
im = Image.open("F:/Imcooc.png")
img = im.crop((left,top,right,height))  #按照指定坐标裁剪图片
img.save("F:/imcooc1.png")
#使用第三方识别图片中的验证码，保存成text
r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dcdbd9969f741b8e7305" )
r.addFilePara("image", "F:/imcooc1.png")
r.addBodyPara("typeId", "35")  #35识别英文数字混合，5位
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
print(res.text)
captchatext = res.json()['showapi_res_body']['Result']  #json中提取Result结果
print("图片获取到的验证码是" + captchatext) # 返回信息
time.sleep(2)


#判断元素是否可见
#element = driver.find_element_by_class_name("controls")
locator = (By.CLASS_NAME,"controls")  #定位元素
WebDriverWait(driver,5).until(EC.visibility_of_element_located(locator))
#拿到定位元素后找，然后判断是否可见，如果找到了就继续往下运行，如果没有找到就返回False

#输入信息和获取信息使用get_attribute方法,随机生成邮箱
emailElement = driver.find_element_by_id("register_email")
suiJi = random.sample('1234567890abcdefg',5) #截取列表的指定长度的随机数
myEmail = "".join(suiJi) + "@qq.com"  #用"".join()方法把它连接起来
print("邮箱：" + emailElement.get_attribute("placeholder"))
emailElement.send_keys(myEmail)
print(emailElement.get_attribute("value"))

# driver.find_element_by_id("register_email").send_keys("760724206@qq.com")
userNameElementNode = driver.find_elements_by_class_name("controls")[1]   #controls有多个的时候需要用find_elements_by_class_name列表指定第几个
userElement = userNameElementNode.find_element_by_class_name("form-control")
#print(len(userElement))
userElement.send_keys("yuling")
print("用户名："+ userElement.get_attribute("placeholder")+ userElement.get_attribute("value"))
nameElement = driver.find_element_by_name("password")
nameElement.send_keys("12345678qwe")
print("密码：" + nameElement.get_attribute("placeholder") + nameElement.get_attribute("value"))
captchaElement = driver.find_element_by_xpath("//*[@id='captcha_code']")
captchaElement.send_keys(captchatext)
print("验证码：" + captchaElement.get_attribute("placeholder") + captchaElement.get_attribute("value"))
time.sleep(5)
driver.close()