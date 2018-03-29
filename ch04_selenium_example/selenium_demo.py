#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import os
import sys
import time
from importlib import reload

import urllib.request

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options


class SeleniumTest(object):
    def __init__(self):
        pass

    def start(self, urls):
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")

        self.driver = webdriver.Chrome(executable_path=r'C:/python36/chromedriver.exe', chrome_options=chrome_options)
        # self.driver = webdriver.Firefox(executable_path='C:/python36/geckodriver.exe')

        self.driver.get(urls)
        print(self.driver.title)

        # self.driver.find_element_by_xpath('.//*[@id="mainImg"]/a/img').location_once_scrolled_into_view
        time.sleep(1)
        self.driver.find_element_by_xpath('.//*[@id="mainImg"]/a/img').click()
        img_count = int(self.driver.find_element_by_xpath('//li[@class="js-cat-item on"]/a/em').text) - 1
        # img_count = 10
        while img_count > 0:
            # self.driver.find_element_by_xpath('//div[@class="next-seat js-next"]/a').location_once_scrolled_into_view
            self.driver.find_element_by_xpath('//div[@class="next-seat js-next"]/a').click()
            img_count -= 1
            print(img_count)
            time.sleep(1)
            if img_count <= 0:
                break
        # self.driver.find_element_by_xpath('.//*[@id="smallImages"]/li[1]/a/img').click()
        time.sleep(1)
        self.driver.quit()


if __name__ == '__main__':
    url = "http://hotel.qunar.com/city/beijing_city/dt-2714"
    url2 = "https://www.baidu.com"
    st = SeleniumTest()
    st.start(url)
