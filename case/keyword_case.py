#coding=utf-8
import sys
sys.path.append('E:\pythonSelenium1')
from util.excel_util import ExcelUtil
from keyword.action_methond import ActionMethod
class KeywordCase:
    def run_main(self):
        handle_excel = ExcelUtil('E:\pythonSelenium1\config\keyword.xls')
        #拿到行数
        #循环行数，去执行每一行的case
        #if 是否执行
            #拿到执行方法
            #拿到操作值
            #拿到输入数据
            #if 是否有输入数据
                #执行方法(输入数据，操作元素)
            #if 没有输入数据
                #执行方法（操作元素）