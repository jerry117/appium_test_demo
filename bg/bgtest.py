# coding:utf-8


from appium import webdriver
import time
import unittest
import os

class testbanggood(unittest.TestCase):

    def testWebview(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['deviceName']='Custom Phone'
        desired_caps['appPackage'] = 'com.xxx.client'
        desired_caps['appActivity'] = '.module.home.MainActivity'

        # 输入法
        desired_caps['unicodeKeyboard'] = 'true'  # 支持中文输入，而且不会乱跳
        desired_caps['resetKeyboard'] = 'true'  # 运行结束以后，删除appium键盘
        desired_caps['noReset'] = 'true'  # 不做应用清除

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("iv_ad_close").click()
        time.sleep(2)
        self.driver.find_element_by_id("iv_close").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[contains(@text,'New User Zone')]").click()
        time.sleep(2)
        print(self.driver.contexts)
        print(self.driver.current_context)

        self.driver.switch_to.context('WEBVIEW_com.xxx.client')
        print(self.driver.contexts)
        print(self.driver.current_context)
        time.sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    testwebview = testbanggood()
    testwebview.testWebview()





