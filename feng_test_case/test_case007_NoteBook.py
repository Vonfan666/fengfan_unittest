from fengfan_unittest.startAPP import *
from fengfan_unittest.feng_test_method.method import *
from fengfan_unittest.feng_test_method.actioning import *
from selenium.webdriver.support.ui import WebDriverWait
from fengfan_unittest.feng_test_conf.feng_test_env.feng_test_config import *
import  unittest,requests,HTMLTestRunner,os,time,random
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC


# time = time.strftime('%d%H%M%S', time.localtime())


class  Test_banner07(unittest.TestCase,object):
    def setUp(self):
        start_App.__init__(self)
        start_App.setUp(self)
        time.sleep(3)

    def tearDown(self):
        startMethod.backCode(self)
        start_App.tearDown(self)
    def test01(self):
        '''每日待办：验证页面跳转'''
        startMethod.loginYiZhiBang(self,'13590283182','123456')#登录
        ActionMethod.NoteBook(self)#进入每日待办
    def test02(self):
        '''新建待办默认提示验证'''
        startMethod.loginYiZhiBang(self,'13590283182','123456')#登录
        ActionMethod.NoteBook(self)#进入每日待办
        try:
            startMethod.action_Id(self,case07['新建id'],'click')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case07['新建保存id']))
            self.logger.info('页面跳转成功')
        except:
            self.assertEqual(1,2,msg='页面未跳转成功')
        newText=self.driver.find_element_by_id(case07['新建输入框id']).text
        self.logger.info('获取到默认提示为：{}'.format(newText))
        self.assertEqual(titleMethod.duQu_Exlce(self,'case07',1,2),newText,msg='新建默认提示不一致')
    def test03(self):
        '''新建待办：输入文字保存,不选择提醒'''
        startMethod.loginYiZhiBang(self,'13590283182','123456')#登录
        ActionMethod.NoteBook(self)#进入每日待办
        try:
            startMethod.action_Id(self,case07['新建id'],'click')

            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case07['新建保存id']))
            self.logger.info('页面跳转成功')
        except:
            self.assertEqual(1,2,msg='页面未跳转成功')
        try:
            startMethod.action_Id(self,case07['新建输入框id'],titleMethod.duQu_Exlce(self,'case07',2,2))#输入内容
            startMethod.action_Id(self,case07['新建保存id'],'click')
            WebDriverWait(self,299).until(lambda driver:self.driver.find_element_by_id(case07['闹钟推迟id']))
            self.assertEqual(1,2,msg='未设置闹钟提醒，获取到提醒，不符合需求')
        except:

            self.logger.info('未设置闹钟提醒，没有闹钟提醒，符合需求')
    def test04(self):
        '''验证正常删除闹钟'''
        startMethod.loginYiZhiBang(self,'13590283182','123456')#登录
        ActionMethod.NoteBook(self)#进入每日待办
        try:
            startMethod.action_Id(self,case07['新建id'],'click')

            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case07['新建保存id']))
            self.logger.info('页面跳转成功')
        except:
            self.assertEqual(1,2,msg='页面未跳转成功')
        try:#添加待办后删除
            timeC=time.strftime('%Y%m%d%H%M%S',time.localtime())
            textC=titleMethod.duQu_Exlce(self, 'case07', 2, 2)+timeC#预输入文字
            startMethod.action_Id(self, case07['新建输入框id'],textC)  # 输入内容
            startMethod.action_Id(self,case07['新建图片id'],'click')#点击上传图片
            startMethod.action_Id(self,flash['从相册选择id'],'click')#点击从相册选择
            self.driver.find_elements_by_id(case07['安卓图片id'])[0].click()#选择安卓图片
            startMethod.action_Id(self,case07['安卓图片选择完成id'],'click')#点击完成
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case07['新建保存id']))#获取判断页面返回
            startMethod.action_Id(self,case07['新建保存id'],'click')#点击保存
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case07['新建id']))#获取新建id
            self.logger.info('输入内容、上传图片，点击保存成功，返回每日待办首页')
            # startMethod.scroll_resourceId(self,case07['待办区域列表id'],textC)#待办首页滑动查找元素
            startMethod.scroll_my(self, 0.5, 0.9, 0.5, 0.5, '//android.widget.TextView[@text="{}"]'.format(textC),60)
            elementCode=self.driver.find_element_by_xpath('//android.widget.TextView[@text="{}"]'.format(textC))#定位元素textc
            startMethod.longClear(self,elementCode,1000)#长按这个元素
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(flash['确定id']))#获取确定id
            startMethod.action_Id(self,flash['确定id'],'click')
            self.logger.info('删除成功')
        except:
            self.assertEqual(1,2,msg='添加图片删除，流程验证异常')
        try:
            startMethod.action_Id(self, flash['页面返回id'], 'click')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_xpath(navigation['素材xpath']))

            self.logger.info('返回成功')
            self.driver.find_element_by_xpath(navigation['每日待办xpath']).click()
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case07['新建id']))
            self.logger.info('页面手动刷新成功')
        except:
            self.assertEqual(1,2,msg='网络异常')
        try:
            # startMethod.scroll_resourceId(self, case07['待办区域列表id'], '早上七点半起床20171122190213')  # 待办首页滑动查找元素
            startMethod.scroll_my(self, 0.5, 0.9, 0.5, 0.5, '//android.widget.TextView[@text="{}"]'.format(textC),60)
            self.assertEqual(1,2,'删除之后，任然可以获取到元素，删除失败')
        except:
            self.logger.info('删除元素正常')
    def test05(self):
        '''验证：闹钟提醒、待办日程、历史日程、'''
        startMethod.loginYiZhiBang(self,'13590283182','123456')#登录
        ActionMethod.NoteBook(self)#进入每日待办
        try:
            startMethod.action_Id(self,case07['新建id'],'click')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case07['新建保存id']))
            self.logger.info('页面跳转成功')
        except:
            self.assertEqual(1,2,msg='页面未跳转成功')
        try:#输入内容
            timeC = time.strftime('%Y%m%d%H%M%S', time.localtime())
            textC = titleMethod.duQu_Exlce(self, 'case07', 2, 2) + timeC  # 预输入文字
            startMethod.action_Id(self, case07['新建输入框id'], textC)  # 输入内容
            startMethod.action_Id(self, case07['新建图片id'], 'click')  # 点击上传图片
            startMethod.action_Id(self, flash['从相册选择id'], 'click')  # 点击从相册选择
            self.driver.find_elements_by_id(case07['安卓图片id'])[0].click()  # 选择安卓图片
            startMethod.action_Id(self, case07['安卓图片选择完成id'], 'click')  # 点击完成
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case07['新建保存id']))  # 获取判断页面返回
            startMethod.action_Id(self,case07['开关id'],'click')#点击开关，打开闹钟
            time.sleep(1)
            # toastText=titleMethod.duQu_Exlce(self,'case07',3,2)#预获取toast信息读取
            # startMethod.find_toast(self,toastText)#验证是否获取toast
            # self.logger.info('获取到toast：{}'.format(toastText))
            startMethod.action_Id(self, case07['新建保存id'], 'click')  # 点击保存,默认重复提醒一次，准时提醒
        except:
            self.assertEqual(1,2,msg='添加日程失败')
        try:#验证待办日程
            self.logger.info('******************************验证待办日程')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case07['新建id']))
            self.driver.find_element_by_xpath(case07['日程列表xpath']).click()
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case07['历史日程id']))
            startMethod.action_Id(self, case07['待办日程id'], 'click')
            xpath='//android.widget.TextView[@resource-id="com.henji.yunyi.yizhibang:id/item_schedule_calendar_content" and @text="{}"]'.format(textC)
            self.logger.info('获取xpath为：{}'.format(xpath))
            startMethod.scroll_my(self, 0.5, 0.9, 0.5, 0.3, xpath, 60)#滑动查找元素
            self.logger.info('获取到待办历程:{}'.format(textC))
            startMethod.action_Id(self,flash['页面返回id'],'click')
        except:
            self.assertEqual(1,2,msg='添加待办历程之后，进入又上角设置，查看待办历程成功')
        try:#等待闹钟响起，并关闭闹钟
            self.logger.info('**********************************验证闹钟响起和关闭')
            WebDriverWait(self,299).until(lambda driver:self.driver.find_element_by_id(case07['闹钟关闭id']))
            startMethod.action_Id(self,case07['闹钟关闭id'],'click')
            self.logger.info('收到闹钟提醒，完美')
        except:
            self.assertEqual(1,2,msg='设置五分钟之后提醒，五分钟之后未获取到闹钟提醒')
        try:#验证历史日程
            self.logger.info('*********************************验证历史日程')
            self.driver.find_element_by_xpath(case07['日程列表xpath']).click()
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case07['历史日程id']))
            startMethod.action_Id(self,case07['历史日程id'],'click')
            xpathCode='//android.widget.TextView[@text="{}"]'.format(textC)
            startMethod.scroll_my(self,0.5,0.9,0.5,0.3,xpathCode,60)
            self.driver.find_element_by_xpath('//android.widget.TextView[@text="{}"]'.format(textC))
            self.logger.info('关闭闹钟之后，在历史日程中获取到该项：{}'.format(textC))
            self.logger.info('**********************************验证闹钟响起和关闭')
        except:
            self.assertEqual(1,2,msg='验证历史日程失败')
    def test06(self):
        '''验证历史日程修改'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')  # 登录
        ActionMethod.NoteBook(self)  # 进入每日待办
        try:
            startMethod.action_Id(self, case07['新建id'], 'click')
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case07['新建保存id']))
            self.logger.info('页面跳转成功')
        except:
            self.assertEqual(1, 2, msg='页面未跳转成功')
        try:  #创建日程
            timeC = time.strftime('%Y%m%d%H%M%S', time.localtime())
            textC = titleMethod.duQu_Exlce(self, 'case07', 2, 2) + timeC  # 预输入文字
            startMethod.action_Id(self, case07['新建输入框id'], textC)  # 输入内容
            startMethod.action_Id(self, case07['新建图片id'], 'click')  # 点击上传图片
            startMethod.action_Id(self, flash['从相册选择id'], 'click')  # 点击从相册选择
            self.driver.find_elements_by_id(case07['安卓图片id'])[0].click()  # 选择安卓图片
            startMethod.action_Id(self, case07['安卓图片选择完成id'], 'click')  # 点击完成
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case07['新建保存id']))  # 获取判断页面返回
            startMethod.action_Id(self, case07['开关id'], 'click')  # 点击开关，打开闹钟
            time.sleep(1)
            # toastText=titleMethod.duQu_Exlce(self,'case07',3,2)#预获取toast信息读取
            # startMethod.find_toast(self,toastText)#验证是否获取toast
            # self.logger.info('获取到toast：{}'.format(toastText))
            startMethod.action_Id(self, case07['新建保存id'], 'click')  # 点击保存,默认重复提醒一次，准时提醒
        except:
            self.assertEqual(1, 2, msg='添加日程失败')
        try:  # 验证待办日程
            self.logger.info('******************************验证待办日程')
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case07['新建id']))
            self.driver.find_element_by_xpath(case07['日程列表xpath']).click()
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case07['历史日程id']))
            startMethod.action_Id(self, case07['待办日程id'], 'click')
            xpath = '//android.widget.TextView[@resource-id="com.henji.yunyi.yizhibang:id/item_schedule_calendar_content" and @text="{}"]'.format(
                textC)
            self.logger.info('获取xpath为：{}'.format(xpath))
            startMethod.scroll_my(self, 0.5, 0.9, 0.5, 0.3, xpath, 60)  # 滑动查找元素
            self.logger.info('获取到待办历程:{}'.format(textC))
            startMethod.action_Id(self, flash['页面返回id'], 'click')
        except:
            self.assertEqual(1, 2, msg='添加待办历程之后，进入又上角设置，查看待办历程成功')
        try:  # 等待闹钟响起，并关闭闹钟
            self.logger.info('**********************************验证闹钟响起和关闭')
            WebDriverWait(self, 299).until(lambda driver: self.driver.find_element_by_id(case07['闹钟关闭id']))
            startMethod.action_Id(self, case07['闹钟关闭id'], 'click')
            self.logger.info('收到闹钟提醒，完美')
        except:
            self.assertEqual(1, 2, msg='设置五分钟之后提醒，五分钟之后未获取到闹钟提醒')
        try:  # 验证关闭闹钟之后，是否存在历史日程
            self.logger.info('*********************************验证历史日程')
            self.driver.find_element_by_xpath(case07['日程列表xpath']).click()
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case07['历史日程id']))
            startMethod.action_Id(self, case07['历史日程id'], 'click')
            xpathCode = '//android.widget.TextView[@text="{}"]'.format(textC)
            startMethod.scroll_my(self, 0.5, 0.9, 0.5, 0.3, xpathCode, 60)
            self.driver.find_element_by_xpath('//android.widget.TextView[@text="{}"]'.format(textC))
            self.logger.info('关闭闹钟之后，在历史日程中获取到该项：{}'.format(textC))
        except:
            self.assertEqual(1, 2, msg='验证历史日程失败')
        try:#获取历史日程的title ****************************************************************************************
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case07['历史日程id']))
            startMethod.action_Id(self, case07['历史日程id'], 'click')
            n=random.randint(0,5)
            itemList=self.driver.find_elements_by_id(case07['历史日程列表id'])
            itemText=itemList[n].text#获取第N个元素的text
            itemList[n].click()#点击第N个元素
        except:
            self.assertEqual(1,2,msg='获取历史日程title失败')
        try:#验证页面跳转到历史日程编辑页面
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case07['删除id']))
            self.logger.info('页面跳转到每日待办成功')
        except:
            self.assertEqual(1,2,msg='跳转到编辑页面失败')
        try:#编辑历史日程
            startMethod.action_Id(self,case07['修改id'],'click')
            self.logger.info('点击修改')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case07['新建保存id']))
            self.logger.info('页面跳转成功，获取到保存id')
            self.driver.find_element_by_id(case07['新建输入框id']).clear()#删除输入框内容
            timeC01 = time.strftime('%Y%m%d%H%M%S', time.localtime())
            textC01 = titleMethod.duQu_Exlce(self, 'case07', 2, 2) + timeC01 # 预输入文字
            startMethod.action_Id(self, case07['新建输入框id'], textC01)  # 输入内容
            self.driver.find_element_by_xpath(case07['计划开始xpath']).click()#点击计划开始时间准备选择时间
            self.logger.info('点击计划开始时间，准备选择时间')
            startMethod.clickXY(self,685,1240)#点击更换时间
            self.logger.info('点击更换时间成功')
            time.sleep(1)
            startMethod.action_Id(self, case07['计划开始确定id'], 'click')#上滑选择时间
            self.logger.info('点击确定')
            startMethod.action_Id(self,case07['新建保存id'],'click')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case07['历史日程id']))
        except:
            self.assertEqual(1, 2, msg='编辑历史日程失败')
        try:#编辑历史日程之后，验证在历史日程无法搜索到编辑之后的title
            xpathCode = '//android.widget.TextView[@text="{}"]'.format(textC)
            startMethod.scroll_my(self, 0.5, 0.9, 0.5, 0.3, xpathCode, 60)
            self.assertEqual(1,2,msg='搜索到已编辑的历史日程，异常')
        except:
            self.logger.info('未搜索到已编辑的历史日程，正常')
        try:#验证无法搜索到编辑之前的元素
            xpathCode = '//android.widget.TextView[@text="{}"]'.format(itemText)
            startMethod.scroll_my(self, 0.5, 0.9, 0.5, 0.3, xpathCode, 60)
            self.assertEqual(1, 2, msg='搜索到编辑之前的历史日程，异常')
        except:
            self.logger.info('未搜索到编辑之前的历史日程')
        try:#验证在每日待办首页，可以搜索到编辑后的历史日程
            startMethod.action_Id(self, flash['页面返回id'], 'click')
            xpathCode01 = '//android.widget.TextView[@text="{}"]'.format(textC)
            startMethod.scroll_my(self, 0.5, 0.9, 0.5, 0.3, xpathCode01, 60)
            self.logger.info('历史日程编辑成功')
        except:
            self.assertEqual(1,2,msg='未获取到已编辑的历史日程，编辑历史日程失败')
    def test07(self):
        '''验证历史日程删除'''
        startMethod.loginYiZhiBang(self,'13590283182','123456')#登录
        ActionMethod.NoteBook(self)#进入每日待办
        try:#删除日程
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case07['新建id']))
            self.driver.find_element_by_xpath(case07['日程列表xpath']).click()
            startMethod.action_Id(self,case07['历史日程id'],'click')#点击历史日程id
            itemList = self.driver.find_elements_by_id(case07['历史日程列表id'])#获取所有的title
            firstText=itemList[0].text#获取第一个title的名称
            self.logger.info('获取第一个title的标题:{}'.format(firstText))
            self.driver.find_elements_by_id(case07['历史日程列表id'])[0].click()#点击第一个title
            startMethod.action_Id(self,case07['删除id'],'click')
            startMethod.action_Id(self,flash['确定id'],'click')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case07['历史日程id']))
        except:
            self.assertEqual(1,2,msg='删除日程，执行异常')
        try:
            xpathCode = '//android.widget.TextView[@text="{}"]'.format(firstText)
            startMethod.scroll_my(self,0.5,0.9,0.5,0.4,xpathCode,60)
            self.assertEqual(1,2,msg='删除元素历史日程只有任然可以获取到该日程，删除失败')
        except:
            self.logger.info('删除成功')
    def test08(self):
        '''验证待办日程修改'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')  # 登录
        ActionMethod.NoteBook(self)  # 进入每日待办
        try:#添加待办日程
            startMethod.action_Id(self, case07['新建id'], 'click')
            timeC = time.strftime('%Y%m%d%H%M%S', time.localtime())
            textC = titleMethod.duQu_Exlce(self, 'case07', 2, 2) + timeC  # 预输入文字
            startMethod.action_Id(self, case07['新建输入框id'], textC)  # 输入内容
            startMethod.action_Id(self, case07['新建图片id'], 'click')  # 点击上传图片
            startMethod.action_Id(self, flash['从相册选择id'], 'click')  # 点击从相册选择
            self.driver.find_elements_by_id(case07['安卓图片id'])[0].click()  # 选择安卓图片
            startMethod.action_Id(self, case07['安卓图片选择完成id'], 'click')  # 点击完成
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case07['新建保存id']))  # 获取判断页面返回\
            startMethod.action_Id(self, case07['新建保存id'], 'click')
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case07['新建id']))
        except:
            self.assertEqual(1, 2, msg="网络异常")

        try:#修改待办日程
            xpathCode = '//android.widget.TextView[@text="{}"]'.format(textC)
            startMethod.scroll_my(self,0.5,0.9,0.5,0.4,xpathCode,20)
            self.driver.find_element_by_xpath(xpathCode).click()
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case07['删除id']))
            startMethod.action_Id(self,case07['修改id'],'click')
            self.driver.find_element_by_id(case07['新建输入框id']).clear()  # 删除输入框内容
            timeC3 = time.strftime('%Y%m%d%H%M%S', time.localtime())
            textC3 = titleMethod.duQu_Exlce(self, 'case07', 2, 2) + timeC3  # 预输入文字
            startMethod.action_Id(self,case07['新建输入框id'],textC3)
            startMethod.action_Id(self, case07['新建保存id'], 'click')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case07['新建id']))
            self.logger.info('修改待办日程完成')
        except:
            self.assertEqual(1,2,msg='网络异常')
        try:#验证每日待办首页存在已修改的日程
            xpathCode = '//android.widget.TextView[@text="{}"]'.format(textC3)
            startMethod.scroll_my(self, 0.5, 0.9, 0.5, 0.4, xpathCode, 20)
            self.logger.info('首页搜索到已修改的日程')
        except:
            self.assertEqual(1,2,msg='修改待办日程失败')
        try:#每日待办首页，搜索之前的日程
            xpathCode = '//android.widget.TextView[@text="{}"]'.format(textC)
            startMethod.scroll_my(self, 0.5, 0.9, 0.5, 0.4, xpathCode, 20)
            self.assertEqual(1,2,msg='可以搜索到修改前后的日程，异常')
        except:
            self.logger.info('没毛病')

        try:#验证每日待办日程存在该日程
            self.driver.find_element_by_xpath(case07['日程列表xpath']).click()
            xpathCode = '//android.widget.TextView[@text="{}"]'.format(textC3)
            startMethod.scroll_my(self, 0.5, 0.9, 0.5, 0.4, xpathCode, 20)
            self.logger.info('每日待办搜索到已修改的待办')
        except:
            self.assertEqual(1,2,msg='网络异常')
        try:#待办日程搜索之前的日程
            xpathCode = '//android.widget.TextView[@text="{}"]'.format(textC)
            startMethod.scroll_my(self, 0.5, 0.9, 0.5, 0.4, xpathCode, 20)
            self.assertEqual(1, 2, msg='可以搜索到修改前后的日程，异常')
        except:
            self.logger.info('没毛病')
    def test09(self):
        '''验证待办日程删除'''
        startMethod.loginYiZhiBang(self,'13590283182','123456')#登录
        ActionMethod.NoteBook(self)#进入每日待办
        try:
            startMethod.action_Id(self,case07['新建id'],'click')
            timeC = time.strftime('%Y%m%d%H%M%S', time.localtime())
            textC = titleMethod.duQu_Exlce(self, 'case07', 2, 2) + timeC  # 预输入文字
            startMethod.action_Id(self, case07['新建输入框id'], textC)  # 输入内容
            startMethod.action_Id(self, case07['新建图片id'], 'click')  # 点击上传图片
            startMethod.action_Id(self, flash['从相册选择id'], 'click')  # 点击从相册选择
            self.driver.find_elements_by_id(case07['安卓图片id'])[0].click()  # 选择安卓图片
            startMethod.action_Id(self, case07['安卓图片选择完成id'], 'click')  # 点击完成
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case07['新建保存id']))  # 获取判断页面返回\
            startMethod.action_Id(self, case07['新建保存id'], 'click')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case07['新建id']))
        except:
            self.assertEqual(1,2,msg="网络异常")
        try:
            self.driver.find_element_by_xpath(case07['日程列表xpath']).click()
            self.logger.info('点击日程列表')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case07['历史日程列表id']))
            xpathCode = '//android.widget.TextView[@text="{}"]'.format(textC)
            startMethod.scroll_my(self,0.5,0.9,0.5,0.4,xpathCode,60)#滑动搜索该元素
            self.logger.info('在待办日程中搜索新添加的日程')
            self.driver.find_element_by_xpath(xpathCode).click()#点击该元素
            self.logger.info('点击该日程')
            startMethod.action_Id(self,case07['删除id'],'click')
            startMethod.action_Id(self,flash['确定id'],'click')
        except:
            self.assertEqual(1, 2, msg="网络异常")
        try:
            startMethod.scroll_my(self, 0.5, 0.9, 0.5, 0.4, xpathCode, 60)  # 删除之后滑动搜索该元素
            self.assertEqual(1,2,msg='删除待办日程失败')
        except:
            self.logger.info('删除待办日程成功')






















