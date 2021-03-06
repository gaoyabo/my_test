# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def browser(browser='firefox'):
    '''
    打开浏览器函数，‘firefox’、‘Chrome’、‘IE’、‘phantomjs’
    '''
    try:
        if browser == 'firefox':
            driver = webdriver.Firefox()
            return driver
        elif browser == 'chrome':
            driver = webdriver.Chrome()
            return driver
        elif browser == 'ie':
            driver = webdriver.Ie()
            return driver
        elif browser == 'phantomjs':
            driver = webdriver.PhantomJS()
            return driver
        else:
            print "NOt found this browser,You can enter'firefox','chrome','ie' or 'phantomjs'"
    except Exception as msg:
        print "%s" % msg


class Yoyo(object):
    '''
    底层封装
    '''

    def __init__(self):
        '''
        定义基础条件
        '''
        # self.driver = webdriver.PhantomJS()
        self.driver = webdriver.Firefox()
        # self.driver = browser()

    def open(self, url, t='', timeout=10):
        '''使用get打开url后，最大化窗口，判断title符合预期
        usage:
        driver = Yoyo()
        driver.open(url, t='')
        '''
        self.driver.get(url)
        self.driver.maximize_window()
        try:
            WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(t))
        except TimeoutException:
            print "open %s title error" % url
        except Exception as msg:
            print "error:%s" % msg

    def get(self, url):
        '''使用get打开url'''
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        '''定位元素,参数locator是元组类型
        usage:
        locator = ("id", "xxx")
        driver.find_element(locator)
        '''
        element = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator, timeout=10):
        '''定位一组元素,参数locator是元组类型
        '''
        elements = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_all_elements_located(locator))
        return elements

    def click(self, locator):
        '''点击操作
        usage:
        locator = ("id", "xxx")
        driver.click(locator)
        '''
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        '''发送文本，清空后输入
        usage:
        loctor = ("id", "xxx")
        driver.send_keys(locator, text)
        '''
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def is_text_in_element(self, locator, text, timeout=10):
        '''
        判断文本在元素里，没定位到元素返回false，定位到返回判断结果布尔值
        result = driver.text_in_element(locator, text)
        '''
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.text_to_be_present_in_element(lacator, text))
        except TimeoutException:
            print "元素没定位到：" + str(locator)
        else:
            return result

    def is_text_in_value(self, locator, value, timeout=10):
        '''
        判断元素的value值，没定位到元素返回false，定位到返回判断结果布尔值
        result = driver.text_in_element(locator, text)
        '''
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.text_to_be_present_in_element_value(locator, value))
        except TimeoutException:
            print u"元素没定位到:" + str(locator)
            return False
        else:
            return result

    def is_title(self, title, timeout=10):
        '''
        判断title完全等于
        '''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_is(title))
        return result

    def is_title_contains(self, title, timeout=10):
        '''
        判断title包含
        '''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(title))
        return result

    def is_selected(self, locator, timeout=10):
        '''
        判断元素被选中，返回布尔值
        '''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_to_be_selected(locator))
        return result

    def is_selected_be(self, locator, selected=True, timeout=10):
        '''
        判断元素的状态，selected是期望的参数true/false
        返回布尔值
        '''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_located_selection_state_to_be(locator, selected))
        return result

    def is_alert_present(self, timeout=10):
        '''判断页面是否有alert
        有返回alert（注意这里是返回alert，不是true）
        没有返回false'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.alert_is_present())
        return result

    def is_visibility(self, locator, timeout=10):
        '''
        元素可见返回本身，不可见返回false
        '''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.visibility_of_element_located(locator))
        return result

    def is_clickable(self, locator, timeout=10):
        '''
        元素可以点击is_enabled返回本身，不可点击返回fasle
        '''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_to_be_clickable(locator))
        return result

    def is_located(self, locator, timeout=10):
        '''
        判读元素有没被定位到（并不意味着可见），定位到返回element,没有定位到返回fasle
        '''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(locator))
        return result

    def move_to_element(self, locator):
        '''
        鼠标悬停操作
        usage:
        locator = ('id','xxx')
        driver.move_to_element(locator)
        '''
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def back(self):
        '''
        back to old window.
        usage:
        driver.back()
        '''
        self.driver.back()

    def forward(self):
        '''
        Forward to old window.返回上一个窗口
        usage:
        driver.forward()
        '''
        self.driver.forward()

    def close(self):
        '''
        Close the window.关闭浏览器窗口
        usage:
        driver.close()
        '''
        self.driver.close()

    def quit(self):
        '''
        Quit the driver and close all the windows.退出浏览器并关闭窗口
        usage:
        driver.quit()
        '''
        self.driver.quit()

    def get_title(self):
        '''获取title'''
        return self.driver.title

    def get_text(self, locator):
        '''获取文本'''
        element = self.find_element(locator)
        return element.text

    def get_attribute(self, locator, name):
        '''获取属性'''
        element = self.find_element(locator)
        return element.get_attribute(name)

    def js_execute(self, js):
        '''执行js'''
        return self.driver.execute_script(js)

    def js_focus_element(self, locator):
        '''聚焦元素'''
        target = self.find_element(locator)
        self.driver.execute_script("argument[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        '''滚到底部'''
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def select_by_index(self, locator, index):
        '''通过索引，index是索引第几个，从0开始'''
        element = self.find_element(locator)
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        '''通过value属性'''
        element = self.find_element(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        '''通过文本值定位'''
        element = self.find_element(locator)
        Select(element).select_by_value(text)
        

if __name__ == "__main__":
    driver = browser()
    driver_n = Yoyo()
    driver_n.open("https://www.baidu.com")
    cd = ("id", "kw")
    driver_n.send_keys(cd, "selenium")
    cs = ("id", "su")
    driver_n.click(cs)
    time.sleep(5)
    driver_n.send_keys(("id", "kw"), "python")
    driver_n.click(("id", "su"))
