import unittest,time
from fengfan_unittest.startAPP import *
from fengfan_unittest.feng_test_method.method import *
import  unittest,requests,HTMLTestRunner
from fengfan_unittest.feng_test_conf.feng_test_env.feng_test_config import *
import random

# time = time.strftime('%d%H%M%S', time.localtime())


class  Test_banner(unittest.TestCase,object):
    def setUp(self):
        start_App.__init__(self)
        start_App.setUp(self)
        time.sleep(3)
    def tearDown(self):
        startMethod.backCode(self)
        start_App.tearDown(self)
    def test01(self):
        '''验证首页引导页'''
        self.logger.info('*************************************************************')
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id('android:id/button1'))
            startMethod.action_Id(self, 'android:id/button1', 'click')
            self.logger.info('获取点击授权“允许”')
        except:
            time.sleep(30)
            self.logger.info('手机系统不兼容，无法获取到授权允许，默认等待三十秒！')
        startMethod.toachSweip(self, 0.9, 0.1, 0.1, 0.1)
        time.sleep(1)
        startMethod.toachSweip(self, 0.9, 0.1, 0.1, 0.1)
        time.sleep(1)
        startMethod.action_Id(self, flash['开始使用id'], 'click')
        try:
            startMethod.action_Id(self, login['登录id'], 'obtain')
            self.assertEqual(1, 1, msg='第一次开机引导页，成功跳过')
            self.logger.info('第一次开机引导页，成功跳过')
        except:
            self.assertEqual(1, 2, msg='第一次开机引导页，没有跳过，未检测到登录元素')
        startMethod.loginYiZhiBang(self, '13590283182', '123456')  # 登陆
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(flash['首页知道啦id']))
        except:
            self.assertEqual(1,2,msg='未获取到首页引导页')
        try:#验证首页引导页
            self.driver.find_element_by_id(flash['首页知道啦id']).click()
            self.logger.info('点击首页“我知道啦')
            time.sleep(2)
            WebDriverWait(self, 1).until(lambda driver: self.driver.find_element_by_id(flash['首页知道啦id']))
            self.assertEqual(1, 2, msg='点击引导页“知道啦”之后，引导页仍然存在')
        except:
            self.logger.info('点击首页“知道啦”，成功')
        try:#验证个人中心引导页
            startMethod.action_Id(self,bottom['我的id'],'click')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(flash['我知道啦id']))
            self.logger.info('页面跳转成功')
        except:
            self.assertEqual(1,2,msg='页面未跳转成功')
        try:
            startMethod.action_Id(self,flash['我知道啦id'],'click')
            time.sleep(1)
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(flash['我知道啦id']))
            self.assertEqual(1,2,msg='点击知道啦，引导页未消失')
        except:
            self.logger.info('点击知道啦引导页消失')
    def test02(self):
        '''品牌微网知道啦'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')  # 登陆
        try:#验证品牌微网引导页
            self.driver.find_element_by_xpath(navigation['品牌微网xpath']).click()
            time.sleep(1)
            self.logger.info('点击品牌微网')
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(flash['品牌微网知道啦id']))
            self.logger.info('获取到品牌微网“知道啦”')
        except:
            self.assertEqual(1,2,msg='点击品牌微网页面未跳转成功')
        try:#点击品牌微网知道啦
            startMethod.action_Id(self,flash['品牌微网知道啦id'],'click')
            time.sleep(1)
            self.logger.info('点击品牌微网知道啦')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id('品牌微网知道啦id'))
            self.assertEqual(1, 2, msg='点击引导页“知道啦”之后，引导页仍然存在')
        except:
            self.logger.info('点击品牌微网知道啦成功')
    def test03(self):
        '''品牌微网产品中心引导页'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')  # 登陆
        try:
            self.driver.find_element_by_xpath(navigation['品牌微网xpath']).click()
            self.logger.info('点击品牌微网')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(flash['页面返回id']))
            self.logger.info('点击产品中心页面跳转成功')
        except:
            self.assertEqual(1,2,msg='点击品牌微网页面未跳转成功')

        try:#点击品牌微网/产品中心
            self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/brand_category_image')[0].click()
            self.logger.info('点击品牌微网/产品中心')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(logoV['产品中心知道啦id']))
            self.logger.info('进入品牌微网/产品中心，获取到知道啦id')
        except:
            self.assertEqual(1,2,msg='点击品牌微网/产品中心，未获取到知道啦')
        try:#点击品牌微网/产品中心知道啦
            startMethod.action_Id(self,logoV['产品中心知道啦id'],'click')
            self.logger.info('点击产品中心知道啦')
            time.sleep(1)
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(logoV['产品中心知道啦id']))
            self.assertEqual(1,2,msg='点击品牌微网/产品中心/知道啦，任然可以获取到知道啦，点击知道啦失败')
        except:
            self.logger.info('点击产品中心知道啦成功')
    def test04(self):
        '''品牌微网右上角模板库'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')  # 登陆
        try:
            self.driver.find_element_by_xpath(navigation['品牌微网xpath']).click()
            self.logger.info('点击品牌微网')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(flash['页面返回id']))
            self.logger.info('点击产品中心页面跳转成功')
        except:
            self.assertEqual(1,2,msg='点击品牌微网页面未跳转成功')
        try:
            startMethod.action_Id(self,logoV['品牌微网更多id'],'click')
            self.logger.info('点击更多')
            time.sleep(2)
            startMethod.action_Id(self,logoV['模板库id'],'click')
            self.logger.info('点击模板库')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(logoV['模板库下一步id']))
            startMethod.action_Id(self,logoV['模板库下一步id'],'click')
        except:
            self.assertEqual(1,2,msg='页面未跳转成功')
        try:
            WebDriverWait(self,3).until(lambda driver:self.driver.find_element_by_id(logoV['模板库下一步id']))
            startMethod.action_Id(self, logoV['模板库下一步id'], 'click')
        except:
            self.assertEqual(1,2,msg='网络异常')
    def test05(self):
        '''品牌微网/模板库/自定义模板'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')  # 登陆
        try:
            self.driver.find_element_by_xpath(navigation['品牌微网xpath']).click()
            self.logger.info('点击品牌微网')
            startMethod.action_Id(self, logoV['品牌微网更多id'], 'click')
            self.logger.info('点击品牌微网更多')
            startMethod.action_Id(self, logoV['模板库id'], 'click')
            self.logger.info('点击模板库id')
            self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/iv_item_template_library_logo')[0].click()
            self.logger.info('选择自定义模板')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_elements_by_id(flash['首页知道啦id']))
            startMethod.action_Id(self,flash['首页知道啦id'],'click')
            self.logger.info('品牌微网/模板库/自定义模板/知道啦处理完毕')
        except:
            self.assertEqual(1,2,msg='页面跳转失败')
    def test06(self):
        '''圈子引导页'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')  # 登陆
        try:
            startMethod.action_Id(self,bottom['圈子id'],'click')
            self.logger.info('点击圈子')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(flash['首页知道啦id']))
            self.logger.info('页面跳转成功')
        except:
            self.assertEqual(1,2,msg='页面跳转失败')
        try:
            startMethod.action_Id(self,flash['首页知道啦id'],'click')
            time.sleep(1)
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(flash['首页知道啦id']))
            self.assertEqual(1,2,msg='点击圈子知道啦，引导页未消失')
        except:
            self.logger.info('引导页消失')
    def test07(self):
        '''圈子/项目圈/右下角加好(我的项目)'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')  # 登陆
        try:
            startMethod.action_Id(self,bottom['圈子id'],'click')
            self.logger.info('点击圈子')
        except:
            self.assertEqual(1,2,msg='页面跳转失败')
        try:
            startMethod.action_Id(self,circle['项目圈id'],'click')
            startMethod.action_Id(self,circle['加号id'],'click')
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(flash['首页知道啦id']))
            self.logger.info('点击圈子“加号”，页面跳转成功')
        except:
            self.assertEqual(1,2,msg='页面未跳转成功')
        try:
            startMethod.action_Id(self,flash['首页知道啦id'],'click')
            self.logger.info('点击知道啦')
            startMethod.action_Id(self,flash['页面返回id'],'click')
            self.logger.info('点击返回')
        except:
            self.assertEqual(1,2,msg='点击知道了，引导页未消失')
    def test08(self):
        '''每日待办引导页'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')  # 登陆
        try:
            self.driver.find_element_by_xpath(navigation['每日待办xpath']).click()

            self.logger.info('点击每日待办')
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(flash['首页知道啦id']))
        except:
            self.assertEqual(1,2,msg='页面跳转失败')
        try:
            startMethod.action_Id(self,flash['首页知道啦id'],'click')
            startMethod.action_Id(self,flash['页面返回id'],'click')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(navigation['换一批id']))
            self.logger.info('每日待办引导页处理完毕')
        except:
            self.assertEqual(1,2,msg='每日待办引导页处理，返回失败')
    def test09(self):
        '''消息引导页'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')  # 登陆
        try:
            startMethod.action_Id(self,bottom['消息id'],'click')
            startMethod.action_Id(self,flash['首页知道啦id'],'click')
        except:
            self.assertEqual(1,2,msg='草，太晚了，就这么低，点击失败报错了')














