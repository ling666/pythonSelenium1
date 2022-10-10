# coding =utf-8
import configparser

class ReadIni(object):   # class继承于object(封装)
    def __init__(self,fileName=None,node=None):  # fileName有可能传有可能不传，它有一个默认值
        if fileName == None:
            fileName = "D:/pythonProject/config/localElement.ini"  # fileName为空时给它复制，不为空时直接运用本身的
        if node == None:
            self.node = "RegisterElement"  # node为空时给它赋值，不为空时直接运用
        else:
            self.node = node
        self.cf = self.loadIni(fileName)


# 加载
    def loadIni(self,fileName):   # 用于加载文件
        cf = configparser.ConfigParser()
        cf.read(fileName)
        return cf

# 获取value值
    def getValue(self,key):   # 该函数用来获取节点和前面的名字key
        date = self.cf.get(self.node,key)
        return date

if __name__=='__main__':
    readIni = ReadIni()
    print(readIni.getValue("userEmail"))






