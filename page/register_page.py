#coding=utf-8
#目的去拿element
from base.find_element import FindElement
class RegisterPage(object):
    def __init__(self,driver):
        self.fd = FindElement(driver)
    def getEmailElement(self):
        return self.fd.getElement("userEmail")

    def getUserNameElement(self):
        return self.fd.getElement("userName")

    def getPasswordElement(self):
        return self.fd.getElement("password")

    def getCodeElement(self):
        return self.fd.getElement("codeText")

    def getButtonElement(self):
        return self.fd.getElement("registerButton")

    def getuserEmailErrorElement(self):
        return self.fd.getElement("userEmailError")

    def getuserNameErrorElement(self):
        return self.fd.getElement("userNameError")

    def getpasswordErrorElement(self):
        return self.fd.getElement("passwordError")

    def getcodeTextErrorElement(self):
        return self.fd.getElement("codeTextError")
