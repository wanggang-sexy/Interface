#!/usr/bin/env python
# -*- coding: utf-8 -*-
#unittest和封装的请求方法及HTMLTestRunner结合一起使用
import unittest

from app.base.Request_method import RunMain


class TestMethod(unittest.TestCase):

    def test_001(self):
        url ='http://183.62.205.226:8777/hsdgold-portal-app/index/getGoldPrice.json'
        data={}
        ran =RunMain(url,'get',data).res
        print ran
        self.assertEqual(ran['code'],'00000','测试失败')
        globals()['platformPrice']= ran['data']['platformPrice']

    def test_002(self):
        print platformPrice
        url ='http://183.62.205.226:8777/hsdgold-portal-app/gold/listTodayRecommendGoldProduct.json'
        data={}
        ran = RunMain(url,'get',data).res
        self.assertEqual(ran['code'],'00009','测试失败')
    def test_003(self):
        print platformPrice
        url ='http://183.62.205.226:8777/hsdgold-portal-app/gold/listTodayRecommendGoldProduct.json'
        data={}
        run = RunMain(url,'get',data).res
        print run
        self.assertEqual(run['code'],'00009','测试失败')

if __name__ == '__main__':
    unittest.main()
    '''
    filepath ="F:/maijinbei/app/report/htmlreport.html"
    fp = file(filepath,'wb')
    suit = unittest.TestSuite()
    suit.addTest(TestMethod('test_001'))
    suit.addTest(TestMethod('test_002'))
    suit.addTest(TestMethod('test_003'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is report')#生成测试报告
    runner.run(suit)
    #unittest.TextTestRunner().run(suit)#直接运行，未生成测试报告
    '''
