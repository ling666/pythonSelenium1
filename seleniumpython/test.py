
class Student():
    def __init__(self,name,age):
        self.name =name
        self.age = age
        # 私有变量定义
        # 以两个下划线开头，不能以两个下划线结尾
        self.__dairy = self.name + "日记"

    def hello(self):
        print("我的名字是%s，我的日记是%s"%(self.name,self.__dairy))
lisi = Student("LiSi",28)
lisi.hello()
print(lisi.name)
print(lisi.age)
print(lisi._Student__dairy)
