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
        ''''''