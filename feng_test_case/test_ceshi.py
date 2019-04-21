import unittest,time
from fengfan_unittest.startAPP import *
from fengfan_unittest.feng_test_method.method import *
import  unittest,requests,HTMLTestRunner
from fengfan_unittest.feng_test_conf.feng_test_env.feng_test_config import *
import random

time = time.strftime('%d%H%M%S', time.localtime())


class  Blood(unittest.TestCase,object):
    def setUp(self):
        start_App.__init__(self)
        start_App.setUp(self)
    def tearDown(self):
        start_App.tearDown(self)
    def test_03(self):
        '''验证轮播图2页面跳转'''
        self.driver.find_element_by_xpath(r'//android.view.View[@content-desc={}]'.format(name))
        self.driver.find_element_by_xpath(r'//android.view.View[@content-desc={}]'.format("易直帮号：" + nameTel))
        self.driver.find_element_by_xpath(r'//android.view.View[@content-desc={}]'.format("所属职务：") + job)
        self.driver.find_element_by_xpath(
            r'//android.view.View[@content-desc=\"公司名称：云易恒基10163413\"]'.format("公司名称：" + companyName))
        self.logger.info('预览页面获取到用户昵称、易直帮号、所属职务、公司名称、且与主页面一致！')

