# coding:utf-8
import  redis
from selenium import webdriver
import time
import random
import  os
from appium.webdriver.common.touch_action import TouchAction #导入Touch Action类   这个是支持手势操作
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlrd#读取
from xlutils.copy import copy#复制写入

from selenium.webdriver.support import *
from pyocr import pyocr
from PIL import Image
import traceback
import logging
from fengfan_unittest.feng_test_log.feng_test_logmethod import *
from fengfan_unittest.feng_test_conf.feng_test_env.feng_test_config import *


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class ActionMethod(object):
    def Material(self):  #登录到素材页面方法封装
        try:
            self.driver.find_element_by_xpath(navigation['素材xpath']).click()
            self.logger.info('点击素材')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case06['添加id']))
            self.logger.info('页面跳转成功')
        except:
            self.assertEqual(1,2,msg='网络异常，页面未成功跳转')
    def NoteBook(self):#登录后进入每日待办
        try:
            self.driver.find_element_by_xpath(navigation['每日待办xpath']).click()
            self.logger.info('点击每日待办')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case07['新建id']))
            self.logger.info('页面跳转成功')
        except:
            self.asserEqual(1,2,msg='网络异常，页面未成功跳转')
    def Diary(self,xpath):#登录后进入二级页面
        try:
            self.driver.find_element_by_xpath(navigation['营销日记xpath']).click()
            self.logger.info('点击营销日记')
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_xpath(case06['添加id']))
            self.logger.info('页面跳转成功')
        except:
            self.asserEqual(1,2,msg='网络异常，页面未成功跳转')







