#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.tools.operation_excel import OperationExcel
from app.tools.operation_json import OperationJson
from app.tools import Define_variables
class GetData:
    def __init__(self):
        self.open_excel = OperationExcel()
        self.open_json = OperationJson()
    #获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.open_excel.get_lines()
    #获取是否执行
    def get_is_run(self,row):
        flag = None
        col = Define_variables.get_run()
        run_model = self.open_excel.get_cell_value(row,int(col))
        if run_model == 'YES':
            flag= True
        else:
            flag=False
        return flag
    #是否携带headers
    def get_is_header(self,row):
        col = Define_variables.get_headers()
        headers = self.open_excel.get_cell_value(row,int(col))
        if headers == 'yes':
            return 'headers'
        else:
            return None
    #获取请求方式
    def get_request_method(self,row):
        col = Define_variables.get_run_way()
        request_method = self.open_excel.get_cell_value(row,int(col))
        return request_method
    #获取url
    def get_request_url(self,row):
        col = Define_variables.get_url()
        request_url = self.open_excel.get_cell_value(row,int(col))
        return request_url
    #获取请求数据
    def get_request_data(self,row):
        col = Define_variables.get_request_data()
        data = self.open_excel.get_cell_value(row,int(col))
        if data == '':
            return None
        else:
            return data
    #通过获取关键字拿到data数据
    def get_data_for_json(self,row):
        request_data = self.open_json.get_json(self.get_request_data(row))
        return request_data
    #获取预期结果
    def get_expect_data(self,row):
        col =Define_variables.get_expected_result()
        expect = self.open_excel.get_cell_value(row,int(col))
        if expect == '':
            return None
        else:
            return expect
    #获取caseid
    def get_is_id(self,row):
        col = Define_variables.get_id()
        id  = self.open_excel.get_cell_value(row,int(col))
        return id
    #获取模块名称
    def get_is_name(self,row):
        col = Define_variables.get_name()
        name = self.open_excel.get_cell_value(row,int(col))
        return name
    #获取实际结果
    def get_actual_data(self,row):
        col = Define_variables.get_actual_result()
        actual = self.open_excel.get_cell_value(row,int(col))
        return actual
    #获取token
    def get_token_data(self,row):
        col = Define_variables.get_token()
        token = self.open_excel.get_cell_value(row,int(col))
        if token == '':
            return None
        else:
            return token
    #写入实际结果
    def write_result(self,row,value):
        col = Define_variables.get_actual_result()
        self.open_excel.write_value(row,int(col),value)

    #获取依赖数据的key
    def get_depend_key(self,row):
        col = Define_variables.get_data_depend()
        depend_key = self.open_excel.get_cell_value(row,int(col))
        if depend_key == '':
            return None
        else:
            return depend_key

    #判断是否有数据依赖case_id
    def is_depend(self,row):
        col = Define_variables.get_relyid()
        depend_case_id = self.open_excel.get_cell_value(row,int(col))
        if depend_case_id == '':
            return None
        else:
            return depend_case_id

    #获取数据依赖字段
    def get_depend_field(self,row):
        col = Define_variables.get_field_depend()
        data = self.open_excel.get_cell_value(row,int(col))
        if data == "":
            return None
        else:
            return data

if __name__ == '__main__':
    g = GetData()
    print g.write_result(1,'pass')
    print g.get_is_name(1)
    print g.get_depend_key(2)
    print g.is_depend(2)
