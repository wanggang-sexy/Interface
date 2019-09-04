#!/usr/bin/env python
# -*- coding: utf-8 -*-
#定义变量
class global_var:
    Case_Id = '0'#用例ID
    Case_Name = '1'#用例名称
    Case_Url = '2'#请求地址
    Case_Run = '3'#是否执行
    Case_Request_way = '4'#请求方式
    Case_Headers = '5'#是否携带headers
    Case_Rely_Id = '6'#依赖ID
    Case_Data_depend = '7'#数据依赖
    Case_Field_depend = '8'#依赖数据所属字段
    Case_Request_data = '9'#请求数据
    Case_Expected_result = '10'#预期结果
    Case_Actual_result = '11'#实际结果
    Case_Token = '12'#获取token
#获取Caseid
def get_id():
    return global_var.Case_Id
#获取用例名称
def get_name():
    return global_var.Case_Name
#获取url
def get_url():
    return global_var.Case_Url
#获取是否执行
def get_run():
    return global_var.Case_Run
#获取请求方式
def get_run_way():
    return global_var.Case_Request_way
#获取headers
def get_headers():
    return global_var.Case_Headers
#获取依赖id
def get_relyid():
    return global_var.Case_Rely_Id
#获取数据依赖
def get_data_depend():
    return global_var.Case_Data_depend
#获取依赖所属字段
def get_field_depend():
    return global_var.Case_Field_depend
#获取请求数据
def get_request_data():
    return global_var.Case_Request_data
#获取预期结果
def get_expected_result():
    return global_var.Case_Expected_result
#获取实际结果
def get_actual_result():
    return global_var.Case_Actual_result
#获取token值
def get_token():
    return global_var.Case_Token

