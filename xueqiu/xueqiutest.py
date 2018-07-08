#coding:utf-8

import unittest
from appium import webdriver
from time import sleep

class xueqiu(unittest.TestCase):
    def test(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Android Emulator'
        # desired_caps['app'] = PATH('D:/xueqiu_000_05301650.apk')
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['dontStopAppOnReset'] = True
        desired_caps['NoReset'] =  True

        # 输入法
        desired_caps['unicodeKeyboard'] = 'true'  # 支持中文输入，而且不会乱跳
        desired_caps['resetKeyboard'] = 'true'  # 运行结束以后，删除appium键盘
        desired_caps['noReset'] = 'true'  # 不做应用清除

        # desired_caps['udid'] =   'FA6B4BN00753'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)


        self.driver.find_element_by_xpath('//*[@text="好的"]').click()

        sleep(3)
        self.driver.find_element_by_xpath('//*[@text="交易"]').click()

        sleep(5)
        print(self.driver.contexts)
        print(self.driver.current_context)
        sleep(10)


if __name__ =="__main__":
    Test = xueqiu()
    Test.test()