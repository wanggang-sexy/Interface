#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
class OperationJson:
    def __init__(self,file_path=None):
        if file_path  == None:
            self.file_path = r"F:\maijinbei\app\data_file\request_data.json"
        else:
            self.file_path = file_path
        self.data = self.read_json()
    #读取json文件
    def read_json(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data
    #获取json内容
    def get_json(self,id):
        return self.data[id]

    #写json
    def write_data(self,data):
        with open(r"F:\maijinbei\app\data_file\cookie.json","w") as fp:
            fp.write(json.dumps(data))

if __name__ == '__main__':
    opecjson = OperationJson()
    print opecjson.get_json('login')
    print opecjson.get_json('goldprice')
    print opecjson.get_json('bannertype')
    op = OperationJson(file_path=r"F:\maijinbei\app\data_file\cookie.json")
    print op.get_json('data')['authToken']

