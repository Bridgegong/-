# -*- coding: utf-8 -*-
# @Time    : 2018/4/4 10:13
# @Author  : Bridge
# @Email   : 13722450120@163.com
# @File    : get_news_content.py
# @Software: PyCharm
from selenium import webdriver
import requests, time, os
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pymysql


class ShiYeJinFu():
    def __init__(self, idd, password):
        self.idd = idd
        self.password = password

    def get_login(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(19)
        try:
            input1 = driver.find_element_by_xpath('//*[@id="account"]')
        except:
            time.sleep(3)
            input1 = driver.find_element_by_xpath('//*[@id="account"]')
        driver.implicitly_wait(3)
        input1.send_keys(self.idd, Keys.ENTER)
        input2 = driver.find_element_by_id('pass')
        time.sleep(3)
        input2.send_keys(self.password, Keys.ENTER)
        time.sleep(3)
        f = open(r'D:\ZHiYin\shiyejinfu\urlss.txt')
        f.readline()
        for urls in f:
            print(urls)
            driver.get(url=urls)
            time.sleep(5)
            driver.implicitly_wait(8)
            driver.find_element_by_xpath('//*[@id="main-tabs"]/li[5]/a').click()
            time.sleep(3.6)
            try:
                nums = driver.find_element_by_xpath('//*[@id="company4b"]/header/div/span[2]/small').text
                print('共计' + nums + '条')
                n = 1
                for num in range(1, int(nums)+1):
                    part1 = '//*[@id="company4b"]/div/div[1]/table/tbody/tr['
                    part2 = ']/td[1]/div/a'
                    allxpath = part1 + str(n) + part2
                    print(allxpath)
                    try:
                        driver.find_element_by_xpath(allxpath).click()
                        time.sleep(3)
                        handles = driver.window_handles
                        driver.switch_to_window(handles[-1])
                        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="content"]'))
                        title = driver.find_element_by_xpath('/html/body/div/div/section/header/div/span[1]').text
                        print(title)
                        path = r'D:\SYAssss\\'
                        if not os.path.exists(path):
                            os.makedirs(path)
                        with open(path + 'B4-' + title + '.txt', 'a+', encoding='utf-8') as f:
                            f.write(driver.page_source)
                            driver.close()
                            driver.switch_to_window(driver.window_handles[0])
                            time.sleep(2)
                            if num % 20 == 0:
                                driver.find_element_by_xpath('//*[@id="company4b"]/div/div[2]/ul/li[3]/a').click()
                                n = 1
                            else:
                                n += 1
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)

    def main(self):
        URL = "https://www.seeyii.com/v2/login.html"
        self.get_login(URL)


if __name__ == '__main__':
    idd = u'18603117806'
    password = u'111111'
    sy = ShiYeJinFu(idd = idd, password = password).main()