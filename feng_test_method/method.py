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


class startMethod(object):

    def longClear(self,element,time): #element长按元素 time长按时间
        action = TouchAction(self.driver)
        action.press(element).wait(time).release()
        action.perform()

    '''封装ID获取元素'''
    def action_Id(self,id,text):
        if text=='obtain':
            pro = '获取元素：'
            self.logger.info(u'>>>%s%s' % (pro, id))
            return self.driver.find_element_by_id(id)
        else:
            if text=='click':
                pro = '点击控件：'
                self.logger.info(u'>>>%s%s' % (pro, id))
                return self.driver.find_element_by_id(id).click()
            else:
                pro = '输入内容为：'
                self.logger.info(u'>>>定位控件%s,%s%s' % (id,pro,text))
                return self.driver.find_element_by_id(id).set_text(text)

    '''方法包装_通过当前页面:classname+text定位控件并完成输入'''
    def dianJi_ClassText_ShuRu(self,driver, className, text, txtUsername):
        allClassNames = driver.find_elements_by_class_name(className)  # 定义所有该className下所有控件为 allclassname
        for allClassName in allClassNames:
            print(allClassName.text)
            if text in allClassName.text:  # 当text的值属于  遍历出来当中的一个text值时，则为我们需要的值
                allClassName.set_text(txtUsername)
                break

    '''封装一个根据clsaa+text的方法点击控件 '''
    def dianJi_classText(self,driver, className, text):
        clickClassName = driver.find_elements_by_class_name(className)
        for clickclassNameOne in clickClassName:
            if text in clickclassNameOne.text:
                clickclassNameOne.click()
                break

    '''封装一个根据class+text的方法获取元素'''
    def huoQu_classText(self,className, text):
        clickClassName = self.driver.find_elements_by_class_name(className)
        for clickclassNameOne in clickClassName:
            if text in clickclassNameOne.text:
                print(text)
                print(clickclassNameOne)
                self.logger.info(text)
                break
            else:
                self.logger.info('sjoj')

    '''封装一个获取className的方法（className唯一）'''
    def huoQu_className(self,className):

        return self.driver.find_element_by_class_name(className)

    '''封装一个滑动当前页面查找元素方法'''
    def scroll_resourceId(self,id, textCode):
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().resourceId("%s")).scrollIntoView(new UiSelector().text("%s"))' % (
            id, textCode))

    '''封装一个滑动当前页面class+text查看元素方法'''
    def scroll_classText(self, classNameCode, textCode):
        self.driver.find_element_by_android_uiautomator((
                                                        'new UiScrollable(new UiSelector().className("%s")).scrollIntoView(new UiSelector().text("%s"))' % (
                                                        classNameCode, textCode)))
    '''无限各方为滑动加载获取指定元素'''
    def scroll_my(self,x1,y1,x2,y2,xpathCode,timeOut):
        timeStart = time.strftime('%d%H%M%S', time.localtime())
        while 1:
            try:
                self.driver.find_element_by_xpath(xpathCode)
                self.logger.info('获取到指定元素')
                break
            except:
                action = TouchAction(self.driver)
                action.press(x=x1, y=y1).wait(ms=1000).move_to(x=x2, y=y2).release()
                action.perform()
                timeOver = time.strftime('%d%H%M%S', time.localtime())
                if int(timeOver)-int(timeStart)>=int(timeOut):
                    self.logger.debug('抓取指定元素超时，抓取时间为：%s'%(int(timeOver)-int(timeStart)))
                    break
                else:
                    continue
        return self.driver.find_element_by_xpath(xpathCode)


    '''封装一个滑动toach的方法'''
    def toachSweip(self,x,y,x1,y1):
        action = TouchAction(self.driver)
        action.press(x=x, y=y).wait(ms=1000).move_to(x=x1, y=y1).release()
        action.perform()
    '''封装登录易直帮app方法'''
    def loginYiZhiBang(self,a,b):
        startMethod.action_Id(self, login['账号id'], 'obtain').clear()  # 清除账号输入框
        startMethod.action_Id(self, login['密码id'], 'obtain').clear()  # 清除密码输入框
        self.logger.info('初始化登录框完成')
        self.driver.find_element_by_id(login['账号id']).set_text(a)
        self.logger.info('输入账号为{}'.format(a))
        self.driver.find_element_by_id(login['密码id']).set_text(b)
        self.logger.info('输入密码为{}'.format(b))
        self.driver.find_element_by_id(login['登录id']).click()
        self.logger.info('点击登录按钮')
        try:
            WebDriverWait(self,20).until(
            lambda driver: startMethod.action_Id(self, bottom['我的id'], 'obtain'))  # 验证页面是否正常跳转成功
            self.logger.info('登录成功')
        except:
            self.logger.info('登录失败')

    '''封装退出易直帮APP方法'''
    def backLogin(self,a,b):
        if a==None and b==None:
            a=720
            b=1280
        while True:
            try:
                WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(flash['页面返回id']))
                self.driver.find_element_by_id(flash['页面返回id']).click()
                time.sleep(1)
                self.logger.info('获取到返回按钮，点击返回')
            except:
                break
        try:
            a1 = a / 720
            b1 = b / 1280
            x1 = self.driver.get_window_size()['width']
            y1 = self.driver.get_window_size()['height']
            a2 = x1 * a1
            b2 = y1 * b1
            self.logger.info('开始退出app')
            # time.time(2)
            WebDriverWait(self,30,0.1).until(lambda driver:self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/tv_home_exchange'))
            self.logger.info('获取到“我”控件元素')
            self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/rl_home_mine').click()  # 点击“我”

            WebDriverWait(self,10).until(
                lambda driver: self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/tv_home_exchange'))#获取"换一批"按钮，以判断页面是否跳转，否则有蒙层
            self.logger.info('点击我之后，仍然可以获取到“换一批”控件元素，存在“引导提示”')
            self.driver.tap([(a2, b2)])
            self.logger.info('点击引导提示')
            self.logger.info('1')
            self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/rl_home_mine').click()# 点击“我”
            self.logger.info('点击"我"')
            self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"设置\"]').click()
            self.logger.info('点击"设置"')
            try:
                self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/btn_setting_exit').click()
                self.logger.info('点击"退出登录"')
            except:
                self.logger.info('点击“退出登录”无响应，页面无“退出登录按钮，页面存在引导提示')
                self.driver.tap([(a2, b2)])
                self.logger.info('点击引导提示')
                self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"设置\"]').click()
                self.logger.info('点击"设置"')
                self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/btn_setting_exit').click()
                self.logger.info('点击"退出登录"')
        except:
            self.logger.info('点击“我”之后，未获取到“换一批”元素控件——页面已经跳转')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"设置\"]'))
            self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"设置\"]').click()
            self.logger.info('点击“设置”')
            try:
                WebDriverWait(self,10).until(
                    lambda driver: self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/btn_setting_exit'))
                self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/btn_setting_exit').click()
                self.logger.info('点击"退出登录"')
            except:
                self.logger.info('点击"退出登录"报错，存在引导提示')
                self.driver.tap([(a2, b2)])
                self.logger.info('点击引导提示')
                self.logger.info('5')
                self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"设置\"]').click()
                self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/btn_setting_exit').click()
    def backCode(self):
        while True:
            try:
                WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(flash['页面返回id']))
                self.driver.find_element_by_id(flash['页面返回id']).click()
                time.sleep(1)
                self.logger.info('获取到返回按钮，点击返回')
            except:
                break
        WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(bottom['我的id']))
        try:
            startMethod.action_Id(self,bottom['我的id'],'click')
            WebDriverWait(self, 10).until(
                lambda driver:self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"设置\"]'))
        except:
            self.assertEqual('网络异常')
        try:
            self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"设置\"]').click()
            WebDriverWait(self, 10).until(
            lambda driver: self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/btn_setting_exit'))
            self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/btn_setting_exit').click()
        except:
            self.assertEqual('网络异常')










    '''封装获取toast方法'''
    def find_toast(self,message):
        toast_Code = ('xpath', './/*[contains(@text,"%s")]'%message)
        t = WebDriverWait(self.driver,5,0.1).until(EC.presence_of_element_located(toast_Code))
        self.logger.info('获取到toast:{}'.format(t))


    def loginCode(self,User): #封装登陆方法
        startMethod.action_Id(self,login['账号id'],User)
        startMethod.action_Id(self,login['验证码id'],'click')
        time.sleep(2)
        code=titleMethod.redisCode(self,'192.168.1.171','6379','5','yc_test',User)
        startMethod.action_Id(self,login['密码id'],code)
        startMethod.action_Id(self,login['登录id'],'click')
        self.logger.info('初始化登陆成功')
        self.driver.implicitly_wait(10)
    def clickXY(self,x,y):
        '''封装点击坐标的方法'''
        x1=x/720#获取宽度比例
        y1=y/1280#获取高度比例
        a1=self.driver.get_window_size()['width']#获取当前屏幕宽度
        b1=self.driver.get_window_size()['height']#获取当前屏幕高度
        x2=int(a1*x1)#计算当前屏幕点击横坐标
        y2=int(b1*y1)#计算当前屏幕点击纵坐标
        self.driver.tap([(x2,y2)])#点击

class myMethod(object):
    # '''清除账号密码输入框'''
    # def clear(self):
    #     startMethod.action_Id(self, login['账号id'], 'obtain').clear()#清除账号输入框
    #     startMethod.action_Id(self, login['密码id'], 'obtain').clear()#清除密码输入框
    #     self.logger.info('账号与密码输入框已初始化')

    '''封装手机屏幕适配'''
    def androidSize(self,a,b):
        a1=a/720
        b1=b/1280
        x1=self.driver.get_window_size()['width']
        y1=self.driver.get_window_size()['height']
        m=x1*a1
        n=y1*b1
        return self.driver.tap([(m,n)])


    '''封装一个随机生成电话号码的方法,默认方法首位字母为1，其余十位随机'''
    def randomTel(self):
        i = 1
        listUsername = ['1']
        while i <= 10:
            Usernamecode = str(random.choice(range(10)))
            listUsername.append(Usernamecode)
            i += 1
        return ''.join(listUsername)
    '''等待定位元素'''
    def wait_time(self,resourceid,waitTime=None):
        try:
            if waitTime==None:
                waitTime=10
            WebDriverWait(waitTime).until(lambda driver:driver.find_element_by_id(resourceid))
            self.logger.info(u'>>>检测到{},页面未跳转成功'.format(resourceid))

        except Exception as f:
            print(f)
            self.logger.info(u'>>>未检测到{},页面跳转成功'.format(resourceid))
    '''读取excl表格内容'''

class titleMethod(object):
    '''excelb表格读取'''
    def duQu_Exlce(self,Sheet,a,b):
        exlce_Name = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\python01\fengfan_unittest\feng_exlce_case\denglu_excel.xls')  # 打开excel文件格式为xlsx有的是xls
        table = exlce_Name.sheet_by_name(Sheet)
        cell_a1 = table.cell(a,b).value  # a代表行——从零开始   b代表列 从零开始
        return cell_a1
        self.logger.info(u'>>>获取excel表格内容：{}'.format(cell_a1))

    '''复制表格写入excel'''
    def xieRu_Exlce(a, b, sheet_name, value, filePath):  # excel 写入
        excel_Name = xlrd.open_workbook(r'C:\Users\Administrator/Desktop/excel_case/denglu_excel.xls',
                                        formatting_info=True)  # 打开excel表格
        table = excel_Name.sheet_by_name(sheet_name)  # 选择sheet页
        exlce_NameCode = copy(excel_Name)  # 复制一个excel
        tableCode = exlce_NameCode.get_sheet(0)  # 找到复制后的 sheet页 ——备注：excel_Name.sheet_by_name无法write！get——sheet可以write
        tableCode.write(a, b, value)  # 写入
        exlce_NameCode.save(filePath)  # 保存新的excel


    '''封装一个传入服务器地址host，port端口号,db第几个表,redisPassword密码'''
    def redisCode(self,host,port,db,redisPassword,Usernamecode):
        pool=redis.ConnectionPool(host=host,port=port,db=db,password=redisPassword)
        r = redis.StrictRedis(connection_pool=pool)
        a=Usernamecode
        b='register_user_code_'
        return r.get(b+a).decode('utf-8')

