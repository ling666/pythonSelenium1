#coding=utf-8
#business层去操作handle层
from handle.register_handle import RegisterHandle
class RegisterBusiness(object):
    def __init__(self,driver):
        self.registerH = RegisterHandle(driver)
    def userBase(self,email,name,password,code):
        self.registerH.sendUserEmail(email)
        self.registerH.sendUserName(name)
        self.registerH.sendUserPassword(password)
        self.registerH.sendUserCode(code)
        self.registerH.clickRegisterButton()
        self.registerH.getRegisterButtonText()

    def registerSuccess(self,email,name,password,code):
        self.userBase(email, name, password, code)
        if self.registerH.getRegisterButtonText() == None:
            print("注册成功")
            return True
        else:
            print("注册失败")
            return False

    #邮箱错误
    def loginEmailError(self,email,name,password,code):
        self.userBase(email,name,password,code)
        #email是从case中传下来的
        if self.registerH.getUsertext('userEmailError',"请输入有效的电子邮件地址") == None:
            print("邮箱格式正确")
            return True
        else:
            return False

    #用户名错误
    def loginUsernameError(self, email, name, password, code):
        self.userBase(email, name, password, code)
        # email是从case中传下来的
        if self.registerH.getUsertext('userNameError', "字符长度必须大于等于4，一个中文字算2个字符") == None:
            print("用户名格式正确")
            return True
        else:
            return False
    #密码错误
    def loginUserpasswordError(self, email, name, password, code):
        self.userBase(email, name, password, code)
        # email是从case中传下来的
        if self.registerH.getUsertext('passwordError', "最少需要输入 5 个字符") == None:
            print("密码格式正确")
            return True
        else:
            return False

    #验证码错误
    def loginCodeError(self, email, name, password, code):
        self.userBase(email, name, password, code)
        # email是从case中传下来的
        if self.registerH.getUsertext('codeTextError', "验证码错误") == None:
            print("验证码正确")
            return True
        else:
            return False

        #     return True
        # self.registerH.sendUserPassword(password)
        # self.registerH.sendCode(code)
