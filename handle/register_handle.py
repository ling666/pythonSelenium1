#coding =utf-8
#handle层去操作page层
from page.register_page import RegisterPage
class RegisterHandle(object):
    def __init__(self,driver):
        self.registerP = RegisterPage(driver)

    #输入邮箱
    def sendUserEmail(self,email):
        self.registerP.getEmailElement().send_keys(email)

    #输入用户名
    def sendUserName(self,username):
        self.registerP.getUserNameElement().send_keys(username)

    #输入密码
    def sendUserPassword(self,password):
        self.registerP.getPasswordElement().send_keys(password)

    #输入验证码
    def sendUserCode(self,code):
        self.registerP.getCodeElement().send_keys(code)

    #获取文字信息
    def getUsertext(self,info,userInfo):     #UserInfo判断邮箱错误还是用户名错误
        try:
            if info=='userEmailError':
                text = self.registerP.getuserEmailErrorElement().text
               #text = self.registerP.getuserEmailErrorElement().get_attribute('value')
            elif info=='userNameError':
               text = self.registerP.getuserNameErrorElement().text
            elif info=='passwordError':
               text = self.registerP.getpasswordErrorElement().text
            else:
                text = self.registerP.getcodeTextErrorElement().text
        except:
            text = None
        print(text)
        return text


    #点击注册按钮
    def clickRegisterButton(self):
        self.registerP.getButtonElement().click()
    #获取注册按钮文字
    def getRegisterButtonText(self):
        return  self.registerP.getButtonElement().text