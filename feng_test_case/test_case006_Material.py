from fengfan_unittest.startAPP import *
from fengfan_unittest.feng_test_method.method import *
from fengfan_unittest.feng_test_method.actioning import *
from selenium.webdriver.support.ui import WebDriverWait
from fengfan_unittest.feng_test_conf.feng_test_env.feng_test_config import *
import  unittest,requests,HTMLTestRunner,os,time,random
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC


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
        '''验证新增微信名片默认姓名和手机号'''
        startMethod.loginYiZhiBang(self,'13590283182','123456')
        try:
            startMethod.action_Id(self,bottom['我的id'],'click')#点击我的
            self.logger.info('点击个人中心')

            WebDriverWait(self, 10).until(
                lambda driver: self.driver.find_element_by_xpath('//android.widget.TextView[@text="设置"]'))
            self.logger.info('页面跳转成功')
        except:
            self.assertEqual(1,2,msg='页面跳转失败')
        try:
            startMethod.action_Id(self, 'com.henji.yunyi.yizhibang:id/tv_mine_name', 'click')
            nameCode=self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]').text
            self.logger.info('获取用户昵称:{}'.format(nameCode))
            tel=self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]').text
            self.logger.info('获取到用户电话：{}'.format(tel))
        except:
            self.assertEqual(1,2,msg='用户昵称和电话号码获取失败')
        startMethod.action_Id(self,flash['页面返回id'],'click')#点击页面返回
        startMethod.action_Id(self,bottom['首页id'],'click')#点击首页
        ActionMethod.Material(self)
        try:
            startMethod.action_Id(self,case06['添加id'],'click')#点击添加新的名片
            WebDriverWait(self,5).until(lambda driver:self.driver.find_element_by_id(case06['名片保存id']))
            self.logger.info('获取到名片保存id，页面跳转成功')
            nameCode01=self.driver.find_element_by_xpath(case06['姓名xpath']).text
            tel01=self.driver.find_element_by_xpath(case06['手机xpath']).text
            self.assertEqual(nameCode,nameCode01,msg='新增名片自动获取昵称与实际昵称不一致，未获取到昵称')
            self.assertEqual(tel,tel01,msg='新增名片自动获取电话号码与实际电话号码不一致，未获取到电话号码')
        except:
            self.assertEqual(1,2,msg='页面跳转失败')
        try:#页面返回
            startMethod.action_Id(self,flash['页面返回id'],'click')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case06['确定id']))
            startMethod.action_Id(self,case06['确定id'],'click')
            self.logger.info('返回到素材主页')
        except:
            self.assertEqual(1,2,msg='返回素材主页失败')
    def test02(self):
        '''验证添加名片'''
        startMethod.loginYiZhiBang(self,'13590283182','123456')
        ActionMethod.Material(self)
        try:
            startMethod.action_Id(self,case06['添加id'],'click')
            self.logger.info('点击添加微名片')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case06['名片保存id']))
            self.logger.info('页面跳转成功')
        except:
            self.assertEqual(1,2,msg='页面跳转失败')
        try:#上传图片
            startMethod.action_Id(self,case06['头像id'],'click')
            startMethod.action_Id(self, flash['从相册选择id'], 'click')#点击从相册选择
            n=random.randint(1,10)
            self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/iv_thumb')[2].click()#选择图片
            startMethod.action_Id(self,'com.henji.yunyi.yizhibang:id/menu_crop','click')#点击确认
            WebDriverWait(self,10).until(lambda driver:self.driver.find_elements_by_id(case06['名片保存id']))
            self.logger.info('上传图片成功')
        except:
            self.assertEqual(1,2,msg='上传图片失败')
        try:#更改姓名
            self.driver.find_element_by_xpath(case06['姓名xpath']).click()#点击姓名
            timeCode = time.strftime('%d%H%M%S', time.localtime())
            textCode=titleMethod.duQu_Exlce(self,'case06',1,2)+timeCode
            self.logger.info('预输入字符串为：{}'.format(textCode))
            WebDriverWait(self,3).until(lambda driver:self.driver.find_element_by_id(case06['名片输入框id']))
            self.driver.find_element_by_id(case06['名片输入框id']).set_text(textCode)#输入姓名
            startMethod.action_Id(self,case06['名片输入框确定id'],'click')#点击确定
            self.logger.info('更改姓名成功,最新姓名为：{}'.format(textCode))
        except:
            self.assertEqual(1,2,msg='更改姓名失败')
        try:#更改手机号
            self.driver.find_element_by_xpath(case06['手机xpath']).click()#点击手机号
            timeCode = time.strftime('%d%H%M%S', time.localtime())#获取时间戳
            telCode=titleMethod.duQu_Exlce(self,'case06',2,2)+timeCode#预输入号码135+八位时间戳
            self.driver.find_element_by_id(case06['名片输入框id']).set_text(telCode)#输入手机号码
            startMethod.action_Id(self,case06['名片输入框确定id'],'click')#点击确定
            self.logger.info('更改姓名成功,最新手机号码为：{}'.format(telCode))
        except:
            self.assertEqual(1,2,msg='更换手机号失败')
        try:#输入个性签名
            self.driver.find_element_by_xpath(case06['签名xpath']).click()#点击签名
            timeCode = time.strftime('%d%H%M%S', time.localtime())  # 获取时间戳
            txtCode=titleMethod.duQu_Exlce(self,'case06',3,2)+timeCode
            self.driver.find_element_by_id(case06['名片输入框id']).set_text(txtCode)#输入内容
            startMethod.action_Id(self, case06['名片输入框确定id'], 'click')  # 点击确定
        except:
            self.assertEqual(1,2,msg='输入个性签名失败')
        try:#更换地址
            startMethod.action_Id(self,case06['地址id'],'click')
            timeCode = time.strftime('%d%H%M%S', time.localtime())  # 获取时间戳
            txtCode1 = titleMethod.duQu_Exlce(self, 'case06', 4, 2) + timeCode
            startMethod.action_Id(self,case06['名片输入框id'],txtCode1)#输入内容
            startMethod.action_Id(self, case06['名片输入框确定id'], 'click')  # 点击确定
        except:
            self.assertEqual(1,2,msg='更换地址失败')
        try:#更换公司名称
            self.driver.find_element_by_xpath(case06['公司xpath']).click()
            timeCode = time.strftime('%d%H%M%S', time.localtime())  # 获取时间戳
            txtCode2 = titleMethod.duQu_Exlce(self, 'case06', 5, 2) + timeCode
            startMethod.action_Id(self, case06['名片输入框id'], txtCode2)  # 输入内容
            startMethod.action_Id(self, case06['名片输入框确定id'], 'click')  # 点击确定
            startMethod.action_Id(self,case06['名片保存id'],'click')
        except:
            self.assertEqual(1,2,msg='更换公司名称失败')
        # try:
        #     startMethod.action_Id(self,flash['页面返回id'],'click')
        #     WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case06['确定id']))
        #     self.driver.find_element_by_id(case06['名片保存id']).click()
        # except:
        #     self.assertEqual(1,2,msg='退出失败')
    def test03(self):
        '''验证只添加文字'''
        startMethod.loginYiZhiBang(self,'13590283182','123456')#登录
        ActionMethod.Material(self)#进入素材页面
        try:
            startMethod.action_Id(self,case06['文字id'],'click')#点击选择文字
            startMethod.action_Id(self,case06['添加id'],'click')#点击添加文字
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case06['文字保存id']))
            self.logger.info('页面跳转到文字输入页面')
        except:
            self.assertEqual(1,2,msg='页面跳转失败')
        try:
            startMethod.action_Id(self,case06['文字输入框id'],titleMethod.duQu_Exlce(self,'case06',6,2))#输入内容
            startMethod.action_Id(self,case06['文字保存id'],'click')#点击保存
            startMethod.find_toast(self,titleMethod.duQu_Exlce(self,'case06',7,2))#验证toast信息
            startMethod.action_Id(self,flash['页面返回id'],'click')
            WebDriverWait(self,3).until(lambda driver:self.driver.find_element_by_id(case06['确定id']))
            startMethod.action_Id(self,case06['确定id'],'click')
        except:
            self.assertEqual(1,2,msg='只输入文字内容，不输入外链，返回失败！')
    def test04(self):
        '''验证只添加外链'''
        startMethod.loginYiZhiBang(self,'13590283182','123456')#登录
        ActionMethod.Material(self)#进入素材页面
        try:
            startMethod.action_Id(self,case06['文字id'],'click')#点击选择文字
            startMethod.action_Id(self,case06['添加id'],'click')#点击添加文字
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case06['文字保存id']))
            self.logger.info('页面跳转到文字输入页面')
        except:
            self.assertEqual(1, 2, msg='页面跳转失败')
        try:
            startMethod.action_Id(self,case06['外链id'],titleMethod.duQu_Exlce(self,'case06',8,2))
            startMethod.action_Id(self, case06['文字保存id'], 'click')  # 点击保存
            startMethod.find_toast(self, titleMethod.duQu_Exlce(self, 'case06', 9, 2))  # 验证toast信息
            startMethod.action_Id(self, flash['页面返回id'], 'click')
            WebDriverWait(self, 3).until(lambda driver: self.driver.find_element_by_id(case06['确定id']))
            startMethod.action_Id(self, case06['确定id'], 'click')
        except:
            self.assertEqual(1,2,msg='只输入外链，不输入文字，返回失败')
    def test05(self):
        '''添加文字和外链'''
        startMethod.loginYiZhiBang(self,'13590283182','123456')#登录
        ActionMethod.Material(self)#进入素材页面
        try:
            startMethod.action_Id(self,case06['文字id'],'click')#点击选择文字
            startMethod.action_Id(self,case06['添加id'],'click')#点击添加文字
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case06['文字保存id']))
            self.logger.info('页面跳转到输入页面')
        except:
            self.logger.info('页面跳转到文字输入页面失败')
        try:
            startMethod.action_Id(self, case06['文字输入框id'], titleMethod.duQu_Exlce(self, 'case06', 6, 2))#输入内容
            startMethod.action_Id(self, case06['外链id'], titleMethod.duQu_Exlce(self, 'case06', 8, 2))#输入外链
            startMethod.action_Id(self, case06['文字保存id'], 'click')  # 点击保存

            WebDriverWait(self, 3).until(lambda driver: self.driver.find_element_by_id(case06['添加id']))
            self.logger.info('添加完毕')
            textList=self.driver.find_elements_by_id(case06['文字列表id'])
            text=textList[0].text
            self.assertNotEqual(text,titleMethod.duQu_Exlce(self,'case06',6,2))
        except:
            self.assertEqual(1,2,msg='添加失败')
    def test06(self):
        '''添加一张图片点击保存'''
        startMethod.loginYiZhiBang(self,'13590283182','123456')
        ActionMethod.Material(self)
        try:#进入添加图片页面
            startMethod.action_Id(self,case06['图片id'],'click')#点击选择图片
            startMethod.action_Id(self,case06['添加id'],'click')#点击添加图片
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case06['图片保存id']))
            self.logger.info('页面跳转到输入页面')
        except:
            self.logger.info('页面跳转到文字输入页面失败')
        try:
            startMethod.action_Id(self,case06['添加图片id'],'click')#点击添加图片id
            WebDriverWait(self,5).until(lambda driver:self.driver.find_element_by_id(flash['从相册选择id']))
            startMethod.action_Id(self,flash['从相册选择id'],'click')#点击从相册选择
            n = random.randint(1, 10)
            self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/iv_thumb')[n].click()  # 选择图片
            # startMethod.action_Id(self, 'com.henji.yunyi.yizhibang:id/menu_crop', 'click')  # 点击确认
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case06['图片保存id']))
            self.logger.info('上传图片成功')
        except:
            self.assertEqual(1,2,msg='上传图片失败')
        try:
            self.driver.find_element_by_id(case06['图片保存id']).click()
            startMethod.find_toast(self,titleMethod.duQu_Exlce(self,'case06',10,2))
        except:
            self.assertEqual(1,2,msg='获取toast失败')

        try:#点击返回
            startMethod.action_Id(self,flash['页面返回id'],'click')
            WebDriverWait(self,3).until(lambda driver:self.driver.find_element_by_id(case06['确定id']))
            self.driver.find_element_by_id(case06['确定id']).click()
        except:
            self.assertEqual(1,2,msg='返回失败')
    def test07(self):
        '''新增图片只添加标题和外链'''
        startMethod.loginYiZhiBang(self,'13590283182','123456')
        ActionMethod.Material(self)
        try:#进入添加图片页面
            startMethod.action_Id(self,case06['图片id'],'click')#点击选择图片
            startMethod.action_Id(self,case06['添加id'],'click')#点击添加图片
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case06['图片保存id']))
            self.logger.info('页面跳转到输入页面')
        except:
            self.logger.info('页面跳转到文字输入页面失败')
        try:
            timeCode = time.strftime('%d%H%M%S', time.localtime())  # 获取时间戳
            textCodeCase01 = titleMethod.duQu_Exlce(self, 'case06', 11, 2) + timeCode
            startMethod.action_Id(self,case06['图片标题输入框id'],textCodeCase01)#输入内容
            startMethod.action_Id(self,case06['图片外链id'],titleMethod.duQu_Exlce(self,'case06',13,2))
            self.driver.find_element_by_id(case06['图片保存id']).click()
            toastCode=titleMethod.duQu_Exlce(self,'case06',12,2)
            self.logger.info('获取toast为：{}'.format(toastCode))
            startMethod.find_toast(self,toastCode)
            self.logger.info('输入标题和链接，获取到toast')
        except:
            self.logger.error('未获取到toast')
        try:#点击返回
            startMethod.action_Id(self,flash['页面返回id'],'click')
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case06['确定id']))
            self.driver.find_element_by_id(case06['确定id']).click()
        except:
            self.assertEqual(1,2,msg='返回失败')
    def test08(self):
        '''上传图片/填写标题和外链'''
        startMethod.loginYiZhiBang(self,'13590283182','123456')
        ActionMethod.Material(self)
        try:#进入添加图片页面
            startMethod.action_Id(self,case06['图片id'],'click')#点击选择图片
            startMethod.action_Id(self,case06['添加id'],'click')#点击添加图片
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case06['图片保存id']))
            self.logger.info('页面跳转到输入页面')
        except:
            self.logger.info('页面跳转到输入页面失败')
        try:#上传图片
            startMethod.action_Id(self, case06['添加图片id'], 'click')  # 点击添加图片id
            WebDriverWait(self, 5).until(lambda driver: self.driver.find_element_by_id(flash['从相册选择id']))
            startMethod.action_Id(self, flash['从相册选择id'], 'click')  # 点击从相册选择
            n = random.randint(1, 10)
            self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/iv_thumb')[n].click()  # 选择图片
            # startMethod.action_Id(self, 'com.henji.yunyi.yizhibang:id/menu_crop', 'click')  # 点击确认
            # WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case06['图片保存id']))
            self.logger.info('上传图片成功')
        except:
            self.assertEqual(1, 2, msg='上传图片失败')
        try:#输入标题和外链
            timeCode = time.strftime('%d%H%M%S', time.localtime())  # 获取时间戳
            textCodeCase01 = titleMethod.duQu_Exlce(self, 'case06', 11, 2) + timeCode
            startMethod.action_Id(self,case06['图片标题输入框id'],textCodeCase01)#输入内容
            startMethod.action_Id(self,case06['图片外链id'],titleMethod.duQu_Exlce(self,'case06',13,2))#输入外网链接

            # startMethod.find_toast(self,titleMethod.duQu_Exlce(self,'case06',12,2))
            self.logger.info('输入标题和外链成功')
        except:
            self.assertEqual(1,2,msg='输入标题和外链失败')

        try:#点击保存
            self.driver.find_element_by_id(case06['图片保存id']).click()
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case06['添加id']))
            self.logger.info('保存成功')

        except:
            self.assertEqual(1,2,msg='保存失败')
        #验证添加后最新一条的标题
    def test09(self):
        '''验证新添加标题置顶显示'''
        startMethod.loginYiZhiBang(self,'13590283182','123456')
        ActionMethod.Material(self)
        try:#进入添加图片页面
            startMethod.action_Id(self,case06['图片id'],'click')#点击选择图片
            startMethod.action_Id(self,case06['添加id'],'click')#点击添加图片
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case06['图片保存id']))
            self.logger.info('页面跳转到输入页面')
        except:
            self.logger.info('页面跳转到文字输入页面失败')
        try:#上传图片
            startMethod.action_Id(self, case06['添加图片id'], 'click')  # 点击添加图片id
            WebDriverWait(self, 5).until(lambda driver: self.driver.find_element_by_id(flash['从相册选择id']))
            startMethod.action_Id(self, flash['从相册选择id'], 'click')  # 点击从相册选择
            n = random.randint(1, 10)
            self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/iv_thumb')[n].click()  # 选择图片
            # startMethod.action_Id(self, 'com.henji.yunyi.yizhibang:id/menu_crop', 'click')  # 点击确认
            # WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case06['图片保存id']))
            self.logger.info('上传图片成功')
        except:
            self.assertEqual(1, 2, msg='上传图片失败')
        try:#输入标题和外链
            timeCode = time.strftime('%d%H%M%S', time.localtime())  # 获取时间戳
            textCodeCase01 = titleMethod.duQu_Exlce(self, 'case06', 11, 2) + timeCode
            startMethod.action_Id(self,case06['图片标题输入框id'],textCodeCase01)#输入内容
            startMethod.action_Id(self,case06['图片外链id'],titleMethod.duQu_Exlce(self,'case06',13,2))#输入外网链接
            # startMethod.find_toast(self,titleMethod.duQu_Exlce(self,'case06',12,2))
            self.logger.info('输入标题和外链成功')
        except:
            self.assertEqual(1,2,msg='输入标题和外链失败')
        try:#点击保存
            self.driver.find_element_by_id(case06['图片保存id']).click()
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case06['添加id']))
            self.logger.info('保存成功')
        except:
            self.assertEqual(1,2,msg='保存失败')
        try:#验证第一个图片的标题是否为最新添加标题
            listText01=self.driver.find_elements_by_id(case06['图片list标题id'])[0].text
            self.logger.info('获取到图片列表第一个文章标题为：{}'.format(listText01))
            self.assertEqual(listText01,textCodeCase01,msg='图片列表获取到置顶的标题与最新输入的标题不符')
        except:
            self.logger.info('未获取到图片列表元素')
    def test10(self):
        '''验证图片删除功能'''
        startMethod.loginYiZhiBang(self,'13590283182','123456')
        ActionMethod.Material(self)
        startMethod.action_Id(self,case06['图片id'],'click')#点击选择图片
        try:
            action01=self.driver.find_elements_by_id(case06['已添加图片ids'])
            action=TouchAction(self.driver)
            action.press(action01[0]).wait(1000).release()
            action.perform()
            WebDriverWait(self,3).until(lambda driver:self.driver.find_elements_by_id(case06['确定id']))
            self.logger.info('长按第一个图片内容，弹出删除二次确定按钮')
            startMethod.action_Id(self,case06['确定id'],'click')
        except:
            self.assertEqual(1,2,msg='长按删除文章失败')
    def test11(self):
        '''验证只添加视频标题'''
        startMethod.loginYiZhiBang(self,'13590283182','123456')
        ActionMethod.Material(self)
        try:#进入添加图片页面
            startMethod.action_Id(self,case06['视频id'],'click')#点击选择图片
            startMethod.action_Id(self,case06['添加id'],'click')#点击添加图片
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case06['视频保存id']))
            self.logger.info('页面跳转到输入页面')
        except:
            self.logger.info('页面跳转到视频输入页面失败')
        try:
            timeText=time.strftime('%Y%m%d%H%M%S',time.localtime())
            excelText=titleMethod.duQu_Exlce(self,'case06',15,2)
            txt=excelText+':'+timeText
            startMethod.action_Id(self,case06['视频标题id'],txt)#输入内容
            self.logger.info('输入标题为：{}'.format(txt))
            startMethod.action_Id(self,case06['视频保存id'],'click')
            toastText=titleMethod.duQu_Exlce(self,'case06',16,2)#读取toast名称
            self.logger.info('读取预验证toast提示为：{}'.format(toastText))
            startMethod.find_toast(self,toastText)#验证toast
        except:
            self.assertEqual(1,2,msg='添加标题保存失败')
        try:
            startMethod.action_Id(self,flash['页面返回id'],'click')
            WebDriverWait(self,5).until(lambda driver:self.driver.find_elements_by_id(case06['确定id']))
            startMethod.action_Id(self,case06['确定id'],'click')
        except:
            self.assertEqual(1,2,msg='只输入标题退出失败')
    def test12(self):
        '''输入标题加外链'''
        startMethod.loginYiZhiBang(self,'13590283182','123456')
        ActionMethod.Material(self)
        try:#进入添加图片页面
            startMethod.action_Id(self,case06['视频id'],'click')#点击选择图片
            startMethod.action_Id(self,case06['添加id'],'click')#点击添加图片
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case06['视频保存id']))
            self.logger.info('页面跳转到输入页面')
        except:
            self.logger.info('页面跳转到视频输入页面失败')
        try:#输入标题叫外链
            timeText = time.strftime('%Y%m%d%H%M%S', time.localtime())
            excelText = titleMethod.duQu_Exlce(self, 'case06', 15, 2)
            txt = excelText + ':' + timeText
            startMethod.action_Id(self, case06['视频标题id'], txt)  # 输入内容
            startMethod.action_Id(self,case06['视频外链id'],titleMethod.duQu_Exlce(self,'case06',14,2))#输入视频外链
            startMethod.action_Id(self, case06['视频保存id'], 'click')#点击视频保存
            toastText=titleMethod.duQu_Exlce(self,'case06',17,2)
            startMethod.find_toast(self,toastText)
        except:
            self.assertEqual(1,2,msg='输入标题和外链，点击保存，操作失败')
        try:
            startMethod.action_Id(self,flash['页面返回id'],'click')
            WebDriverWait(self,5).until(lambda driver:self.driver.find_elements_by_id(case06['确定id']))
            startMethod.action_Id(self,case06['确定id'],'click')
        except:
            self.assertEqual(1,2,msg='只输入标题退出失败')
    def test13(self):
        '''输入视频标题，外链，图片保存'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        ActionMethod.Material(self)
        try:  # 进入添加图片页面
            startMethod.action_Id(self, case06['视频id'], 'click')  # 点击选择图片
            startMethod.action_Id(self, case06['添加id'], 'click')  # 点击添加图片
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case06['视频保存id']))
            self.logger.info('页面跳转到输入页面')
        except:
            self.logger.info('页面跳转到视频输入页面失败')
        try:  # 输入标题叫外链
            timeText = time.strftime('%Y%m%d%H%M%S', time.localtime())
            excelText = titleMethod.duQu_Exlce(self, 'case06', 15, 2)
            txt = excelText + ':' + timeText
            startMethod.action_Id(self, case06['视频标题id'], txt)  # 输入内容
            startMethod.action_Id(self, case06['视频外链id'], titleMethod.duQu_Exlce(self, 'case06', 14, 2))  # 输入视频外链
        except:
            self.assertEqual(1, 2, msg='输入标题和外链，失败')
        try:#添加图片
            startMethod.action_Id(self, case06['视频图片id'], 'click')  # 点击添加图片id
            WebDriverWait(self, 5).until(lambda driver: self.driver.find_element_by_id(flash['从相册选择id']))
            startMethod.action_Id(self, flash['从相册选择id'], 'click')  # 点击从相册选择
            n = random.randint(1, 10)
            self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/iv_thumb')[n].click()  # 选择图片
            # startMethod.action_Id(self, 'com.henji.yunyi.yizhibang:id/menu_crop', 'click')  # 点击确认
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(flash['从相册选择确定id']))
            self.driver.find_element_by_id(flash['从相册选择确定id']).click()
            self.logger.info('上传图片成功')
        except:
            self.assertEqual(1, 2, msg='上传图片失败')
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_elements_by_id(case06['视频保存id']))
            startMethod.action_Id(self, case06['视频保存id'], 'click')  # 点击视频保存
            WebDriverWait(self,20).until(lambda driver: self.driver.find_elements_by_id(case06['添加id']))
            self.logger.info('保存成功')
        except:
            self.assertEqual(1, 2, msg='输入视频标题、外链、图片之后，保存失败')
    def test14(self):
        '''验证视频删除'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        ActionMethod.Material(self)
        try:  #添加视频列表
            startMethod.action_Id(self, case06['视频id'], 'click')  # 点击选择视频
            startMethod.action_Id(self, case06['添加id'], 'click')  # 点击添加视频
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case06['视频保存id']))
            self.logger.info('页面跳转到输入页面')
        except:
            self.logger.info('页面跳转到视频输入页面失败')
        try:  # 输入标题叫外链
            timeText = time.strftime('%Y%m%d%H%M%S', time.localtime())
            excelText = titleMethod.duQu_Exlce(self, 'case06', 15, 2)
            txt = excelText + ':' + timeText
            startMethod.action_Id(self, case06['视频标题id'], txt)  # 输入内容
            startMethod.action_Id(self, case06['视频外链id'], titleMethod.duQu_Exlce(self, 'case06', 14, 2))  # 输入视频外链
        except:
            self.assertEqual(1, 2, msg='输入标题和外链，失败')
        try:#添加图片
            startMethod.action_Id(self, case06['视频图片id'], 'click')  # 点击添加图片id
            WebDriverWait(self, 5).until(lambda driver: self.driver.find_element_by_id(flash['从相册选择id']))
            startMethod.action_Id(self, flash['从相册选择id'], 'click')  # 点击从相册选择
            n = random.randint(1, 10)
            self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/iv_thumb')[n].click()  # 选择图片
            # startMethod.action_Id(self, 'com.henji.yunyi.yizhibang:id/menu_crop', 'click')  # 点击确认
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(flash['从相册选择确定id']))
            self.driver.find_element_by_id(flash['从相册选择确定id']).click()
            self.logger.info('上传图片成功')
        except:
            self.assertEqual(1, 2, msg='上传图片失败')
        try:
            WebDriverWait(self,10).until(lambda driver:self.driver.find_elements_by_id(case06['视频保存id']))
            startMethod.action_Id(self, case06['视频保存id'], 'click')  # 点击视频保存
            WebDriverWait(self,20).until(lambda driver: self.driver.find_elements_by_id(case06['添加id']))
            self.logger.info('保存成功')
        except:
            self.assertEqual(1, 2, msg='输入视频标题、外链、图片之后，保存失败')
        try:
            videoList=self.driver.find_elements_by_id(case06['视频列表id'])
            videoText=videoList[0].text#获取第一个视频列表的title
            self.logger.info('获取删除第一个视频的title为：{}'.format(videoText))
            action=TouchAction(self.driver)
            action.press(videoList[0]).wait(1000).release()
            action.perform()#长按第一个视频
            WebDriverWait(self,3).until(lambda driver:self.driver.find_elements_by_id(case06['确定id']))
            startMethod.action_Id(self,case06['确定id'],'click')
            videoListNew=self.driver.find_elements_by_id(case06['视频列表id'])
            videoTextNew=videoListNew[0].text#获取删除视频列表之后的第一个视频列表title
            self.logger.info('获取删除之后第一个视频的title为：{}'.format(videoTextNew))
            self.assertNotEqual(videoText,videoTextNew,msg='删除元素之后，列表数量仍然相等，删除失败')
        except:
            self.assertEqual(1,2,msg='删除视频列表失败')
    def test15(self):
        '''验证文字删除'''
        startMethod.loginYiZhiBang(self,'13590283182','123456')#登录
        ActionMethod.Material(self)#进入素材页面
        try:#添加一个文章
            startMethod.action_Id(self,case06['文字id'],'click')#点击选择文字
            startMethod.action_Id(self,case06['添加id'],'click')#点击添加文字
            WebDriverWait(self,10).until(lambda driver:self.driver.find_element_by_id(case06['文字保存id']))
            self.logger.info('页面跳转到输入页面')
        except:
            self.logger.info('页面跳转到文字输入页面失败')
        try:
            timeText=time.strftime('%Y%m%d%H%M%S',time.localtime())#获取当前时间戳
            text=titleMethod.duQu_Exlce(self, 'case06', 6, 2)+timeText#输入内容为文字加时间戳
            startMethod.action_Id(self, case06['文字输入框id'], text)#输入内容
            startMethod.action_Id(self, case06['外链id'], titleMethod.duQu_Exlce(self, 'case06', 8, 2))#输入外链
            startMethod.action_Id(self, case06['文字保存id'], 'click')  # 点击保存

            WebDriverWait(self, 3).until(lambda driver: self.driver.find_element_by_id(case06['添加id']))
            self.logger.info('添加完毕')
            textList=self.driver.find_elements_by_id(case06['文字列表id'])
            text=textList[0].text
            self.assertNotEqual(text,titleMethod.duQu_Exlce(self,'case06',6,2))
        except:
            self.assertEqual(1,2,msg='添加失败')
        try:#删除文字内容
            textList=self.driver.find_elements_by_id(case06['文字列表id'])
            firstText=textList[0].text#获取删除之前的titile
            self.logger.info('删除之前的文字title：{}'.format(firstText))
            action=TouchAction(self.driver)
            action.press(textList[0]).wait(1000).release()
            action.perform()#选择第一个文字列表内容删除
            WebDriverWait(self,3).until(lambda driver:self.driver.find_element_by_id(case06['确定id']))
            startMethod.action_Id(self,case06['确定id'],'click')
            textListNew=self.driver.find_elements_by_id(case06['文字列表id'])
            firstTextNew=textListNew[0].text#获取删除之后的title
            self.logger.info('删除之后的文字title：{}'.format(firstTextNew))
            self.assertNotEqual(firstText,firstTextNew,msg='元素未正常删除')
        except:
            self.assertEqual(1,2,msg='删除文字失败')
    def test16(self):
        '''验证删除名片'''
        startMethod.loginYiZhiBang(self, '13590283182', '123456')
        ActionMethod.Material(self)
        try:
            startMethod.action_Id(self, case06['添加id'], 'click')
            self.logger.info('点击添加微名片')
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(case06['名片保存id']))
            self.logger.info('页面跳转成功')
        except:
            self.assertEqual(1, 2, msg='页面跳转失败')
        try:  # 上传图片
            startMethod.action_Id(self, case06['头像id'], 'click')
            startMethod.action_Id(self, flash['从相册选择id'], 'click')  # 点击从相册选择
            n = random.randint(1, 10)
            self.driver.find_elements_by_id('com.henji.yunyi.yizhibang:id/iv_thumb')[2].click()  # 选择图片
            startMethod.action_Id(self, 'com.henji.yunyi.yizhibang:id/menu_crop', 'click')  # 点击确认
            WebDriverWait(self, 10).until(lambda driver: self.driver.find_elements_by_id(case06['名片保存id']))
            self.logger.info('上传图片成功')
        except:
            self.assertEqual(1, 2, msg='上传图片失败')
        try:  # 更改姓名
            self.driver.find_element_by_xpath(case06['姓名xpath']).click()  # 点击姓名
            timeCode = time.strftime('%d%H%M%S', time.localtime())
            textCode = titleMethod.duQu_Exlce(self, 'case06', 1, 2) + timeCode
            self.logger.info('预输入字符串为：{}'.format(textCode))
            WebDriverWait(self, 3).until(lambda driver: self.driver.find_element_by_id(case06['名片输入框id']))
            self.driver.find_element_by_id(case06['名片输入框id']).set_text(textCode)  # 输入姓名
            startMethod.action_Id(self, case06['名片输入框确定id'], 'click')  # 点击确定
            self.logger.info('更改姓名成功,最新姓名为：{}'.format(textCode))
        except:
            self.assertEqual(1, 2, msg='更改姓名失败')
        try:  # 更改手机号
            self.driver.find_element_by_xpath(case06['手机xpath']).click()  # 点击手机号
            timeCode = time.strftime('%d%H%M%S', time.localtime())  # 获取时间戳
            telCode = titleMethod.duQu_Exlce(self, 'case06', 2, 2) + timeCode  # 预输入号码135+八位时间戳
            self.driver.find_element_by_id(case06['名片输入框id']).set_text(telCode)  # 输入手机号码
            startMethod.action_Id(self, case06['名片输入框确定id'], 'click')  # 点击确定
            self.logger.info('更改姓名成功,最新手机号码为：{}'.format(telCode))
        except:
            self.assertEqual(1, 2, msg='更换手机号失败')
        try:  # 输入个性签名
            self.driver.find_element_by_xpath(case06['签名xpath']).click()  # 点击签名
            timeCode = time.strftime('%d%H%M%S', time.localtime())  # 获取时间戳
            txtCode = titleMethod.duQu_Exlce(self, 'case06', 3, 2) + timeCode
            self.driver.find_element_by_id(case06['名片输入框id']).set_text(txtCode)  # 输入内容
            startMethod.action_Id(self, case06['名片输入框确定id'], 'click')  # 点击确定
        except:
            self.assertEqual(1, 2, msg='输入个性签名失败')
        try:  # 更换地址
            startMethod.action_Id(self, case06['地址id'], 'click')
            timeCode = time.strftime('%d%H%M%S', time.localtime())  # 获取时间戳
            txtCode1 = titleMethod.duQu_Exlce(self, 'case06', 4, 2) + timeCode
            startMethod.action_Id(self, case06['名片输入框id'], txtCode1)  # 输入内容
            startMethod.action_Id(self, case06['名片输入框确定id'], 'click')  # 点击确定
        except:
            self.assertEqual(1, 2, msg='更换地址失败')
        try:  # 更换公司名称
            self.driver.find_element_by_xpath(case06['公司xpath']).click()
            timeCode = time.strftime('%d%H%M%S', time.localtime())  # 获取时间戳
            txtCode2 = titleMethod.duQu_Exlce(self, 'case06', 5, 2) + timeCode
            startMethod.action_Id(self, case06['名片输入框id'], txtCode2)  # 输入内容
            startMethod.action_Id(self, case06['名片输入框确定id'], 'click')  # 点击确定
            startMethod.action_Id(self, case06['名片保存id'], 'click')
        except:
            self.assertEqual(1, 2, msg='更换公司名称失败')
        try:
            textList=self.driver.find_elements_by_id(case06['名片列表id'])
            firstText=textList[0].text#获取删除之前的title
            self.logger.info('获取删除之前的名片title：{}'.format(firstText))
            action=TouchAction(self.driver)
            action.press(textList[0]).wait(1000).release()
            action.perform()#长按控件
            WebDriverWait(self,10).until(lambda driver:self.driver.find_elements_by_id(case06['确定id']))
            startMethod.action_Id(self,case06['确定id'],'click')#点击确定
            textListNew = self.driver.find_elements_by_id(case06['名片列表id'])
            firstTextNew = textListNew[0].text#获取删除之后名片title
            self.logger.info('获取删除之后的名片title：{}'.format(firstTextNew))
            self.assertNotEqual(firstText,firstTextNew,msg='删除前后元素一直，未删除成功')
        except:
            self.assertEqual(1,2,msg='删除名片失败')





















































