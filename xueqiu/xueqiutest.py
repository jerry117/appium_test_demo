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
        # desired_caps['noReset'] =  True

        # 输入法
        desired_caps['unicodeKeyboard'] = 'true'  # 支持中文输入，而且不会乱跳
        desired_caps['resetKeyboard'] = 'true'  # 运行结束以后，删除appium键盘
        desired_caps['noReset'] = 'true'  # 不做应用清除

        # desired_caps['udid'] =   'FA6B4BN00753'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

        #建议用着四种做定位
        # self.driver.find_element_by_id()
        # self.driver.find_element_by_xpath()
        # self.driver.find_element_by_accessibility_id()   #content-desc 盲人辅助，可以让开发加
        # self.driver.find_element_by_android_uiautomator()

        #1、APP里的webview控件，必须打开debug模式
        #2、手机必须是4.4或以上，（Chromedriver）
        #3、切换到Chromedriver模式以后，【移动端定制】的操作不可用
        print(self.driver.contexts)
        webview = self.driver.contexts[1]
        self.driver.switch_to.content(webview)
        self.driver.find_element_by_xpath('//')

        #假设APP跳转到了Android view，切记切换回 native_app
        native = self.driver.contexts[0]
        self.driver.switch_to.content(native)


        #文本定位
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