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
class RloeAssig ():
    """角色功能权限"""
    def __init__(self,driver,acc=None):
        self.driver = driver
        self.accounts = acc
    def RloeQuert(self):
        """角色功能查询"""
        dr = Student(self.driver)
        time.sleep(1)
        log.info("------搜索角色功能为：%s------" % self.accounts)
        dr.send_ke("id","kw",self.accounts) #根据账户查询
        time.sleep(0.1)
        role = dr.elements("xpath","//*[@id='append']/div")
        log.info("------共搜索出%s个角色名称------" % len(role))
        dr.click("xpath","//*[@id='append']/div[1]")
        system = dr.element("xpath",'//*[@id="functionTr"]/li[1]/div/span[3]').is_selected()  #判断系统管理是否被选中
        if system == True:
            print("已分系统管理配权限")
            dr.click("xpath", '//*[@id="functionTr"]/li[1]/div/span[3]')  # 反选取消选中
            dr.click("xpath", '//*[@id="functionTr"]/li[1]/div/span[3]')  # 重新选中
        elif system == False:
            dr.click("xpath",'//*[@id="functionTr"]/li[1]/div/span[3]')

        hr = dr.element("xpath",'//*[@id="functionTr"]/li[2]/div/span[3]').is_selected()  # 判断人事系统是否被选中
        if hr == True:
            print("已分配人事系统权限")
            dr.click("xpath","//*[@id='functionTr']/li[2]/div/span[3]")  # 反选取消选中
            dr.click("xpath","//*[@id='functionTr']/li[2]/div/span[3]")  # 重新选中
        elif system == False:
            dr.click("xpath", '//*[@id="functionTr"]/li[2]/div/span[3]')
        dr.click("xpath","/html/body/div[2]/div[2]/a/span/span[1]")  #保存
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
    driver.switch_to.frame("152")
    # 从这里开始调用上面写的方法
    RloeAssig(driver,"Diploma").RloeQuert()
