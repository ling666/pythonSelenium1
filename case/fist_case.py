# coding = utf-8
# 不同的测试用例
import os
import sys
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
        self.driver.close()
        print("这是case的后置条件")


    def testLoginEmailError(self):
        emailError = self.login.loginEmailError('88@qq.com','1111','11111','111')
        self.assertFalse(emailError,"case注册执行成功了")
        # if emailError == True:
        #     print("注册成功了，此条case执行失败")
        #通过assert判断是否为error

    def testUsernameError(self):
        usernameError = self.login.loginUsernameError('34@qq.com','111','11111','111')
        self.assertFalse(usernameError)
        # if usernameError == True:
        #     print("注册成功了，此条case执行失败")

    def testUserpasswordError(self):
        userpasswordError = self.login.loginUserpasswordError('34@qq.com','1111','111','111')
        self.assertFalse(userpasswordError)
        # if userpasswordError == True:
        #     print("注册成功了，此条case执行失败")

    def testCodeError(self):
        codeError = self.login.loginCodeError('34@qq.com','1111','11111','111')
        self.assertFalse(codeError)
        # if codeError == True:
        #     print("注册成功了，此条case执行失败")

    def testLoginSuccess(self):
        success = self.login.registerSuccess('34@qq.com','1111','11111','111')
        self.assertFalse(success)
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
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="this is first report",description=u"这是我们第一次测试报告",verbosity=2)
    runner.run(suite)
    #unittest.main()