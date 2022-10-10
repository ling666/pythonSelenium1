#coding=utf-8
from selenium import webdriver
import  time
#导入expected_conditions预期包判断标题是否正确：
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()   #运用什么浏览器使用什么浏览器的driver
driver.maximize_window()  #将窗口最大化
driver.get("http://183.61.5.19:8989/sso/login")
time.sleep(5)
title1 = EC.title_contains('登录') #title_contains则为True否则为False包含
print(title1(driver))
# title2 = EC.title_is('珠海市金湾区政务服务统一申办受理平台|登录')#title_is 匹配完全一致为True，否则为False
# print(title2(driver))

# #另外一种写法
# title1 = EC.title_contains('登录')(driver)
# title2 = EC.title_is('珠海市金湾区政务服务统一申办受理平台|登录')(driver)
# print(title1)
# print(title2)

#element = driver.find_element_by_class_name("fg-line")
locator = (By.CLASS_NAME,"fg-line")
WebDriverWait(driver,5).until(EC.visibility_of_element_located(locator))
driver.close() #实例化一个driver就要关掉不然电脑越来越卡
#EC.invisibility_of_element_located()方法判断传入的元素是否可见
#EC.presence_of_element_located()方法判断传入的元素是都存在dom里面

# #定位后输入
# #driver.find_element_by_id("username").send_keys("丁亚云")
# driver.find_element_by_name("username").send_keys("丁亚云")
# passwordElementDivClass = driver.find_elements_by_class_name("fg-line")[1]
# passwordElementInputClass = passwordElementDivClass.find_element_by_class_name("form-control")
# #print(len(passwordElementInputClass))
# passwordElementInputClass.send_keys("12345678")
# driver.find_element_by_xpath("//*[@id='validateCode']").send_keys("111")


