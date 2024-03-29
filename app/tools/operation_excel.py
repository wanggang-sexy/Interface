#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd
from xlutils.copy import copy
class OperationExcel:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
            #self.data = self.get_data()
        else:
            self.file_name = r'F:\maijinbei\app\data_file\Read_data.xls'
            self.sheet_id = 0
        self.data = self.get_data()
    #获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables
    #获取单元格行数
    def get_lines(self):
        tables = self.data
        return tables.nrows
    #获取某一单元格的内容
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)
    #写入excel数据
    def write_value(self,row,col,value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

    #根据对应的caseid找到行的内容
    def get_rows_data(self,case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data

    #根据对应的caseid找到对应的行号
    def get_row_num(self,case_id):
        num = 0
        cols_data = self.get_cols_data()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num+=1

    #根据行号找到该行的内容
    def get_row_values(self,row):
        tables  = self.data
        row_data = tables.row_values(row)#获取整行内容
        return row_data

    #获取某一列内容
    def get_cols_data(self,col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)#获取整列内容
        else:
            cols = self.data.col_values(0)
        return cols

if __name__ == '__main__':
    opers = OperationExcel()

    print opers.get_lines()
    print opers.get_cell_value(1,0)
    print opers.get_row_values(1)
    print opers.get_cols_data(1)