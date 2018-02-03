# -*- coding: utf-8 -*-
import Yoyo
import unittest
from selenium import webdriver


# @unittest.skip(u"无条件跳过整个测试类")
class Ale(unittest.TestCase):

    @classmethod
    def setUpClass(sls):
        '''setUp是每次登录每次打开，
        setUpClass是打开一次，执行以下所有用例
        '''
        sls.driver = Yoyo.Yoyo()
        # self.ale.open("http://admin.aleqipei.com/site/login")

    @classmethod
    def tearDownClass(sls):
        '''tearDown是每次执行完成后执行
        tearDownClass是运行完所有用例后执行'''
        sls.driver.quit()

    def login(self, username='gaoyabo', password='gaoyabo'):
        # try:
            # ale = Yoyo.Yoyo()
        self.driver.open("http://admin.aleqipei.com/site/login")
        self.driver.send_keys(('id', 'loginform-username'), username)
        self.driver.send_keys(('id', 'loginform-password'), password)
        self.driver.click(('id', 'loginform-rememberme'))
        self.driver.click(('name', 'login-button'))
        self.driver.is_title(u'客户列表')
        # except Exception as msg:
        #     print u'异常原因:%s' % msg
            # nowTime = time.strftime("%Y%m%d.%H%M.%S")
            # self.ale.driver.get_screenshot_as_file('.\\jpg\\%s.jpg' % nowTime)
            # 如果加try...except捕获异常后结果，此时所有的测试用例都通过了，会影响测试结果。解决办法就是再次抛出异常
            # raise

    @unittest.skip("is ture")   # 无条件跳过
    def test_login_1(self):
        '''无密码，登录'''
        self.login('gaoyabo', '')

    @unittest.skipUnless(False, "is ture")  # 错误跳过
    def test_login_2(self):
        '''无用户，登录'''
        self.login('', 'gaoyabo')

    @unittest.skipIf(True, "is ture")   # 正确跳过
    def test_login_3(self):
        '''无用户、无密码登录'''
        self.login('', '')

    def test_login_4(self):
        '''默认登录'''
        self.login()

    # @unittest.expectedFailure   #断言的时候跳过
    def test_login_5(self):
        '''默认登录'''
        self.login('sunmingzhe', 'smz3865')


if __name__ == "__main__":
    unittest.main()
