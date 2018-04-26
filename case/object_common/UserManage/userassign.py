# -!- coding: utf-8 -!-
from selenium import  webdriver
from selenium.webdriver.common.by import By
from HRXT.uidriver.loggin import Log
from HRXT.uidriver.location import Student
from HRXT.case.object_common.login.Login import Login_HR
import time,datetime,random
from selenium.webdriver.common.keys import Keys
import os
import xlrd
log = Log()
class UserAssig ():
    """用户角色权限分配"""
    def __init__(self,driver,acc=None):
        self.driver = driver
        self.accounts = acc
    def UserQuert(self):
        """用户数据权限-查询"""
        dr = Student(self.driver)
        time.sleep(1)
        log.info("------搜索用户账户为：%s------" % self.accounts)
        dr.send_ke("id","_easyui_textbox_input2",self.accounts) #根据账户查询
        dr.click("link_text","查询")

    def UserAss(self):
        dr = Student(self.driver)

if __name__ == '__main__':
    # 单元测试
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\GoogleFile'}
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path='D:\\python36\\chromedriver.exe', chrome_options=options)
    driver.get("http://192.168.0.16:8080/HRAS/login.jsp")
    Login_HR(driver).login("laozi","a123456")
    dr = Student(driver)
    dr.click("xpath", "//*[@id='_easyui_tree_6']/span[3]")
    dr.click("xpath", "//*[@id='_easyui_tree_9']/span[4]/a/span")
    driver.switch_to.frame("223")
    # 从这里开始调用上面写的方法
    RloeAssig(driver,"Diploma").RloeQuert()
