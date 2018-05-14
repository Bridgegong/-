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
        #self.conn = pymysql.connect(host='localhost', db='zhiyin', user='root', passwd='123456', charset='utf8')
        #self.cur = self.conn.cursor()
        #if self.cur:
         #   print("连接成功")
        #else:
         #   print("连接失败")

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
        # f = open(r'D:\ZHiYin\syjf_news\AZ-urls.txt')
        # f.readline()
        # for urls in f:
        #     print(urls)
        urlz='https://www.seeyii.com/v2/routeStockDetail.html?t=2&e=Y29kZT0wMDIwNDkmc3ROYW1lPSVFNyVCNCVBQiVFNSU4NSU4OSVFNSU5QiVCRCVFOCU4QSVBRiZnVGltZVN0YW1wPTE1MjMzNjU3OTEyNDE='
        #driver.get(url='https://www.seeyii.com/v2/routeStockDetail.html?t=2&e=Y29kZT0wMDI4NDEmc3ROYW1lPSVFOCVBNyU4NiVFNiVCQSU5MCVFOCU4MiVBMSVFNCVCQiVCRCZleGNoYW5nZVR5cGU9MTAxJmdUaW1lU3RhbXA9MTUyMzMzOTM2ODY1MA==')
        driver.get(urlz)
        time.sleep(5)
        driver.implicitly_wait(8)
        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="content"]'))
        driver.find_element_by_xpath('//*[@id="main-tabs"]/li[11]/a').click()
        time.sleep(3.6)
        pageHtml = driver.page_source
        bea = BeautifulSoup(pageHtml, 'lxml')
        #print bea
        name = bea.find('span', 'stock-name').text.replace('*', '').strip()
        print(name)
        for num in range(1, 5):
            # driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="content"]'))
            # driver.find_element_by_xpath('//*[@id="main-tabs"]/li[11]/a').click()
            part1 = '//*[@id="news"]/section/div/ul/li['
            part2 = "]/a"
            allxpath = part1 + str(num) + part2
          
            try:
                driver.find_element_by_xpath(allxpath).click()
                time.sleep(3)
                handles = driver.window_handles
                driver.switch_to_window(handles[-1])
                title = driver.find_element_by_xpath('//*[@id="newsDetail"]/header/div/h2').text
                data = driver.find_element_by_xpath('//*[@id="newsDetail"]/header/div/div/span[2]').text
                url_old = driver.find_element_by_xpath('//*[@id="newsDetail"]/header/div/div/a').get_attribute('href')
                con = driver.find_element_by_xpath('//*[@id="newsDetail"]/div/div').text
                print(title)
                #print(data)
                print(num,url_old)
                #print(con)
                # sql = "insert into news_syjf(Url,Title,DateTime,Content,Froms,`Name`) VALUES ('%s','%s','%s','%s','%s','%s')" % (url_old, title, data, con, '视野', name)
                # try:
                #     self.cur.execute(sql)
                #     self.conn.commit()
                # except Exception as e:
                #     print(e)
                driver.close()
                driver.switch_to_window(driver.window_handles[0])
                
                # relocate news list
                driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="content"]'))
                
            except Exception as e:
                print(e)

    def main(self):
        URL = "https://www.seeyii.com/v2/login.html"
        self.get_login(URL)

if __name__ == '__main__':
    idd = u'13810595671'
    password = u'123456'
    sy = ShiYeJinFu(idd=idd, password=password).main()
