#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.tools.operation_excel import OperationExcel
from app.base.run_method import RunMethod
from app.data.get_data import GetData
from jsonpath_rw import jsonpath,parse
import json
class DependentData:
    def __init__(self,case_id):
        self.case_id = case_id
        self.oper_excel = OperationExcel()
        self.data = GetData()
    #通过caseid去获取caseid整行数据
    def get_case_line_data(self):
        rows_data = self.oper_excel.get_rows_data(self.case_id)
        return rows_data

    #执行依赖数据，获取结果
    def run_dependent(self):
        run_method = RunMethod()
        row_num = self.oper_excel.get_row_num(self.case_id)
        #request_data = self.data.get_data_for_json(row_num)
        url = self.data.get_request_url(row_num)#url参数
        method = self.data.get_request_method(row_num)#请求方式
        data = self.data.get_data_for_json(row_num)#从json中取请求数据
        headers = self.data.get_is_header(row_num)#取出headers数据
        res = run_method.run_main(method,url,data,headers)
        return json.loads(res)
    #根据依赖的key去获取依赖测试case的响应数据，然后返回
    def get_data_for_key(self,row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]


if __name__ == '__main__':
    d = DependentData('M-001')
    print d.run_dependent()