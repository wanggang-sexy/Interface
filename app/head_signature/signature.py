# -*- coding: utf-8 -*-
import EncSign
import time

def basis_parameter(dataes):
    hsd_mobile={
        "deviceId": "865586023165519",
        "sysName": "Android:4.4.2_Manufacturer:HUAWEI_Model:PE-TL20",
        "sysType": "41",
        "timestamp": str(int(time.time()*1000)),
        "token": "token",
        "verCode": "10",
        "verName": "1.1.1"
    }


    Pdata = dict(dataes.items()+hsd_mobile.items())
    
    return Pdata


def intefr_encryption(datadict):
    if datadict.has_key("signature"):
        del datadict["signature"]
    datalist=sorted(datadict.keys())
    sign=''
    for flag in datalist:
        key_value=str(flag)+"="+str(datadict[flag])+','
        sign += str(key_value)

    sign += "mjb147258369!"

    sign=EncSign.Md5Enerypt(sign)
    datadict["signature"]=sign
    return datadict


	
def qingqiu_tou(tou):#拼接请求头
    tou["Content-Type"]="application/x-www-form-urlencoded; charset=UTF-8"
    return tou
