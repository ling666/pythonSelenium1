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
                print(is_run)
                if is_run == 'yes':
                    method = handle_excel.get_col_values(i,4)
                    send_value = handle_excel.get_col_values(i,5)
                    handle_value = handle_excel.get_col_values(i, 6)
                    except_result_method = handle_excel.get_col_values(i,7)
                    except_result = handle_excel.get_col_values(i,8)
                    #except_result_method和except_result有可能为空的，是''而不是None
                    self.run_method(method,send_value,handle_value)
                    if except_result != '':
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] == 'text':
                            result = self.run_method(except_result_method)
                            if except_value[1] in result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        elif except_value[0] == 'element':
                            result = self.run_method(except_result_method,except_value[1])
                            if result:
                                handle_excel.write_value(i, 'pass')
                            else:
                                handle_excel.write_value(i, 'fail')
                        else:
                            print('没有else')
                    else:
                        print('预期结果为空')


    #获取预期结果值
    def get_except_result_value(self,data):
        return data.split('=')  #split()可以进行字符串分割

    #如果send_value不为空的时候就执行
    def run_method(self,method,send_value='',handle_value=''):  #send_value有值就有值，如果没有值那我就认为你是空的
        print(send_value,"----->",handle_value)
        method_value = getattr(self.action_method,method)  #getattr()可以通过字符串拿到对象里面的方法，这里只是拿到了这个方法这个对象
        if send_value == '' and handle_value != '':
            result = method_value(handle_value)  #执行method,即打开浏览器
        elif send_value =='' and handle_value =='':
            result = method_value(send_value,handle_value)
        elif send_value !='' and handle_value =='':
            result = method_value(send_value)
        else:
            result = method_value()
        return result

if __name__=='__main__':
    test = KeywordCase()
    test.run_main()


