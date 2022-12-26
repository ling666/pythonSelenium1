# coding =utf-8
from util.read_ini import ReadIni
from selenium.webdriver.common.by import By


class FindElement(object):
    def __init__(self, driver):
        self.driver = driver

    def getElement(self, key):
        readIni = ReadIni()
        date = readIni.getValue(key)
        by = date.split('>')[0]  # 取>前的内容
        value = date.split('>')[1]  # 取>后的内容
        try:
            if by == 'id':
                return self.driver.find_element(By.ID, value)
                # return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element(By.NAME, value)
                # return self.driver.find_element_by_name(value)
            elif by == 'className':
                return self.driver.find_element(By.CLASS_NAME, value)
                # return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_class_xpath(value)
        except:
            self.driver.save_screenshot('D:/pythonProject/image/%s.png' % value)
            return None
