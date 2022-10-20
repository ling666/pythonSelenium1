#coding = utf-8
import xlrd
from xlutils.copy import copy
class ExcelUtil:
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            self.excel_path = "E:\pythonSelenium1\config\casedata.xls"
        else:
            self.excel_path =excel_path
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index]   #目的是将case读成[["A","B"],[],[]]

    #获取Excel数据，按照每行一个list，添加到一个大的list里面
    def get_data(self):
        result = []
        rows = self.get_line()
        if row != None:
            for i in range(rows):
                col = self.table.row_values(i) #拿行的数据
                result.append(col)  # 将col追加到列表末尾
            return result
        return None
    #获取Excel行数
    def get_lines(self):
        rows = self.table.nrows  # 获取行数
        if rows >= 1:
            return rows
        return None
    #获取单元格数据
    def get_col_values(self,row,col):
        if self.get_lines()>row:
            date = self.table.cell(row,col).value  #第4行第3列的数据
            return date
        return None

    #写入数据
    def write_value(self,row,value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value) #复制工作表
        write_data.get_sheet(0).write(row,9,value)  #get_sheet(0)获得工作表，然后write写入内容
        write_data.save(self.excel_path)

if __name__ == '__main__':
    ex = ExcelUtil('E:\pythonSelenium1\config\keyword.xls')
    print(ex.get_col_values(10,8))
