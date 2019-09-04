#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from app.base.run_method import RunMethod
from app.data.get_data import GetData
from app.tools.common_util import CommonUtil
from app.data.dependent_data import DependentData
from app.tools.operation_json import OperationJson
class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.common = CommonUtil()
        self.open_json = OperationJson()
    #程序执行
    def go_on_run(self):
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()#行数
        for i in range(1,rows_count):
            is_run = self.data.get_is_run(i)#是否执行
            if is_run:
                url = self.data.get_request_url(i)#url参数
                method = self.data.get_request_method(i)#请求方式
                data = self.data.get_data_for_json(i)#从json中取请求数据
                headers = self.data.get_is_header(i)#取出headers数据
                expect = self.data.get_expect_data(i)#预期结果数据
                depend_case = self.data.is_depend(i)
                Token = self.data.get_token_data(i)
                res = self.run_method.run_main(method,url,data,headers)
                if depend_case != None:
                    self.depend_data = DependentData(depend_case)
                    #获取的依赖响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    #获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    data[depend_key] = depend_response_data
                if Token == 'write':
                    res = self.run_method.run_main(method,url,data,headers)
                    res_data = json.loads(res)
                    self.open_json.write_data(res_data)
                    self.open_cookie = OperationJson(file_path=r"F:\maijinbei\app\data_file\cookie.json")
                    token = str(self.open_cookie.get_json('data')['authToken'])
                elif Token == 'yes':
                    res = self.run_method.run_main(method,url,data,token,headers)
                else:
                    res = self.run_method.run_main(method,url,data,headers)
                if self.common.is_contain(expect,res):
                    self.data.write_result(i,'pass')
                    pass_count.append(i)
                else:
                    self.data.write_result(i,res)
                    fail_count.append(i)

if __name__ == '__main__':

    runtest = RunTest()
    runtest.go_on_run()


