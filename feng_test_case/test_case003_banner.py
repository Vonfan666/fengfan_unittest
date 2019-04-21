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
    def test_01(self):
        '''验证首页轮播图标识个数'''
        self.logger.info('*****************************************************')
        startMethod.loginYiZhiBang(self,'13590283182','123456')
        bannerCode=self.driver.find_elements_by_xpath('//android.widget.LinearLayout[@resource-id=\"com.henji.yunyi.yizhibang:id/loPageTurningPoint\"]/android.widget.ImageView')#获取轮播图个数
        self.logger.info('获取轮播图个数标识符为{}'.format(len(bannerCode)))
        self.assertEqual(len(bannerCode),3,msg='进入首页之后，获取轮播图个数不为3')
        self.logger.info('判定轮播图个数为3个，符合预期')
    def test_02(self):
        '''验证轮播图1页面跳转'''
        self.logger.info('*****************************************************')
        startMethod.loginYiZhiBang(self,'13590283182','123456')
        self.driver.find_element_by_xpath(banner['图1xpath']).click()#点击第一个标识
        self.logger.info('点击第一张轮播图进入内页面')
        #验证是否出现第一张轮播图内容
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/title'))
            self.logger.info('检测到title为：{}'.format(self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/title').text))
            # 获取轮播图1内页顶部text
            textCode = self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/title').text
            self.logger.info('获取内页顶部text为：{}'.format(textCode))
        except:
            self.assertEqual(1,2,msg='10s内未获取到该title，页面加载异常')

        try: #检测是否能获取到该页面其他元素
            self.driver.find_element_by_id('player-bigBtn').click()
            self.logger.info('点击播放按钮')
            time.sleep(10)
            self.logger.info('等待10s')
            self.driver.find_element_by_id('player-bigBtn')
            self.logger.info('继续获取播放按钮')
            self.assertEqual(1, 2, msg='点击播放按钮视频没有播放，任然可以获取到播放按钮')
        except:
            self.logger.info('视频正常播放')
        self.assertEqual(textCode, banner['图1text'], msg='点击第一张轮播图进行跳转内页顶部text与预期不相符')
    def test_03(self):
        '''验证轮播图2页面跳转'''
        self.logger.info('*****************************************************')
        startMethod.loginYiZhiBang(self,'13590283182','123456')
        try:
            WebDriverWait(self,3).until(lambda driver:self.driver.find_element_by_id(bottom['首页id']))
            startMethod.toachSweip(self, 0.9, 0.1, 0.1, 0.1)
            self.driver.find_element_by_xpath(banner['图2xpath']).click()  # 点击第二个标识
            self.logger.info('点击第二张轮播图进入内页面')
            WebDriverWait(self,5).until(lambda driver: self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/title'))
            self.logger.info('成功获取到第二张轮播图的title')
            WebDriverWait(self,5).until(lambda driver:self.driver.find_element_by_xpath('//android.view.View[@resource-id=\"btnGoToOrder\"]'))
            self.logger.info('成功获取到第二张轮播图的底部“询底价”')
            WebDriverWait(self,5).until(lambda driver:self.driver.find_element_by_xpath('//android.view.View[@content-desc=\" 400-872-9169\"]'))
            self.logger.info('成功获取到第二张轮播图的底部“联系方式”')
            # 验证是否出现第二张轮播图内容
            textCode01=self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/title').text
            self.logger.info('第二张轮播图的顶部title为:{}'.format(textCode01))
            self.assertEqual(textCode01,banner['图2text'],msg='获取的第二张轮播图内页顶部text与预期不一致')
        except:  #报错处理
            self.assertEqual(1,2,msg='异常情况，该用例执行不成功')
    def test_04(self):
        '''验证轮播图3页面跳转'''
        self.logger.info('*****************************************************')
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        try:
            WebDriverWait(self, 3).until(lambda driver: self.driver.find_element_by_id(bottom['首页id']))
            startMethod.toachSweip(self, 0.9, 0.1, 0.1, 0.1)
            startMethod.toachSweip(self, 0.9, 0.1, 0.1, 0.1)
            self.driver.find_element_by_xpath(banner['图3xpath']).click()  # 点击第二个标识
            self.logger.info('点击第二张轮播图进入内页面')
            try:
                WebDriverWait(self,5).until(lambda driver:self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/title'))
                textCode2=self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/title').text
                self.logger.info('成功获取第三张轮播图title：{},页面跳转成功'.format(textCode2))
            except Exception as f:
                self.assertEqual(1,2,msg='报错信息：'+ f + ',未获取到title')
        except:
            self.assertEqual(1,2,msg="脚本执行失败，异常")
    def test_05(self):
        '''验证第三章轮播图车型数量'''
        '''验证轮播图3页面跳转'''
        self.logger.info('*****************************************************')
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        try:
            WebDriverWait(self, 3).until(lambda driver: self.driver.find_element_by_id(bottom['首页id']))
            startMethod.toachSweip(self, 0.9, 0.1, 0.1, 0.1)
            startMethod.toachSweip(self, 0.9, 0.1, 0.1, 0.1)
            self.driver.find_element_by_xpath(banner['图3xpath']).click()  # 点击第二个标识
            self.logger.info('点击第三张轮播图进入内页面')

            try:
                self.driver.find_element_by_xpath('//android.view.View[@content-desc=\"收起\"]').click()
                time.sleep(2)
                listMath=self.driver.find_elements_by_xpath('//android.view.View/android.widget.ListView/android.view.View[1]')
                self.assertEqual(len(listMath),11,msg='获取车型数量不等于11，不符合预期11个')
            except Exception as f:
                self.assertEqual(1, 2, msg='未获取到title'+'报错信息：' + f)
        except:
            self.assertEqual(1, 2, msg='报错信息：' + f + ',未获取到title')

if __name__=='__main__':
    unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(Test_banner('test_01'))
    suite.addTest(Test_banner('test_02'))
    suite.addTest(Test_banner('test_03'))
    suite.addTest(Test_banner('test_04'))
    suite.addTest(Test_banner('test_05'))

    pathCode = 'C:\\Users\\feng\Desktop\python01\\fengfan_unittest\\feng_test_result\\'
    curTime=time.strftime('%Y%m%d%H%M%S',time.localtime())
    report_path = pathCode+curTime+'.html'
    report_set = open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=report_set,title=u'自动化测试报告',description=u'用例执行情况：')
    runner.run(suite)
    report_set.close()


