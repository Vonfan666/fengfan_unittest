import unittest,time
from fengfan_unittest.startAPP import *
from fengfan_unittest.feng_test_method.method import *
import  unittest,requests,HTMLTestRunner
from fengfan_unittest.feng_test_conf.feng_test_env.feng_test_config import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        '''验证品牌微网页面正常跳转'''
        self.logger.info('****************************************')
        startMethod.loginYiZhiBang(self,a='13590283182',b='123456')
        self.driver.find_element_by_xpath(navigation['品牌微网xpath']).click()
        try:
            startMethod.action_Id(self,flash['首页我知道啦id'],'click')
        except:
            try:
            #获取品牌微网title

                titleCode=startMethod.action_Id(self,'com.henji.yunyi.yizhibang:id/tv_title','obtain').text
                self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"关于我们\"]')#验证是否能获取到关于我们栏目
                self.logger.info("获取品牌微网：‘关于我们’")
                self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"产品中心\"]')#验证是否能获取到产品中心栏目
                self.logger.info("获取品牌微网：‘产品中心’")
                self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"新闻动态\"]')#验证是否能获取到新闻动态栏目
                self.logger.info("获取品牌微网：‘新闻动态’")
                self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"视频中心\"]')#验证是否能获取到视频中心栏目
                self.logger.info("获取品牌微网：‘视频中心’")
                self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"招商加盟\"]')#验证是否能获取到招商加盟栏目
                self.logger.info("获取品牌微网：‘招商加盟’")
                self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"联系我们\"]')#验证是否能获取到联系我们栏目
                self.logger.info("获取品牌微网：‘联系我们’")

                textTel = self.driver.find_element_by_android_uiautomator(
                    'new UiSelector().className("android.widget.TextView").text("易直帮号")')
                textTelMath = self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/tv_micro_brand_id')
                self.logger.info('获取 "{0}" 为:{1} '.format(textTel.text, textTelMath.text))
                #判断是否获取左下角阅读量
                textMath2=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.henji.yunyi.yizhibang:id/brand_read_num").textContains("阅读")')
                self.logger.info('获取品牌微网左下角阅读量{}'.format(textMath2.text))
                self.logger.info('获取品牌微网的title为：{}'.format(titleCode))
                self.assertEqual(titleCode,'品牌微网',msg='品牌微网顶部title错误')
            except:
                self.assertEqual(1,2,msg='未获取到品牌微网内页相关元素，报错!')
    def test02(self):
        '''验证品牌微网用户昵称修改'''
        self.logger.info('****************************************')
        startMethod.loginYiZhiBang(self, a='13590283182', b='123456')
        self.driver.find_element_by_xpath(navigation['品牌微网xpath']).click()
        try:
            startMethod.action_Id(self, flash['首页知道啦id'], 'click')
        except:
            try:
                oldNameCode=self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/tv_micro_brand_name').text#获取原始昵称
            except:
                oldNameCode='未填写昵称'
        self.logger.info('获取到原来的用户昵称：{}'.format(oldNameCode))
        self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/rl_brand_index_container').click()#点击进入信息编辑页面
        self.logger.info('进入信息编辑页面')
        self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"姓名\"]').click()#点击编辑姓名
        self.logger.info('点击编辑姓名')
        NameCode='冯凡'+time.strftime('%d%H%M%S', time.localtime())
        startMethod.action_Id(self,'com.henji.yunyi.yizhibang:id/et_dialog_input_content',NameCode)#输入姓名
        startMethod.action_Id(self,'com.henji.yunyi.yizhibang:id/btn_dialog_input_confirm','click')#点击确认
        try: #判断toast是否存在
            startMethod.find_toast(self,'成功')
        except:
            self.logger.info('不存在该toast')
        startMethod.action_Id(self,'com.henji.yunyi.yizhibang:id/tv_back','click')#点击返回到品牌微网首页
        self.logger.info('点击“返回”回到品牌微网首页')

        newNameCode=self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/tv_micro_brand_name').text
        self.logger.info('初始昵称为：{0}，输入更改的昵称为：{1}，输入完成之后首页展示的昵称为:{2}'.format(oldNameCode,NameCode,newNameCode))
        self.assertEqual(newNameCode,NameCode,msg='输入姓名完成之后，回到品牌微网首页，输入与显示昵称不一致')
    def test03(self):
        '''验证公司名称更改'''
        self.logger.info('****************************************')
        startMethod.loginYiZhiBang(self, a='13590283182', b='123456')
        self.driver.find_element_by_xpath(navigation['品牌微网xpath']).click()
        try:
            startMethod.action_Id(self, flash['首页知道啦id'], 'click')
        except:
            self.logger.info('未获取到“我知道啦”')
        try:
            WebDriverWait(self,5,0.1).until(lambda driver:self.driver.find_element_by_xpath('com.henji.yunyi.yizhibang:id/tv_micro_brand_name'))
            company=self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/tv_micro_brand_company').text
        except:
            company='公司名称为空'
        self.logger.info('获取到原来的公司名称：{}'.format(company))
        self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/rl_brand_index_container').click()#点击进入信息编辑页面
        self.logger.info('进入信息编辑页面')
        self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"公司\"]').click()  # 点击编辑公司名称
        self.logger.info('点击编辑公司名称')
        companyNameCode ='云易恒基'+time.strftime('%d%H%M%S', time.localtime())#随机公司名称云易恒基+时间戳
        startMethod.action_Id(self, 'com.henji.yunyi.yizhibang:id/et_dialog_input_content', companyNameCode)  # 输入姓名
        startMethod.action_Id(self, 'com.henji.yunyi.yizhibang:id/btn_dialog_input_confirm', 'click')  # 点击确认
        try: #判断toast是否存在
            startMethod.find_toast(self,'成功')
        except:
            self.logger.info('不存在该toast')
        startMethod.action_Id(self, 'com.henji.yunyi.yizhibang:id/tv_back', 'click')  # 点击返回到品牌微网首页
        self.logger.info('点击“返回”回到品牌微网首页')

        newCompanyNameCode = self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/tv_micro_brand_company').text
        self.logger.info('初始昵称为：{0}，输入更改的昵称为：{1}，输入完成之后首页展示的昵称为:{2}'.format(company, companyNameCode, newCompanyNameCode))
        self.assertEqual(newCompanyNameCode, companyNameCode, msg='输入姓名完成之后，回到品牌微网首页，输入与显示昵称不一致')
    def test04(self):
        '''验证职务更改'''
        self.logger.info('****************************************')
        startMethod.loginYiZhiBang(self, a='13590283182', b='123456')
        WebDriverWait(self,5,0.1).until(lambda driver:self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/tv_home_exchange'))
        self.driver.find_element_by_xpath(navigation['品牌微网xpath']).click()
        try:
            startMethod.action_Id(self,flash['首页知道啦id'], 'click')
        except:
            self.logger.info('未获取到“我知道啦”')
        try:
            a=self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/tv_micro_brand_job')
            oldJob =a.text
        except:
            oldJob='所属职务为空'
        self.logger.info('获取到原来的职务：{}'.format(oldJob))
        self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/rl_brand_index_container').click()#点击进入信息编辑页面
        self.logger.info('进入信息编辑页面')
        self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"职务\"]').click()  # 点击编辑公司名称
        self.logger.info('点击编辑公司名称')
        job = '测试' + time.strftime('%d%H%M%S', time.localtime())  # 随机公司名称云易恒基+时间戳
        startMethod.action_Id(self, 'com.henji.yunyi.yizhibang:id/et_dialog_input_content',job)  # 输入姓名
        startMethod.action_Id(self, 'com.henji.yunyi.yizhibang:id/btn_dialog_input_confirm', 'click')  # 点击确认
        try:  # 判断toast是否存在
            startMethod.find_toast(self,'成功')
        except:
            self.logger.info('不存在该toast')
        startMethod.action_Id(self, 'com.henji.yunyi.yizhibang:id/tv_back', 'click')  # 点击返回到品牌微网首页
        self.logger.info('点击“返回”回到品牌微网首页')

        newJob = self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/tv_micro_brand_job').text
        self.logger.info(
            '初始昵称为：{0}，输入更改的昵称为：{1}，输入完成之后首页展示的昵称为{2}'.format(oldJob,job, newJob))
        self.assertEqual(job,newJob, msg='输入姓名完成之后，回到品牌微网首页，输入与显示昵称不一致')
    def test05(self):
        '''验证电话号码输入'''
        self.logger.info('****************************************')
        startMethod.loginYiZhiBang(self, a='13590283182', b='123456')
        self.driver.find_element_by_xpath(navigation['品牌微网xpath']).click()
        try:
            startMethod.action_Id(self, flash['首页知道啦id'], 'click')
        except:
            self.logger.info('未获取到“我知道啦”')
        try:
            self.driver.find_element_by_id(
                'com.henji.yunyi.yizhibang:id/rl_brand_index_container').click()  # 点击进入信息编辑页面
            self.logger.info('进入信息编辑页面')

            oldTel=self.driver.find_element_by_android_uiautomator('new UiSelector().className(\"android.widget.TextView\").textContains(\"135\").resourceId(\"com.henji.yunyi.yizhibang:id/tv_list_item_content\")').text
            self.logger.info('获取到原来的tel：{}'.format(oldTel))
        except:
            oldTel = '电话为空'
        self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"电话\"]').click()
        self.logger.info('点击电话，进入修改tel页面')
        self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/et_dialog_input_content').clear()
        tel='135'+time.strftime('%d%H%M%S', time.localtime())
        startMethod.action_Id(self,'com.henji.yunyi.yizhibang:id/et_dialog_input_content',tel)
        self.logger.info('输入的账号为：{}'.format(tel))
        startMethod.action_Id(self, 'com.henji.yunyi.yizhibang:id/btn_dialog_input_confirm', 'click')  # 点击确认
        try:  # 判断toast是否存在
            startMethod.find_toast(self,'成功')
        except:
            self.logger.info('不存在该toast')
        newTel=self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]').text
        self.logger.info('初始tel：{0}，输入tel：{1}，显示的tel：{2}'.format(oldTel,tel,newTel))
        self.assertEqual(tel,newTel,msg='电话号码输入与显示不一致，异常')
    # def test06(self):
    #     '''权限定位pass'''
    #     pass
    def test07(self):
        '''微信二维码'''
        self.logger.info('****************************************')
        startMethod.loginYiZhiBang(self, a='13590283182', b='123456')
        self.driver.find_element_by_xpath(navigation['品牌微网xpath']).click()
        try:
            startMethod.action_Id(self, flash['首页知道啦id'], 'click')
        except:
            self.logger.info('未获取到“我知道啦”')
        self.driver.find_element_by_id(
            'com.henji.yunyi.yizhibang:id/rl_brand_index_container').click()  # 点击进入信息编辑页面
        self.logger.info('进入信息编辑页面')
        startMethod.action_Id(self,'com.henji.yunyi.yizhibang:id/rl_brand_index_qr_code_container','click')
        try:
            self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id=\"android:id/text1\" and @text=\"相册\"]').click()
            self.driver.find_element_by_xpath(
                '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/miui.view.ViewPager[1]/'
                'android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]'
            ).click()
            startMethod.action_Id(self,'com.miui.gallery:id/ok','click')
            try:  # 判断toast是否存在
                startMethod.find_toast(self,'这不是一个有效的二维码图片')
            except:
                self.logger.info('不存在该toast')
            # startMethod.action_Id(self, 'com.henji.yunyi.yizhibang:id/tv_preview_brand_back', 'click')  # 点击二级返回
        except:
            self.assertEqual(1,2,msg='异常退出，重新执行该用例')
    def test08(self):
        '''预览模块，验证码个人信息是否与主页面一致'''
        self.logger.info('****************************************')
        startMethod.loginYiZhiBang(self, a='13590283182', b='123456')
        self.driver.find_element_by_xpath(navigation['品牌微网xpath']).click()#点击品牌微网
        name=self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/tv_micro_brand_name').text
        self.logger.info('获取姓名为：{}'.format(name))
        nameTel=self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/tv_micro_brand_id').text
        self.logger.info('获取易直帮号为：{}'.format(nameTel))
        job=self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/tv_micro_brand_job').text
        self.logger.info('获取职务为：{}'.format(job))
        companyName=self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/tv_micro_brand_company').text
        self.logger.info('获取公司名称为：{}'.format(companyName))
        self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/iv_brand_preview').click()#点击预览
        try:
            #预览页获取昵称
            self.driver.find_element_by_xpath('//android.view.View[@content-desc=\"{}\"]'.format(name))
            self.driver.find_element_by_xpath('//android.view.View[@content-desc=\"{}\"]'.format("易直帮号："+nameTel))
            self.driver.find_element_by_xpath('//android.view.View[@content-desc=\"{}\"]'.format(("所属职务：")+job))
            self.driver.find_element_by_xpath('//android.view.View[@content-desc=\"{}\"]'.format("公司名称："+companyName))
            startMethod.action_Id(self,'com.henji.yunyi.yizhibang:id/tv_preview_brand_back','click')#点击二级返回
            self.logger.info('预览页面获取到用户昵称:{0}、易直帮号:{1}、所属职务:{2}、公司名称{3}、且与主页面一致！'.format(name,nameTel,job,companyName))
        except:
            self.assertEqual(1,2,msg='使用主页面元素，获取预览页元素发生异常')
    def test09(self):
        '''获取六个栏目内容是否存在以及加载'''
        self.logger.info('****************************************')
        startMethod.loginYiZhiBang(self, a='13590283182', b='123456')
        self.driver.find_element_by_xpath(navigation['品牌微网xpath']).click()  # 点击品牌微网
        self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/iv_brand_preview').click()
        try:
            self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[1]/android.widget.ListView[1]')
            self.logger.info('获取到"关于我们"')
            self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[1]/android.widget.ListView[2]')
            self.logger.info('获取到“产品中心”')
            self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[2]/android.widget.ListView[1]')
            self.logger.info('获取到“新闻动态”')
            self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[2]/android.widget.ListView[2]')
            self.logger.info('获取到“视频中心”')
            self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[3]/android.widget.ListView[1]')
            self.logger.info('获取到“招商加盟”')
            self.driver.find_element_by_xpath('//android.widget.ListView/android.view.View[3]/android.widget.ListView[2]')
            self.logger.info('获取到“关于我们”')
            startMethod.action_Id(self, 'com.henji.yunyi.yizhibang:id/tv_preview_brand_back', 'click')  # 点击二级返回
        except:
            self.assertEqual(1,2,msg='预览页面六个栏目获取异常')
    def test10(self):
        '''获取底部导航栏'''
        self.logger.info('****************************************')
        startMethod.loginYiZhiBang(self, a='13590283182', b='123456')
        self.driver.find_element_by_xpath(navigation['品牌微网xpath']).click()  # 点击品牌微网
        self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/iv_brand_preview').click()

        try:
            self.driver.find_element_by_xpath('//android.view.View[@content-desc=\"p 进入首页\"]')
            self.driver.find_element_by_xpath('//android.view.View[@content-desc=\"p 拨打电话\"]')
            self.driver.find_element_by_xpath('//android.view.View[@content-desc=\"p 地图导航\"]')
            self.driver.find_element_by_xpath('//android.view.View[@content-desc=\"p 注册微网\"]')
            startMethod.action_Id(self, 'com.henji.yunyi.yizhibang:id/tv_preview_brand_back', 'click')  # 点击二级返回
            self.logger.info('成功获取到品牌微网预览页面，底部四个导航栏目')

        except:
            self.assertEqual(1,2,msg='获取品牌微网预览页面，底部导航栏异常')
    # def test11(self):
    #     '''品牌微网预览页面微网注册'''
    #     pass





