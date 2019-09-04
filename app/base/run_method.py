#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
from app.head_signature import signature
class RunMethod:
    def post_main(self,url,data,token=None,headers=None):
        res = None
        if headers != None:
            res = requests.post(url=url,data=data,headers=headers).json()
        else:
            if token == None:
                datas= signature.basis_parameter(data)
                datas['token'] = 'token'
                headers= signature.qingqiu_tou(signature.intefr_encryption(datas))
                res = requests.post(url=url,data=data,headers=headers).json()
            else:
                datas= signature.basis_parameter(data)
                datas['token'] = token
                headers= signature.qingqiu_tou(signature.intefr_encryption(datas))
                res = requests.post(url=url,data=data,headers=headers).json()
        return res
    def get_main(self,url,data,token=None,headers=None):
        res = None
        if headers != None:
            res = requests.get(url=url,data=data,headers=headers).json()
        else:
            if token == None:
                datas= signature.basis_parameter(data)
                datas['token'] = 'token'
                headers= signature.qingqiu_tou(signature.intefr_encryption(datas))
                res = requests.get(url=url,data=data,headers=headers).json()
            else:
                datas= signature.basis_parameter(data)
                datas['token'] = token
                headers= signature.qingqiu_tou(signature.intefr_encryption(datas))
                res = requests.get(url=url,data=data,headers=headers).json()
        return res
    def run_main(self,method,url,data,token=None,headers=None):
        res = None
        if method == 'POST':
            res = self.post_main(url,data,token,headers)
        else:
            res = self.get_main(url,data,token,headers)

        #return res
        return json.dumps(res,ensure_ascii=False)

        #return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)


if __name__ == '__main__':

    tun = RunMethod()
    url ='http://183.62.205.226:8777/hsdgold-portal-app/index/getGoldPrice.json'
    data={}
    method = 'get'
    res =  tun.run_main(method,url,data)
    print res
    print type(res)