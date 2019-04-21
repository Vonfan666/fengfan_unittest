import unittest,time
from fengfan_unittest.startAPP import *
from fengfan_unittest.feng_test_method.method import *
import  unittest,requests,HTMLTestRunner,os
from fengfan_unittest.feng_test_conf.feng_test_env.feng_test_config import *
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
import random,time

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
        '''验证软文推广页面跳转成功'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        self.driver.find_element_by_xpath(navigation['推广软文xpath']).click()
        try:
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(flash['页面返回id']))
            self.logger.info('进入主页，点击软文推广，十秒内获取到返回按钮，页面正常跳转成功')
        except:
            self.assertEqual(1,2,msg='进入主页，点击软文推广，十秒内未获取到返回按钮，页面跳转失败')
    def test02(self):
        '''验证软文推广下滑正常'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        self.driver.find_element_by_xpath(navigation['推广软文xpath']).click()
        try:
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(flash['页面返回id']))
            self.logger.info('进入主页，点击软文推广，十秒内获取到返回按钮，页面正常跳转成功')
            firstText=self.driver.find_elements_by_id(titleMethod.duQu_Exlce(self,'case05',2,2))[0].text
            self.logger.info('获取到firstText为：{}'.format(firstText))
            mathCode=0
            while mathCode<20: #页面滑动十次
                mathCode=mathCode+1
                startMethod.toachSweip(self,0.5,0.9,0.5,0.2)
            try:
                WebDriverWait(self,3).until(lambda driver:self.driver.find_element_by_xpath('//android.widget.TextView[@text="{}"]'.format(firstText)))
                self.assertEqual(1,2,msg='软文推广，页面滑动失败')
            except:
                self.logger.info('页面滑动成功')
        except:
            self.assertEqual(1,2,msg='进入主页，点击软文推广，十秒内未获取到返回按钮，页面跳转失败')
    def test03(self):
        '''验证软文推广/热文/分类下滑搜索元素正常'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        self.driver.find_element_by_xpath(navigation['推广软文xpath']).click()
        self.logger.info('点击软文推广')
        try:
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case05['新增文章id']))
            self.logger.info('获取有下角“+”标识')
        except:
            self.assertEqual(1, 2, msg='点击“推广软文”，链接未正常跳转')
        try:
            xpathCode=titleMethod.duQu_Exlce(self,'case05',1,2)
            self.logger.info('获取指定文章')
            startMethod.scroll_my(self,0.5,0.8,0.5,0.3,xpathCode,'1000').click()
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/title'))
            titleText=self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/title').text
            self.assertEqual(titleText,'文章详情',msg='获取xpath之后，点击链接未正确跳转')
        except:
            self.assertEqual(1,2,msg='未成功获取到，xpath该文章')
    def test04(self):
        '''验证搜素精确搜索功能'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath(navigation['推广软文xpath']))
            self.driver.find_element_by_xpath(navigation['推广软文xpath']).click()
            try:
                WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(flash['页面返回id']))
                print('1')
                startMethod.action_Id(self,titleMethod.duQu_Exlce(self,'case05',3,2),'click')#点击搜索按钮
                try:
                    WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"取消\"]'))#十秒内获取页面是否获取到页面跳转后的元素
                    self.logger.info('获取到“取消”按钮,页面跳转成功',)

                    startMethod.action_Id(self,titleMethod.duQu_Exlce(self,'case05',5,2),titleMethod.duQu_Exlce(self,'case05',6,2))#输入搜索内容
                    time.sleep(3)
                    os.system('adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME')#切换小米输入法
                    startMethod.action_Id(self,titleMethod.duQu_Exlce(self,'case05',5,2),'click')
                    os.system('adb shell input keyevent 66')#点击搜索
                    os.system('adb shell ime set io.appium.android.ime/.UnicodeIME')#切换appium输入法
                    try:
                        WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/advertorial_article_title'))
                        text=self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/advertorial_article_title').text
                        self.logger.info('精确搜索到文章：{}'.format(text))
                        self.assertEqual(text,titleMethod.duQu_Exlce(self,'case05',6,2))
                    except:
                        self.assertEqual(1,2,msg='未搜索到文章')
                    self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"取消\"]').click()
                except:
                    self.assertEqual(1,2,msg='未获取到“取消”按钮，页面未跳转成功')
            except:
                self.assertEqual(1, 2, msg='进入主页，点击软文推广，十秒内未获取到返回按钮，页面跳转失败')
        except:
            self.assertEqual(1,2,msg='登录失败')
    def test05(self):
        '''验证软文推荐模糊搜素'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath(navigation['推广软文xpath']))
            self.driver.find_element_by_xpath(navigation['推广软文xpath']).click()
            try:
                WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(flash['页面返回id']))
                print('1')
                startMethod.action_Id(self,titleMethod.duQu_Exlce(self,'case05',3,2),'click')#点击搜索按钮
                try:
                    WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"取消\"]'))#十秒内获取页面是否获取到页面跳转后的元素
                    self.logger.info('获取到“取消”按钮,页面跳转成功',)

                    startMethod.action_Id(self,titleMethod.duQu_Exlce(self,'case05',5,2),'微信')#输入搜索内容“微信”
                    time.sleep(3)
                    os.system('adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME')#切换小米输入法
                    startMethod.action_Id(self,titleMethod.duQu_Exlce(self,'case05',5,2),'click')
                    os.system('adb shell input keyevent 66')#点击搜索
                    os.system('adb shell ime set io.appium.android.ime/.UnicodeIME')#切换appium输入法上
                    try:
                        WebDriverWait(self,10).until(lambda driver:self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/advertorial_article_title'))
                        textsList=self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/advertorial_article_title')
                        for texts in textsList:
                            self.logger.info('模糊搜索到文章：{}'.format(texts.text))
                            self.assertIn('微信',texts.text,msg='搜索都不包含‘微信’关键字的文章')
                    except:
                        self.assertEqual(1,2,msg='未搜索到文章')
                    self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"取消\"]').click()
                except:
                    self.assertEqual(1,2,msg='未获取到“取消”按钮，页面未跳转成功')
            except:
                self.assertEqual(1, 2, msg='进入主页，点击软文推广，十秒内未获取到返回按钮，页面跳转失败')
        except:
            self.assertEqual(1,2,msg='登录失败')
    def test06(self):
        '''验证更多分类功能页面展开'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath(navigation['推广软文xpath']))
            self.driver.find_element_by_xpath(navigation['推广软文xpath']).click()
            try:
                WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(flash['页面返回id']))

                startMethod.action_Id(self,case05['选择分类id'],'click')#点击搜索按钮
                WebDriverWait(self,10).until(lambda driver:self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/article_category_name'))
                textCode=self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/article_category_name')
                for  text in textCode:
                    self.logger.info('获取到栏目：{}'.format(text.text))

            except:
                self.assertEqual(1, 2, msg='进入主页，点击软文推广，十秒内未获取到返回按钮，页面跳转失败,或打开更多分类异常')
        except:
            self.assertEqual(1,2,msg='登录失败')
        try:
            WebDriverWait(self, 10).until(
                lambda driver: self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/article_category_name'))
            startMethod.action_Id(self, case05['选择分类id'], 'click')  # 点击搜索按钮
            self.logger.info('收起更多分类')
        except:
            self.logger.info('用例执行完毕，准备退出')
    def test07(self):
        '''验证更多功能正常收起'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath(navigation['推广软文xpath']))
            self.driver.find_element_by_xpath(navigation['推广软文xpath']).click()
            try:
                WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(flash['页面返回id']))

                startMethod.action_Id(self,case05['选择分类id'],'click')#点击搜索按钮
                WebDriverWait(self,10).until(lambda driver:self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/article_category_name'))
                textCode=self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/article_category_name')
                for  text in textCode:
                    self.logger.info('获取到栏目：{}'.format(text.text))
            except:
                self.assertEqual(1, 2, msg='进入主页，点击软文推广，十秒内未获取到返回按钮，页面跳转失败,或打开更多分类异常')
        except:
            self.assertEqual(1,2,msg='登录失败')
        try:
            WebDriverWait(self, 10).until(
                lambda driver: self.driver.find_elements_by_id(case05['选择分类id']))
            startMethod.action_Id(self, case05['选择分类id'], 'click')  # 点击搜索按钮
            self.logger.info('收起更多分类')
            try:
                WebDriverWait(self, 10).until(lambda driver: self.driver.find_elements_by_id(
                    'com.henji.yunyi.yizhibang:id/article_category_name'))
                textCode = self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/article_category_name')
                for text in textCode:
                    self.logger.info('获取到栏目：{}'.format(text.text))
                self.assertEqual(1,2,msg='收起更多分类功能页面之后，任然可以获取到分类名称，收起页面失败')
            except:
                self.logger.info('收起更多分类之后，获取分类名称失败，符合预期，正常！')
        except:
            self.logger.info('用例执行完毕，准备退出')
    def test08(self):
        '''验证选择更多分类'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath(navigation['推广软文xpath']))
            self.driver.find_element_by_xpath(navigation['推广软文xpath']).click()
            try:
                WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(flash['页面返回id']))

                startMethod.action_Id(self,case05['选择分类id'],'click')#点击展开更多分类
                WebDriverWait(self,10).until(lambda driver:self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/article_category_name'))#获取分类名称验证是否展开
                self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"儿童教育\"]').click()
                WebDriverWait(self,10).until(lambda driver:self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/advertorial_article_title'))#获取title
                textCode=self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/advertorial_article_title')#获取所有儿童教育的文章元素
                for text in textCode:
                    self.logger.info('获取到儿童教育内页text：{}'.format(text.text))
            except:
                self.assertEqual(1, 2, msg='进入主页，点击软文推广，十秒内未获取到返回按钮，页面跳转失败,或打开更多分类异常')
        except:
            self.assertEqual(1,2,msg='登录失败')
        try:
            WebDriverWait(self, 10).until(
                lambda driver: self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/article_category_name'))
            startMethod.action_Id(self, case05['选择分类id'], 'click')  # 点击搜索按钮
            self.logger.info('收起更多分类')
        except:
            self.logger.info('用例执行完毕，准备退出')
    def test09(self):
        '''验证软文推广右下角+文章编辑/自编文章,
        验证不输入文章内容点击保存，返回
        '''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath(navigation['推广软文xpath']))
            self.driver.find_element_by_xpath(navigation['推广软文xpath']).click()
            try:
                WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(flash['页面返回id']))
            except:
                self.assertEqual(1, 2, msg='进入主页，点击软文推广，十秒内未获取到返回按钮，页面跳转失败,或打开更多分类异常')
        except:
            self.assertEqual(1,2,msg='登录失败')
        startMethod.action_Id(self,case05['新增文章id'],'click')#点击右下角“+”按钮
        self.logger.info('点击右下角“+”按钮')
        WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath(case05['自编文章xpath']))#十秒内搜索并点击自编文章
        self.driver.find_element_by_xpath(case05['自编文章xpath']).click()
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case05['保存id']))#十秒内获取“保存”按钮，验证页面是否成功跳转
            self.logger.info('获取到保存按钮')
            startMethod.action_Id(self,case05['保存id'],'click')#点击保存按钮
            startMethod.find_toast(self,titleMethod.duQu_Exlce(self,'case05',8,2))#验证是否获取到toast：“添加标题图片toast”
        except:
            self.assertIn(1,2,msg='点击自编文章未获取到“保存”按钮，页面未跳转成功！')
        startMethod.action_Id(self,case05['返回id'],'click')
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case05['确定id']))
            self.driver.find_element_by_id(case05['确定id']).click()
            self.assertEqual(1,2,msg='没有输入内容，不点击保存，直接退出，获取到了是否确定保存，不符合需求，应该直接退出')
        except:
            self.logger.info('不输入内容，直接点击返回，没有提示是否保存，符合需求')
    def test10(self):
        '''验证软文推广右下角+文章编辑/自编文章,
        验证输入文章内容点击保存
        '''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath(navigation['推广软文xpath']))
            self.driver.find_element_by_xpath(navigation['推广软文xpath']).click()
            try:
                WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(flash['页面返回id']))
            except:
                self.assertEqual(1, 2, msg='进入主页，点击软文推广，十秒内未获取到返回按钮，页面跳转失败,或打开更多分类异常')
        except:
            self.assertEqual(1,2,msg='登录失败')
        startMethod.action_Id(self,case05['新增文章id'],'click')#点击右下角“+”按钮
        self.logger.info('点击右下角“+”按钮')
        WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath(case05['自编文章xpath']))#十秒内搜索并点击自编文章
        self.driver.find_element_by_xpath(case05['自编文章xpath']).click()#点击自编文章，进入文章编辑页面
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case05['保存id']))#十秒内获取“保存”按钮，验证页面是否成功跳转
            self.logger.info('获取到保存按钮')
            self.driver.find_element_by_xpath(case05['自编文章输入框xpath']).click()#点击输入框
            os.system('adb shell  input text "{}"'.format(titleMethod.duQu_Exlce(self,'case05',7,2)))#输入内容
            self.logger.info('输入内容为：{}'.format(titleMethod.duQu_Exlce(self,'case05',7,2)))
            startMethod.action_Id(self,case05['保存id'],'click')#点击保存按钮
            startMethod.find_toast(self,titleMethod.duQu_Exlce(self,'case05',8,2))#验证是否获取到toast：“添加标题图片toast”
        except:
            self.assertIn(1,2,msg='点击自编文章未获取到“保存”按钮，页面未跳转成功！')
        startMethod.action_Id(self,case05['返回id'],'click')
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case05['确定id']))
            self.logger.info('获取到确定按钮')
            self.driver.find_element_by_id(case05['确定id']).click()
        except:
            self.assertEqual(1,2,msg='输入文章直接点击保存，然后点击返回按钮，未获取到“确定按钮”，不符合需求')
    def test11(self):
        '''验证我的页面跳转
        验证上传图片，不输入标题保存
        '''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath(navigation['推广软文xpath']))
            self.driver.find_element_by_xpath(navigation['推广软文xpath']).click()
            try:
                WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(flash['页面返回id']))
            except:
                self.assertEqual(1, 2, msg='进入主页，点击软文推广，十秒内未获取到返回按钮，页面跳转失败,或打开更多分类异常')
        except:
            self.assertEqual(1,2,msg='登录失败')
        startMethod.action_Id(self,case05['新增文章id'],'click')#点击右下角“+”按钮
        self.logger.info('点击右下角“+”按钮')
        WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath(case05['自编文章xpath']))#十秒内搜索并点击自编文章
        self.driver.find_element_by_xpath(case05['自编文章xpath']).click()
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case05['保存id']))#十秒内获取“保存”按钮，验证页面是否成功跳转
            self.logger.info('获取到保存按钮')
            self.driver.find_element_by_xpath(case05['自编文章输入框xpath']).click()
            os.system('adb shell  input text "{}"'.format(titleMethod.duQu_Exlce(self,'case05',7,2)))
            startMethod.action_Id(self,case05['基本信息id'],'click')#点击底部基本信息
            try:
                startMethod.action_Id(self,case05['添加图片id'],'click')
                startMethod.action_Id(self,case05['从相册选择id'],'click')
                imageCode=self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/iv_thumb')
                n=random.randint(0,10)
                imageCode[n].click()
                startMethod.action_Id(self,case05['选择图片确定id'],'click')
                WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case05['保存id']))
                startMethod.action_Id(self,case05['保存id'],'click')
            except:
                self.assertEqual(1,2,msg='添加图片失败')
            startMethod.action_Id(self,case05['保存id'],'click')
            startMethod.find_toast(self,titleMethod.duQu_Exlce(self,'case05',10,2))#验证是否获取到toast：“添加标题图片toast”
        except:
            self.assertIn(1,2,msg='点击自编文章未获取到“保存”按钮，页面未跳转成功！')
        startMethod.action_Id(self,case05['返回id'],'click')
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case05['确定id']))
            self.driver.find_element_by_id(case05['确定id']).click()
        except:
            self.assertEqual(1,2,msg='输入文章直接点击保存，然后点击返回按钮，未获取到“确定按钮”，不符合需求')
    def test12(self):
        '''验证正常输入，不选择分组，是否正常保存，且新增文章是否置顶显示'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath(navigation['推广软文xpath']))
            self.driver.find_element_by_xpath(navigation['推广软文xpath']).click()
            try:
                WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(flash['页面返回id']))
            except:
                self.assertEqual(1, 2, msg='进入主页，点击软文推广，十秒内未获取到返回按钮，页面跳转失败,或打开更多分类异常')
        except:
            self.assertEqual(1,2,msg='登录失败')
        startMethod.action_Id(self, case05['新增文章id'], 'click')  # 点击右下角“+”按钮
        self.logger.info('点击右下角“+”按钮')
        WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath(case05['自编文章xpath']))#十秒内搜索并点击自编文章
        self.driver.find_element_by_xpath(case05['自编文章xpath']).click()
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case05['保存id']))#十秒内获取“保存”按钮，验证页面是否成功跳转
            self.logger.info('获取到保存按钮')
            self.driver.find_element_by_xpath(case05['自编文章输入框xpath']).click()
            os.system('adb shell  input text "{}"'.format(titleMethod.duQu_Exlce(self,'case05',7,2)))
            startMethod.action_Id(self,case05['基本信息id'],'click')#点击底部基本信息
        except:
            self.assertEqual(1,2,msg='点击自编文章页面未跳转成功')
        try:
            startMethod.action_Id(self,case05['添加图片id'],'click')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case05['从相册选择id']))
            startMethod.action_Id(self,case05['从相册选择id'],'click')
            imageCode=self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/iv_thumb')#获取当前页面所有的图片list id
            n=random.randint(0,10)
            imageCode[n].click()
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case05['选择图片确定id']))
            startMethod.action_Id(self,case05['选择图片确定id'],'click')#点击上传图片
            WebDriverWait(self, 10).until(
            lambda driver: self.driver.find_element_by_id(case05['保存id']))  # 验证图片上传成功，获取到保存id
        except:
            self.assertEqual(1,2,msg='上传图片失败')
        try:
            timeCode = time.strftime('%Y%m%d%H%M%S', time.localtime())
            textCode = titleMethod.duQu_Exlce(self, 'case05', 11, 2) + timeCode  # 输入内容为关键字驱动加时间戳
            startMethod.action_Id(self, case05['文章标题id'], textCode)
            startMethod.action_Id(self, case05['保存id'], 'click')
            WebDriverWait(self,10).until(lambda driver:startMethod.action_Id(self,case05['新增文章id'],'obtain'))
            self.logger.info('输入文章内容、上传图片、添加标题，文章保存成功')
        except:
            self.assertEqual(1,2,msg='新增文章保存失败')
        titleText=self.driver.find_elements_by_id(case05['我的_标题id'])[0]
        self.logger.info('获取到我的_文章标题为：{}'.format(titleText.text))
        textCode1=self.driver.find_elements_by_id(case05['文章所属分组id'])[0]
        self.logger.info('获取到分组名称为：{}'.format(textCode1.text))
        self.assertEqual(textCode,titleText.text,msg='新添加的文章没有在“我的”页面，置顶显示')
        self.assertEqual(titleMethod.duQu_Exlce(self,'case05',12,2),textCode1.text,msg='不选择分组添加文章，该文章没有放到默认分组里面')
    def test13(self):
        '''验证正常输入，选择分组，是否正常保存，且新增文章是否置顶显示'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath(navigation['推广软文xpath']))
            self.driver.find_element_by_xpath(navigation['推广软文xpath']).click()
            try:
                WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(flash['页面返回id']))
            except:
                self.assertEqual(1, 2, msg='进入主页，点击软文推广，十秒内未获取到返回按钮，页面跳转失败,或打开更多分类异常')
        except:
            self.assertEqual(1,2,msg='登录失败')
        startMethod.action_Id(self, case05['新增文章id'], 'click')  # 点击右下角“+”按钮
        self.logger.info('点击右下角“+”按钮')
        WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath(case05['自编文章xpath']))#十秒内搜索并点击自编文章
        self.driver.find_element_by_xpath(case05['自编文章xpath']).click()
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case05['保存id']))#十秒内获取“保存”按钮，验证页面是否成功跳转
            self.logger.info('获取到保存按钮')
            self.driver.find_element_by_xpath(case05['自编文章输入框xpath']).click()
            os.system('adb shell  input text "{}"'.format(titleMethod.duQu_Exlce(self,'case05',7,2)))
            startMethod.action_Id(self,case05['基本信息id'],'click')#点击底部基本信息
        except:
            self.assertEqual(1,2,msg='点击自编文章页面未跳转成功')
        try:#上传图片
            startMethod.action_Id(self,case05['添加图片id'],'click')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case05['从相册选择id']))
            startMethod.action_Id(self,case05['从相册选择id'],'click')
            imageCode=self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/iv_thumb')#获取当前页面所有的图片list id
            n=random.randint(0,10)
            imageCode[n].click()
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case05['选择图片确定id']))
            startMethod.action_Id(self,case05['选择图片确定id'],'click')#点击上传图片
            WebDriverWait(self, 10).until(
            lambda driver: self.driver.find_element_by_id(case05['保存id']))  # 验证图片上传成功，获取到保存id
        except:
            self.assertEqual(1,2,msg='上传图片失败')
        try:#选择分组
            self.driver.find_element_by_android_uiautomator(case05['分组class_text']).click()
            groupName = self.driver.find_elements_by_id(case05['分组分类id'])[1].text
            self.driver.find_elements_by_id(case05['分组分类id'])[1].click()#添加文章时，选取第二个分组

        except:
            self.assertEqual(1,2,msg='选取分组失败')
        try:
            timeCode = time.strftime('%Y%m%d%H%M%S', time.localtime())
            textCode = titleMethod.duQu_Exlce(self, 'case05', 11, 2) + timeCode  # 输入内容为关键字驱动加时间戳
            startMethod.action_Id(self, case05['文章标题id'], textCode)
            startMethod.action_Id(self, case05['保存id'], 'click')
            WebDriverWait(self,10).until(lambda driver:startMethod.action_Id(self,case05['新增文章id'],'obtain'))
            self.logger.info('输入文章内容、上传图片、添加标题，文章保存成功')
        except:
            self.assertEqual(1,2,msg='新增文章保存失败')
        titleText=self.driver.find_elements_by_id(case05['我的_标题id'])[0]
        self.logger.info('获取到我的_文章标题为：{}'.format(titleText.text))
        textCode1=self.driver.find_elements_by_id(case05['文章所属分组id'])[0]
        self.logger.info('获取到分组名称为：{}'.format(textCode1.text))
        self.assertEqual(textCode,titleText.text,msg='新添加的文章没有在“我的”页面，置顶显示')
        self.assertEqual(groupName,textCode1.text,msg='不选择分组添加文章，该文章没有放到默认分组里面')
    def test14(self):
        '''新增文章选择自定义分组
        验证正常输入，选择分组，是否正常保存，且新增文章是否置顶显示'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath(navigation['推广软文xpath']))
            self.driver.find_element_by_xpath(navigation['推广软文xpath']).click()
        except:
            self.assertEqual(1,2,msg='登录失败')
        try:
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(flash['页面返回id']))
        except:
            self.assertEqual(1, 2, msg='进入主页，点击软文推广，十秒内未获取到返回按钮，页面跳转失败,或打开更多分类异常')
        startMethod.action_Id(self, case05['新增文章id'], 'click')  # 点击右下角“+”按钮
        self.logger.info('点击右下角“+”按钮')
        WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath(case05['自编文章xpath']))#十秒内搜索并点击自编文章
        self.driver.find_element_by_xpath(case05['自编文章xpath']).click()
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case05['保存id']))#十秒内获取“保存”按钮，验证页面是否成功跳转
            self.logger.info('获取到保存按钮')
            self.driver.find_element_by_xpath(case05['自编文章输入框xpath']).click()
            os.system('adb shell  input text "{}"'.format(titleMethod.duQu_Exlce(self,'case05',7,2)))
            startMethod.action_Id(self,case05['基本信息id'],'click')#点击底部基本信息
        except:
            self.assertEqual(1,2,msg='点击自编文章页面未跳转成功')
        try:#上传图片
            startMethod.action_Id(self,case05['添加图片id'],'click')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case05['从相册选择id']))
            startMethod.action_Id(self,case05['从相册选择id'],'click')
            imageCode=self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/iv_thumb')#获取当前页面所有的图片list id
            n=random.randint(0,10)
            imageCode[n].click()
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case05['选择图片确定id']))
            startMethod.action_Id(self,case05['选择图片确定id'],'click')#点击上传图片
            WebDriverWait(self, 10).until(
            lambda driver: self.driver.find_element_by_id(case05['保存id']))  # 验证图片上传成功，获取到保存id
        except:
            self.assertEqual(1,2,msg='上传图片失败')
        try:#添加标题
            timeCode = time.strftime('%Y%m%d%H%M%S', time.localtime())
            textCode = titleMethod.duQu_Exlce(self, 'case05', 11, 2) + timeCode  # 输入内容为关键字驱动加时间戳
            startMethod.action_Id(self, case05['文章标题id'], textCode)
            # startMethod.action_Id(self, case05['保存id'], 'click')
            # WebDriverWait(self,10).until(lambda driver:startMethod.action_Id(self,case05['新增文章id'],'obtain'))
            self.logger.info('标题添加成功')
        except:
            self.assertEqual(1,2,msg='新增文章保存失败')
        try:#选择分组
            self.driver.find_element_by_android_uiautomator(case05['分组class_text']).click()#点击选择分组
            self.driver.find_element_by_id(case05['自定义分组id']).click()  # 选择自定义分组点击
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case05['title_id']))
            startMethod.action_Id(self,case05['添加分组id'],'click')
            timeCode=time.strftime('%S', time.localtime())
            timeCode1=titleMethod.duQu_Exlce(self,'case05',13,2)+timeCode
            self.logger.info('添加分组名称为：{}'.format(timeCode1))
            startMethod.action_Id(self,case05['请输入分组名称id'],timeCode1)#输入分组名称，字符加时间戳
            startMethod.action_Id(self,'com.henji.yunyi.yizhibang:id/btn_dialog_input_confirm','click')#点击确定
        except:
            self.assertEqual(1,2,msg='选择自定义分组失败')
        try:#验证toast
            startMethod.find_toast(self,'新增分组成功')
            self.logger.info('新增自定义分组成功')
        except:
            startMethod.find_toast(self,'文章分组名称已存在')
            self.logger.info('分组名称已经存在')
        try:
            startMethod.action_Id(self,flash['页面返回id'],'click')
            self.driver.find_element_by_android_uiautomator(case05['分组class_text']).click()  # 点击选择分组
        except:
            self.assertEqual(1,2,msg='新增自定义分组之后，页面返回失败')
        try:#判断新增分组是否存在
            startMethod.scroll_resourceId(self,'com.henji.yunyi.yizhibang:id/group_list',timeCode1)
            self.driver.find_element_by_xpath('//android.widget.TextView[@text="{}"]'.format(timeCode1)).click()

            startMethod.action_Id(self, case05['保存id'], 'click')
            WebDriverWait(self, 10).until(lambda driver: startMethod.action_Id(self, case05['新增文章id'], 'obtain'))
            self.logger.info('输入文章内容、上传图片、添加标题，选择自定义分组文章保存成功')

        except:
            self.assertEqual(1,2,msg='添加自定义分组之后，选择分组，未找到该分组')

        titleText=self.driver.find_elements_by_id(case05['我的_标题id'])[0]
        self.logger.info('获取到我的_文章标题为：{}'.format(titleText.text))
        textCode1=self.driver.find_elements_by_id(case05['文章所属分组id'])[0]
        self.logger.info('获取到分组名称为：{}'.format(textCode1.text))
        self.assertEqual(textCode,titleText.text,msg='新添加的文章没有在“我的”页面，置顶显示')
        self.assertEqual(timeCode1,textCode1.text,msg='不选择分组添加文章，该文章没有放到默认分组里面')
    def test15(self):
        '''验证存在文章的分组无法删除'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        try:#登录验证
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_xpath(navigation['推广软文xpath']))
            self.driver.find_element_by_xpath(navigation['推广软文xpath']).click()
            try:
                WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(flash['页面返回id']))
            except:
                self.assertEqual(1, 2, msg='进入主页，点击软文推广，十秒内未获取到返回按钮，页面跳转失败,或打开更多分类异常')
        except:
            self.assertEqual(1, 2, msg='登录失败')
        startMethod.action_Id(self, case05['新增文章id'], 'click')  # 点击右下角“+”按钮
        self.logger.info('点击右下角“+”按钮')
        WebDriverWait(self, 10).until(
            lambda driver: self.driver.find_element_by_xpath(case05['自编文章xpath']))  # 十秒内搜索并点击自编文章
        self.driver.find_element_by_xpath(case05['自编文章xpath']).click()
        try:
            WebDriverWait(self, 10).until(
                lambda driver: self.driver.find_element_by_id(case05['保存id']))  # 十秒内获取“保存”按钮，验证页面是否成功跳转
            self.logger.info('获取到保存按钮')
            self.driver.find_element_by_xpath(case05['自编文章输入框xpath']).click()
            os.system('adb shell  input text "{}"'.format(titleMethod.duQu_Exlce(self, 'case05', 7, 2)))
            startMethod.action_Id(self, case05['基本信息id'], 'click')  # 点击底部基本信息
        except:
            self.assertEqual(1, 2, msg='点击自编文章页面未跳转成功')
        try:  # 上传图片
            startMethod.action_Id(self, case05['添加图片id'], 'click')
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case05['从相册选择id']))
            startMethod.action_Id(self, case05['从相册选择id'], 'click')
            imageCode = self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/iv_thumb')  # 获取当前页面所有的图片list id
            n = random.randint(0, 10)
            imageCode[n].click()
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case05['选择图片确定id']))
            startMethod.action_Id(self, case05['选择图片确定id'], 'click')  # 点击上传图片
            WebDriverWait(self, 10).until(
                lambda driver: self.driver.find_element_by_id(case05['保存id']))  # 验证图片上传成功，获取到保存id
        except:
            self.assertEqual(1, 2, msg='上传图片失败')
        try:  # 选择分组
            self.driver.find_element_by_android_uiautomator(case05['分组class_text']).click()
            groupName = self.driver.find_elements_by_id(case05['分组分类id'])[1].text
            self.driver.find_elements_by_id(case05['分组分类id'])[1].click()  # 添加文章时，选取第二个分组

        except:
            self.assertEqual(1, 2, msg='选取分组失败')
        try:
            timeCode = time.strftime('%Y%m%d%H%M%S', time.localtime())
            textCode = titleMethod.duQu_Exlce(self, 'case05', 11, 2) + timeCode  # 输入内容为关键字驱动加时间戳
            startMethod.action_Id(self, case05['文章标题id'], textCode)
            startMethod.action_Id(self, case05['保存id'], 'click')
            WebDriverWait(self, 10).until(lambda driver: startMethod.action_Id(self, case05['新增文章id'], 'obtain'))
            self.logger.info('输入文章内容、上传图片、添加标题，文章保存成功')
        except:
            self.assertEqual(1, 2, msg='新增文章保存失败')
        titleText = self.driver.find_elements_by_id(case05['我的_标题id'])[0]
        self.logger.info('获取到我的_文章标题为：{}'.format(titleText.text))
        textCode1 = self.driver.find_elements_by_id(case05['文章所属分组id'])[0]
        self.logger.info('获取到分组名称为：{}'.format(textCode1.text))
        self.assertEqual(textCode, titleText.text, msg='新添加的文章没有在“我的”页面，置顶显示')
        self.assertEqual(groupName, textCode1.text, msg='不选择分组添加文章，该文章没有放到默认分组里面')

        try: #验证有文章的分组无法删除
            startMethod.action_Id(self, case05['选择分类id'], 'click')  # 点击分类
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case05['自定义分组管理id']))
        except:
            self.assertEqual(1, 2, msg='我的/分组分类未跳转成功')
        listCode = self.driver.find_elements_by_id(case05['分组名称id'])
        if len(listCode) > 1:
            self.driver.find_element_by_id(case05['自定义分组管理id']).click()
            try:
                self.driver.find_elements_by_id(case05['分组删除按钮id'])[0].click()
                WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case05['删除分组二次确认id']))
                startMethod.action_Id(self, case05['删除分组二次确认id'], 'click')
            except:
                self.assertEqual(1, 2, msg='点击删除第一个分组，弹出二次确认删除失败')
            try:
                startMethod.find_toast(self, titleMethod.duQu_Exlce(self,'case05',14,2))
                self.logger.info('删除成功之后，获取到toast信息')
            except:
                self.assertEqual(1, 2, msg='删除成功之后未获取到toast')
    def test16(self):
        '''验证在我的/点击展开分组，点击分组，查看文章'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        try:#登录验证
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_xpath(navigation['推广软文xpath']))
            self.driver.find_element_by_xpath(navigation['推广软文xpath']).click()
            try:
                WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(flash['页面返回id']))
            except:
                self.assertEqual(1, 2, msg='进入主页，点击软文推广，十秒内未获取到返回按钮，页面跳转失败,或打开更多分类异常')
        except:
            self.assertEqual(1, 2, msg='登录失败')
        startMethod.action_Id(self, case05['新增文章id'], 'click')  # 点击右下角“+”按钮
        self.logger.info('点击右下角“+”按钮')
        WebDriverWait(self, 10).until(
            lambda driver: self.driver.find_element_by_xpath(case05['自编文章xpath']))  # 十秒内搜索并点击自编文章
        self.driver.find_element_by_xpath(case05['自编文章xpath']).click()
        try:
            WebDriverWait(self, 10).until(
                lambda driver: self.driver.find_element_by_id(case05['保存id']))  # 十秒内获取“保存”按钮，验证页面是否成功跳转
            self.logger.info('获取到保存按钮')
            self.driver.find_element_by_xpath(case05['自编文章输入框xpath']).click()
            os.system('adb shell  input text "{}"'.format(titleMethod.duQu_Exlce(self, 'case05', 7, 2)))
            startMethod.action_Id(self, case05['基本信息id'], 'click')  # 点击底部基本信息
        except:
            self.assertEqual(1, 2, msg='点击自编文章页面未跳转成功')
        try:  # 上传图片
            startMethod.action_Id(self, case05['添加图片id'], 'click')
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case05['从相册选择id']))
            startMethod.action_Id(self, case05['从相册选择id'], 'click')
            imageCode = self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/iv_thumb')  # 获取当前页面所有的图片list id
            n = random.randint(0, 10)
            imageCode[n].click()
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case05['选择图片确定id']))
            startMethod.action_Id(self, case05['选择图片确定id'], 'click')  # 点击上传图片
            WebDriverWait(self, 10).until(
                lambda driver: self.driver.find_element_by_id(case05['保存id']))  # 验证图片上传成功，获取到保存id
        except:
            self.assertEqual(1, 2, msg='上传图片失败')
        try:  # 选择分组
            self.driver.find_element_by_android_uiautomator(case05['分组class_text']).click()
            groupName = self.driver.find_elements_by_id(case05['分组分类id'])[1].text
            self.driver.find_elements_by_id(case05['分组分类id'])[1].click()  # 添加文章时，选取第二个分组

        except:
            self.assertEqual(1, 2, msg='选取分组失败')
        try:
            timeCode = time.strftime('%Y%m%d%H%M%S', time.localtime())
            textCode = titleMethod.duQu_Exlce(self, 'case05', 11, 2) + timeCode  # 输入内容为关键字驱动加时间戳
            startMethod.action_Id(self, case05['文章标题id'], textCode)
            startMethod.action_Id(self, case05['保存id'], 'click')
            WebDriverWait(self, 20).until(lambda driver: startMethod.action_Id(self, case05['新增文章id'], 'obtain'))
            self.logger.info('输入文章内容、上传图片、添加标题，文章保存成功')
        except:
            self.assertEqual(1, 2, msg='新增文章保存失败')
        titleText = self.driver.find_elements_by_id(case05['我的_标题id'])[0]
        self.logger.info('获取到我的_文章标题为：{}'.format(titleText.text))
        textCode1 = self.driver.find_elements_by_id(case05['文章所属分组id'])[0]
        self.logger.info('获取到分组名称为：{}'.format(textCode1.text))
        self.assertEqual(textCode, titleText.text, msg='新添加的文章没有在“我的”页面，置顶显示')
        self.assertEqual(groupName, textCode1.text, msg='不选择分组添加文章，该文章没有放到默认分组里面')
        #查看分组下面是否有该文章
        startMethod.action_Id(self,case05['选择分类id'],'click')
        self.driver.find_elements_by_id(case05['分组名称id'])[2].click()
        titleTextCode = self.driver.find_elements_by_id(case05['我的_标题id'])[0]
        self.assertEqual(titleTextCode.text,textCode,msg='添加的文章未被分配到所属分组')
    def test17(self):
        '''验证删除文章'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        self.driver.find_element_by_xpath(navigation['推广软文xpath']).click()  # 点击软文推广
        try:  # 判断页面跳转是否成功
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case05['新增文章id']))
        except:
            self.assertEqual(1, 2, msg='首页点击软文推广，页面跳转未成功')
        startMethod.action_Id(self, case05['我的id'], 'click')  # 点击我的
        try:
            titleCode = self.driver.find_elements_by_id(case05['我的_标题id'])  # 获取第一个文章
            textCode = titleCode[0]
        except:
            self.assertEqual(1, 2, msg='未获取到文章')
        try:  # 长按选中文章删除
            action = TouchAction(self.driver)
            action.press(textCode).wait(1000).release()
            action.perform()
        except:
            self.assertEqual(1, 2, msg='脚本异常')
        startMethod.action_Id(self, 'com.henji.yunyi.yizhibang:id/btn_tips_dialog_confirm', 'click')
        try:
            self.driver.find_element_by_android_uiautomator('new UiSelector().text({})'.format(textCode))
            self.assertEqual(1, 2, msg='删除未成功，任然可以搜索到删除的文章')
        except:
            self.logger.info('删除成功')
    def test18(self):
        '''验证分组删除'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        self.driver.find_element_by_xpath(navigation['推广软文xpath']).click()  # 点击软文推广
        try:  # 判断页面跳转是否成功
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case05['新增文章id']))
        except:
            self.assertEqual(1, 2, msg='首页点击软文推广，页面跳转未成功')
        try:
            startMethod.action_Id(self, case05['我的id'], 'click')#点击我的
            startMethod.action_Id(self, case05['选择分类id'], 'click')#点击分类
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case05['自定义分组管理id']))

        except:
            self.assertEqual(1,2,msg='我的/分组分类未跳转成功')
        listCode=self.driver.find_elements_by_id(case05['分组名称id'])
        if len(listCode)>1:
            self.driver.find_element_by_id(case05['自定义分组管理id']).click()#点击自定义分组
            self.logger.info('点击自定义分组管理')
            self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/add_group_rl').click()#点击添加分组
            self.logger.info('点击添加分组')
            self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/et_dialog_input_content').set_text('删除分组')
            startMethod.action_Id(self,'com.henji.yunyi.yizhibang:id/btn_dialog_input_confirm','click')

            startMethod.scroll_resourceId(self,'com.henji.yunyi.yizhibang:id/add_group_rv','删除分组')
            self.driver.find_elements_by_id(case05['分组删除按钮id'])[-1].click()
            # WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case05['删除分组二次确认id']))
            startMethod.action_Id(self,case05['删除分组二次确认id'],'click')
            try:  # 判断toast是否存在
                startMethod.find_toast(self,titleMethod.duQu_Exlce(self,'case05',15,2))
            except:
                self.logger.info('不存在该toast')
        else:
            self.assertEqual(1,2,msg='未检测到分组信息')
    def test19(self):
        '''添加异常外链文章'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        self.driver.find_element_by_xpath(navigation['推广软文xpath']).click()  # 点击软文推广
        try:  # 判断页面跳转是否成功
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case05['新增文章id']))
        except:
            self.assertEqual(1, 2, msg='首页点击软文推广，页面跳转未成功')
        try:#点击链接文章断言跳转
            startMethod.action_Id(self,case05['新增文章id'],'click')
            self.driver.find_element_by_xpath(case05['外链文章xpath']).click()
            WebDriverWait(self,10).until(lambda driver:self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/btn_add_article_ok'))
        except:
            self.assertEqual(1,2,msg='跳转到添加链接页面失败')

        try:#输入链接
            startMethod.action_Id(self,case05['外链输入框id'],titleMethod.duQu_Exlce(self,'case05',16,2))
            self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/btn_add_article_ok').click()#点击确定
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath('//android.view.View[@content-desc="读取失败，该链接内容可能有防采集保护~~"]/android.view.View[1]'))
        except:
            self.assertEqual(1,2,msg='添加异常链接，未获取到“读取失败，该链接内容可能有防采集保护~~”提示！')
        try:#退出
            startMethod.action_Id(self,case05['返回id'],'click')#点击返回id
            startMethod.action_Id(self, case05['确定id'], 'click')#返回提示，“您还未保存，确认退出吗”，二次确认按钮
        except:
            self.assertEqual(1,2,msg='输入异常链接之后，点击确认，返回失败')
    def test20(self):
        '''添加中文外链'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        self.driver.find_element_by_xpath(navigation['推广软文xpath']).click()  # 点击软文推广
        try:  # 判断页面跳转是否成功
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case05['新增文章id']))
        except:
            self.assertEqual(1, 2, msg='首页点击软文推广，页面跳转未成功')
        try:  # 点击链接文章断言跳转
            startMethod.action_Id(self, case05['新增文章id'], 'click')
            self.driver.find_element_by_xpath(case05['外链文章xpath']).click()
            WebDriverWait(self, 10).until(
                lambda driver: self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/btn_add_article_ok'))
        except:
            self.assertEqual(1, 2, msg='跳转到添加链接页面失败')

        try:  # 输入链接
            startMethod.action_Id(self, case05['外链输入框id'], titleMethod.duQu_Exlce(self, 'case05', 17, 2))
            self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/btn_add_article_ok').click()  # 点击确定
            startMethod.find_toast(self,titleMethod.duQu_Exlce(self,'case05',18,2))
        except:
            self.assertEqual(1, 2, msg='未获取到：{},这个toast提示'.format(titleMethod.duQu_Exlce(self,'case05',18,2)))
    # def test21(self):
    #     '''添加非文章链接'''
    #     startMethod.loginYiZhiBang(self, '13590283182', '123456')
    #     self.driver.find_element_by_xpath(navigation['推广软文xpath']).click()  # 点击软文推广
    #     try:  # 判断页面跳转是否成功
    #         WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case05['新增文章id']))
    #     except:
    #         self.assertEqual(1, 2, msg='首页点击软文推广，页面跳转未成功')
    #     try:  # 点击链接文章断言跳转
    #         startMethod.action_Id(self, case05['新增文章id'], 'click')
    #         self.driver.find_element_by_xpath(case05['外链文章xpath']).click()
    #         WebDriverWait(self, 10).until(
    #             lambda driver: self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/btn_add_article_ok'))
    #     except:
    #         self.assertEqual(1, 2, msg='跳转到添加链接页面失败')
    #     try:
    #         startMethod.action_Id(self, case05['外链输入框id'], titleMethod.duQu_Exlce(self, 'case05', 19, 2))
    #         self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/btn_add_article_ok').click()  # 点击确定
    #         #备注:搞不清楚这里咋可以成功，需求异常
    def test22(self):
        '''输入正确的文章链接'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        self.driver.find_element_by_xpath(navigation['推广软文xpath']).click()  # 点击软文推广
        try:  # 判断页面跳转是否成功
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case05['新增文章id']))
        except:
            self.assertEqual(1, 2, msg='首页点击软文推广，页面跳转未成功')
        try:  # 点击链接文章断言跳转
            startMethod.action_Id(self, case05['新增文章id'], 'click')
            self.driver.find_element_by_xpath(case05['外链文章xpath']).click()
            WebDriverWait(self, 10).until(
                lambda driver: self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/btn_add_article_ok'))
        except:
            self.assertEqual(1, 2, msg='跳转到添加链接页面失败')

        try:  # 输入链接
            startMethod.action_Id(self, case05['外链输入框id'], titleMethod.duQu_Exlce(self, 'case05', 20, 2))
            self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/btn_add_article_ok').click()  # 点击确定
            WebDriverWait(self,20).until(lambda driver:self.driver.find_element_by_id(case05['保存id']))
            self.driver.find_element_by_id(case05['保存id']).click()

        except:
            self.assertEqual(1,2,msg='输入链接异常')
        #验证点击保存之后第一个文章的标题
        titleCode=self.driver.find_elements_by_id(case05['我的_标题id'])
        self.assertEqual(titleCode[0].text,titleMethod.duQu_Exlce(self,'case05',21,2))












