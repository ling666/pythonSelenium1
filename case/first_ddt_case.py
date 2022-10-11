#coding = utf-8
import ddt
import unittest
import os
import sys
import time

from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import warnings
import HTMLTestRunner

#邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http:\\www.5itest.cn/register')
        self.login = RegisterBusiness(self.driver)
        # 解决错误 ResourceWarning: Enable tracemalloc to get the object allocation traceback
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self):
        time.sleep(2)
        #sys.exc_info()[0]: #python2里面捕获异常
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd(), ".." + "/report/" +case_name+".png")
                self.driver.save_screenshot(file_path)
        #print("这是case的后置条件")
        self.driver.close()

    @ddt.data(
        ['email','username','password','code','assertCode','assertText']
    )
    @ddt.unpack
    def test_register_case(self,email,username,password,code,assertCode,assertText):
        emailError = self.login.register_function(email,username,password,code,assertCode,assertText)
        self.assertFalse(emailError,"邮箱格式正确")
        # if emailError == True:
        #     print("注册成功了，此条case执行失败")
        #通过assert判断是否为error

if __name__ == '__main__':
    unittest.main()
