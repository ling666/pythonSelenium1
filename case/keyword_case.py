#coding=utf-8
import sys
sys.path.append('E:\\pythonSelenium1')
from util.excel_util import ExcelUtil
from keywordselenium.action_method import ActionMethod
class KeywordCase:
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel = ExcelUtil('E:\pythonSelenium1\config\keyword.xls')
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(1,case_lines):
                is_run = handle_excel.get_col_values(i,3)
                if is_run == 'yes':
                    method = handle_excel.get_col_values(i,4)
                    send_value = handle_excel.get_col_values(i,5)
                    handle_value = handle_excel.get_col_values(i, 6)
                    self.run_method(method,send_value,handle_value)
        return is_run
            #if 是否有输入数据
                #执行方法(输入数据，操作元素)
            #if 没有输入数据
                #执行方法（操作元素）
    #如果send_value不为空的时候就执行
    def run_method(self,method,send_value,handle_value):
        method_value = getattr(self.action_method,method)  #getattr()可以通过字符串拿到对象里面的方法，这里只是拿到了这个方法这个对象
        if send_value:
            method_value(send_value,handle_value)  #执行method
        else:
            method_value(handle_value)

if __name__=='__main__':
    A=KeywordCase()
    print(A.run_main())


