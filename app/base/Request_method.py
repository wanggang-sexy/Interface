#!/usr/bin/env python
# -*- coding: utf-8 -*-
#请求方法封装
import requests
from app.head_signature import signature
from app.head_signature import MD5

class RunMain:
    '''
    def __init__(self,url,mented,data):#实例化
        self.res = self.send_main(url,mented,data)
    '''
    def send_post(self,url,data=None):
        datas= signature.basis_parameter(data)
        headers= signature.qingqiu_tou(signature.intefr_encryption(datas))
        res = requests.post(self,url,headers=headers,data=data).json()
        return res
    def send_get(self,url,data):
        datas= signature.basis_parameter(data)
        headers= signature.intefr_encryption(datas)
        res = requests.get(url,headers=headers,data=data).json()
        return res
    def send_main(self,url,mented,data):
        if mented == 'POST':
            re = None
            re = self.send_post(url,data)
        else:
            re = self.send_get(url,data)
        return re
'''
if __name__ == '__main__':
    url ='http://183.62.205.226:8777/hsdgold-portal-app/index/getGoldPrice.json'
    data={}
    run = RunMain(url,'get',data)
    print run.res
'''