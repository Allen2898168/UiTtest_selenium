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
class UserManage ():
    """用户信息管理"""
    def __init__(self,driver,acc=0):
        self.driver = driver
        self.accounts = acc
    def UserAdd(self):
        """用户新增"""
        log.info("------新增用户------")
        dr = Student(self.driver)
        dr.click("xpath", "/html/body/div[1]/div[1]/div/a[3]")  # 新增
        dr.send_ke("id","_easyui_textbox_input11",self.accounts) # 用户账户
        # 去掉元素的readonly属性
        js = 'document.getElementById("_easyui_textbox_input14").removeAttribute("readonly");'
        self.driver.execute_script(js)
        now = datetime.date.today() + datetime.timedelta(days=365)
        now = str(now)
        dr.send_ke("id", "_easyui_textbox_input14",now)
        js_V = 'document.getElementById("_easyui_textbox_input15").removeAttribute("readonly");'
        self.driver.execute_script(js_V)
        now_Y = datetime.date.today() + datetime.timedelta(days=365)
        now_Y = str(now_Y)
        dr.send_ke("id", "_easyui_textbox_input15", now_Y)
        dr.send_ke("id", "_easyui_textbox_input12", "普通用户")
        time.sleep(0.5)
        self.driver.find_element_by_id("_easyui_textbox_input12").send_keys(Keys.ENTER)
        dr.click("xpath", "//*[@id='FormUpdate']/div/div/table/tbody/tr[6]/td[2]/span[1]/span/a")
        names = dr.elements("css","body > div:nth-child(10) > div >div")
        name = random.randint(1, len(names))
        dr.click("xpath", "//body/div[9]/div/div[%d] "%name)
        Job = dr.element("id","staffnoShow").text
        log.info("------绑定的员工工号为%s------" % Job)
        dr.send_ke("name","remark","自动化测试添加")
        dr.click("link_text","提交")

    def UserQuert(self):
        """用户查询"""
        dr = Student(self.driver)
        time.sleep(2)
        log.info("------查询用户为：%s------" % self.accounts)
        dr.send_ke("id","_easyui_textbox_input1",self.accounts) #根据账户查询
        dr.click("link_text","查询")
        time.sleep(1)

        # 这是修改的代码
        # drdrdr.click("id","_easyui_textbox_input21")
        # drdrdr.click("class","datebox-button-a")
        # drdrdr.click("id","_easyui_textbox_input22")
        # drdrdr.click("xpath","/html/body/div[11]/div/div[2]/table/tbody/tr/td[1]/a")
        # dr.click("link_text","提交")

    def UserExportOptions(self):
        '''导出所选项'''
        dr = Student(self.driver)
        dr.click("link_text","重置")#重置查询条件初始化
        try:
            dr.click("xpath", "//*[@id='tt']/div[1]/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/input")
            self.driver.find_element_by_xpath("//*[@id='tt']/div[1]/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/input").is_selected() #判断元素是否选中
            dr.click("css", "body > div.topTools > div.actionBar > div > a:nth-child(1)")
        except Exception as e:
            print('Test fail{0}', format(e))

    def UserExportWhole(self):
        """导出全部"""
        dr = Student(self.driver)
        dr.click("xpath","/html/body/div[1]/div[1]/div/a[2]")
        time.sleep(1)
if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\GoogleFile'}
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path='D:\\python36\\chromedriver.exe', chrome_options=options)
    driver.get("http://192.168.0.16:8080/HRAS/login.jsp")
    Login_HR(driver).login("laozi","a123456")
    driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/a").click()
    dr = Student(driver)
    dr.click("xpath", "//*[@id='_easyui_tree_6']/span[3]")
    dr.click("xpath", "//*[@id='_easyui_tree_7']/span[4]/a/span")
    frame = driver.find_element_by_xpath("//*[@id='161']")
    driver.switch_to.frame(frame)
    UserManage(driver,222).UserAdd()
    UserManage(driver,222).UserQuert()
    UserManage(driver).UserExportOptions()
    UserManage(driver).UserExportWhole()
