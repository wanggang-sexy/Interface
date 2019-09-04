# -*- coding: utf-8 -*-
import hashlib,time

def Md5Enerypt(Lstr):
    m = hashlib.md5()
    m.update(str(Lstr))
    return m.hexdigest()



