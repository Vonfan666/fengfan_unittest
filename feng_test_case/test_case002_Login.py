# coding:utf-8

from fengfan_unittest.startAPP import *
from fengfan_unittest.feng_test_method.method import *
import  unittest,requests,HTMLTestRunner
from fengfan_unittest.feng_test_conf.feng_test_env.feng_test_config import *
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

PATH = lambda  p:os.path.abspath(
       os.path.join(os.path.dirname(__file__),p)
)
print(os.getcwd())
class Test_login(unittest.TestCase,object):
    def  setUp(self):
        start_App.__init__(self)
        start_App.setUp(self)
        time.sleep(3)
    def tearDown(self):
        start_App.tearDown(self)
    def test01(self):
        '''验证账号为空，输入密码不可登陆'''
        self.logger.info('*************************************************************')
        try:
            startMethod.action_Id(self,login['账号id'],'obtain').clear()
            startMethod.action_Id(self,login['密码id'],titleMethod.duQu_Exlce(self,'登录',1,3))#exlce读取密码
            self.logger.info('输入密码为%s'%titleMethod.duQu_Exlce(self,'登录',1,3))
            startMethod.action_Id(self,login['登录id'],'click')#点击登陆
            #等待两秒之后获取登陆空间元素，验证登陆是否成功
            try:
                WebDriverWait(self,2).until(lambda driver:self.driver.find_element_by_id(login['登录id']))
                self.assertEqual(1,1,msg='账号为空，输入密码，不可登录，符合预期')
            except:
                self.assertEqual(1,2,msg='账号为空，输入密码，可以登陆，不符合预期')
        except:
            startMethod.action_Id(self,login['账号id'],'obtain').clear()
            startMethod.action_Id(self,login['密码id'],titleMethod.duQu_Exlce(self,'登录',1,3))#exlce读取密码
            self.logger.info('输入密码为%s'%titleMethod.duQu_Exlce(self,'登录',1,3))
            startMethod.action_Id(self,login['登录id'],'click')#点击登陆
            #等待两秒之后获取登陆空间元素，验证登陆是否成功
            try:
                WebDriverWait(self,2).until(lambda driver:self.driver.find_element_by_id(login['登录id']))
                self.assertEqual(1,1,msg='账号为空，输入密码，不可登录，符合预期')
            except:
                self.assertEqual(1,2,msg='账号为空，输入密码，可以登陆，不符合预期')
    def test02(self):
        '''验证账号输入正确，密码为空'''
        self.logger.info('*************************************************************')
        startMethod.action_Id(self, login['账号id'], 'obtain').clear()#清除账号输入框
        startMethod.action_Id(self, login['密码id'], 'obtain').clear()#清除密码输入框
        startMethod.action_Id(self,login['账号id'],titleMethod.duQu_Exlce(self,'登录',2,2))#输入账号
        startMethod.action_Id(self,login['登录id'],'click')#点击登录
        try:
            WebDriverWait(self,2).until(lambda driver:self.driver.find_element_by_id(login['登录id']))
            self.assertEqual(1,1,msg='账号为空，输入密码，不可登录，符合预期')
        except:
            self.assertEqual(1,2,msg='账号为空，输入密码，可以登陆，不符合预期')
    def test03(self):
        '''验证输入小于11账号,不输入密码'''
        self.logger.info('*************************************************************')
        startMethod.action_Id(self, login['账号id'], 'obtain').clear()#清除账号输入框
        startMethod.action_Id(self, login['密码id'], 'obtain').clear()#清除密码输入框
        startMethod.action_Id(self,login['账号id'],titleMethod.duQu_Exlce(self,'登录',3,2))
        startMethod.action_Id(self, login['登录id'], 'click')  # 点击登录
        try:
            WebDriverWait(self,2).until(lambda driver:self.driver.find_element_by_id(login['登录id']))
            self.assertEqual(1,1,msg='账号为空，输入密码，不可登录，符合预期')
        except:
            self.assertEqual(1,2,msg='账号为空，输入密码，可以登陆，不符合预期')
    def test04(self):
        '''验证输入小于11账号，输入非正确密码'''
        self.logger.info('*************************************************************')
        startMethod.action_Id(self, login['账号id'], 'obtain').clear()#清除账号输入框
        startMethod.action_Id(self, login['密码id'], 'obtain').clear()#清除密码输入框
        startMethod.action_Id(self,login['账号id'],titleMethod.duQu_Exlce(self,'登录',4,2))#输入账号
        startMethod.action_Id(self,login['密码id'],titleMethod.duQu_Exlce(self,'登录',4,3))#输入密码
        startMethod.action_Id(self,login['登录id'],'click')#点击登录
        try:
            WebDriverWait(self,2).until(lambda driver:self.driver.find_element_by_id(login['登录id']))
            self.assertEqual(1,1,msg='输入小于11位手机号，输入错误密码，不可登录，符合预期')
        except:
            self.assertEqual(1,2,msg='输入小于11位手机号，输入错误密码，可以登陆，不符合预期')
    def test05(self):
        '''输入正确号码但多输入一位，输入错误密码'''
        self.logger.info('*************************************************************')
        startMethod.action_Id(self, login['账号id'], 'obtain').clear()#清除账号输入框
        startMethod.action_Id(self, login['密码id'], 'obtain').clear()#清除密码输入框
        startMethod.action_Id(self,login['账号id'],titleMethod.duQu_Exlce(self,'登录',5,2))#输入账号位135902831821
        startMethod.action_Id(self,login['密码id'],titleMethod.duQu_Exlce(self,'登录',5,3))#输入错误密码
        time.sleep(5)
        text1= self.driver.find_element_by_id(login['账号id']).text#获取输入大于11位账号的test
        # 将获取到的text和exlce中截取的前11位进行断言
        self.assertIn(text1,titleMethod.duQu_Exlce(self,'登录',5,2)[0:11],msg='未截取输入的前11位字符')
        self.logger.info('%s等于%s，输入超过11位手机号码，只截取显示前11位'%(text1,titleMethod.duQu_Exlce(self,'登录',5,2)[0:11]))
        startMethod.action_Id(self, login['登录id'], 'click')  # 点击登录
        try:
            WebDriverWait(self,2).until(lambda driver:self.driver.find_element_by_id(login['登录id']))
            self.assertEqual(1,1,msg='输入正确号码但多输入一位，输入错误密码，不可登录，符合预期')
        except:
            self.assertEqual(1,2,msg='输入正确号码但多输入一位，输入错误密码，可以登陆，不符合预期')
    def test06(self):
        '''输入正确号码但多输入一位,输入正确密码'''
        self.logger.info('*************************************************************')
        startMethod.action_Id(self, login['账号id'], 'obtain').clear()#清除账号输入框
        startMethod.action_Id(self, login['密码id'], 'obtain').clear()#清除密码输入框
        startMethod.action_Id(self, login['账号id'], titleMethod.duQu_Exlce(self,'登录',6,2))  # 输入账号位13590283182
        time.sleep(3)
        startMethod.action_Id(self, login['密码id'], titleMethod.duQu_Exlce(self,'登录',6,3))  # 输入正确密码
        time.sleep(3)
        text1 = self.driver.find_element_by_id(login['账号id']).text  # 获取输入大于11位账号的test
        # 将获取到的text和exlce中截取的前11位进行断言
        self.assertIn(text1,titleMethod.duQu_Exlce(self,'登录',6,2)[0:11], msg='未截取输入的前11位字符')
        self.logger.info('%s等于%s，输入超过11位手机号码，只截取显示前11位' % (text1, titleMethod.duQu_Exlce(self,'登录',6,2)[0:11]))
        startMethod.action_Id(self, login['登录id'], 'click')  # 点击登录
        time.sleep(5)
        try:
            self.driver.find_element_by_id(login['登录id'])
            self.assertEqual(1,2, msg='输入正确号码但多输入一位，输入错误密码，不可登录，不符合预期')
            startMethod.backLogin(self, 350, 1030)
        except:
            self.logger.info('输入正确号码但多输入一位,输入正确密码，成功截取账号前11位，登录成功')
            self.assertEqual(1,1,msg='输入正确号码但多输入一位,输入正确密码，可以登陆，符合预期')
        startMethod.backCode(self)
    def test07(self):
        '''输入非数字账号'''
        self.logger.info('*************************************************************')
        startMethod.action_Id(self, login['账号id'], 'obtain').clear()  # 清除账号输入框
        startMethod.action_Id(self, login['密码id'], 'obtain').clear()  # 清除密码输入框
        startMethod.action_Id(self,login['账号id'],titleMethod.duQu_Exlce(self,'登录',7,2))#输入非法手机号码
        startMethod.action_Id(self,login['密码id'],titleMethod.duQu_Exlce(self,'登录',7,3))#任意输入密码
        startMethod.action_Id(self, login['登录id'], 'click')  # 点击登录
        try:
            WebDriverWait(self, 2).until(lambda driver: self.driver.find_element_by_id(login['登录id']))
            self.assertEqual(1, 1, msg='输入非数字账号，输入错误密码，不可登录，符合预期')
        except:
            self.assertEqual(1, 2, msg='输入非数字账号，输入错误密码，可以登陆，不符合预期')
    def test08(self):
        '''输入正确手机号码，正确密码'''
        self.logger.info('*************************************************************')
        startMethod.action_Id(self, login['账号id'], 'obtain').clear()  # 清除账号输入框
        startMethod.action_Id(self, login['密码id'], 'obtain').clear()  # 清除密码输入框
        startMethod.action_Id(self,login['账号id'],titleMethod.duQu_Exlce(self,'登录',8,2))#输入正确手机号码
        startMethod.action_Id(self,login['密码id'],titleMethod.duQu_Exlce(self,'登录',8,3))#输入正确手机号码
        startMethod.action_Id(self,login['登录id'],'click')#点击登录
        time.sleep(3)
        try:
            WebDriverWait(self, 2).until(lambda driver: self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/rl_home_home'))
            self.assertEqual(1, 1, msg='输入正确手机号码，正确密码，可以登陆，符合预期')

        except:
            self.assertEqual(1, 2, msg='输入正确手机号码，正确密码，不可登录，不符合预期')
        startMethod.backCode(self)
if __name__=='__main__':
    unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(Test_login('test01'))
    suite.addTest(Test_login('test02'))
    suite.addTest(Test_login('test03'))
    suite.addTest(Test_login('test04'))
    suite.addTest(Test_login('test05'))
    suite.addTest(Test_login('test06'))
    suite.addTest(Test_login('test07'))
    suite.addTest(Test_login('test08'))
    pathCode = 'C:\\Users\\feng\Desktop\python01\\fengfan_unittest\\feng_test_result\\'
    curtime=time.strftime('%Y%m%d%H%M%S',time.localtime())
    report_path = pathCode+curtime+'.html'
    report_set = open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=report_set,title=u'自动化测试报告',description=u'用例执行情况：')
    runner.run(suite)
    report_set.close()



