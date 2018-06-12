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
        desired_caps['appPackage'] = 'com.banggood.client'
        desired_caps['appActivity'] = '.module.home.MainActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("iv_ad_close").click()
        time.sleep(2)
        self.driver.find_element_by_id("iv_close").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[contains(@text,'New User Zone')]").click()
        time.sleep(2)
        print(self.driver.context)
        self.driver.quit()

if __name__ == '__main__':
    testwebview = testbanggood()
    testwebview.testWebview()





