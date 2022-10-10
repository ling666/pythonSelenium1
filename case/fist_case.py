# coding = utf-8
# 不同的测试用例
import os
import sys
import time

from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import warnings
import HTMLTestRunner


class FistCase(unittest.TestCase):
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


    def testLoginEmailError(self):
        emailError = self.login.loginEmailError('88@qq.com','1111','11111','111')
        self.assertFalse(emailError,"邮箱格式正确")
        # if emailError == True:
        #     print("注册成功了，此条case执行失败")
        #通过assert判断是否为error

    def testUsernameError(self):
        usernameError = self.login.loginUsernameError('34@qq.com','111','11111','111')
        self.assertFalse(usernameError,"用户名格式正确，这条case执行失败")
        # if usernameError == True:
        #     print("注册成功了，此条case执行失败")

    def testUserpasswordError(self):
        userpasswordError = self.login.loginUserpasswordError('34@qq.com','1111','111','111')
        self.assertFalse(userpasswordError,"密码格式正确，这条case执行失败")
        # if userpasswordError == True:
        #     print("注册成功了，此条case执行失败")

    def testCodeError(self):
        codeError = self.login.loginCodeError('34@qq.com','1111','11111','111')
        self.assertFalse(codeError,"验证码正确，这条case执行失败")
        # if codeError == True:
        #     print("注册成功了，此条case执行失败")

    def testLoginSuccess(self):
        success = self.login.registerSuccess('34@qq.com','1111','11111','111')
        self.assertFalse(success,"注册成功了")
        # if self.login.registerSucces()  == True:
        #     print("注册成功")

'''
def main():
    first = FistCase()
    first.testLoginEmailError()
    first.testUsernameError()
    first.testUserpasswordError()
    first.testCodeError()
    first.testLoginSuccess()
'''
if __name__ == '__main__':

    file_path = os.path.join(os.getcwd(),".." + "/report/" + "first_case.html")
    f = open(file_path,'wb')
    suite = unittest.TestSuite()
    suite.addTest(FistCase('testLoginEmailError'))
    suite.addTest(FistCase('testUsernameError'))
    suite.addTest(FistCase('testUserpasswordError'))
    suite.addTest(FistCase('testCodeError'))
    suite.addTest(FistCase('testLoginSuccess'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="this is first report",description=u"这是我们第一次测试报告",verbosity=2)
    runner.run(suite)
    #unittest.main()