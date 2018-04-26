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
class RloeManage ():
    """角色管理"""
    def __init__(self,driver,acc=None):
        self.driver = driver
        self.accounts = acc
    def RloeAdd(self):
        """角色新增"""
        log.info("------新增角色------")
        dr = Student(self.driver)
        dr.click("css", "body > div.topTools > div.actionBar > div > a")  # 新增
        dr.send_ke("id","_easyui_textbox_input3",self.accounts) # 角色名称
        dr.send_ke("name","roledesc","自动化测试添加角色")
        dr.click("link_text","提交")

    def RloeQuert(self):
        """角色查询"""
        dr = Student(self.driver)
        time.sleep(1)
        log.info("------查询角色为：%s------" % self.accounts)
        dr.send_ke("id","_easyui_textbox_input1",self.accounts) #根据账户查询
        dr.click("link_text","查询")
if __name__ == '__main__':
    #单元测试
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\GoogleFile'}
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path='D:\\python36\\chromedriver.exe', chrome_options=options)
    driver.get("http://192.168.0.16:8080/HRAS/login.jsp")
    Login_HR(driver).login("laozi","a123456")
    dr = Student(driver)
    dr.click("xpath", "//*[@id='_easyui_tree_6']/span[3]")
    dr.click("xpath", "//*[@id='_easyui_tree_8']/span[4]/a/span")
    driver.switch_to_frame("127")
    #从这里开始调用上面写的方法
    RloeManage(driver,"学士证").RloeAdd()
    RloeManage(driver,"学士证").RloeQuert()
