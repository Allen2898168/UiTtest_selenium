# -!- coding: utf-8 -!-
import configparser  #配置文件
import os
import time
import unittest

import xlrd
from selenium import webdriver

from HRXT.case.object_common.UserManage.usermanage import UserManage
from HRXT.case.object_common.login.Login import Login_HR  #导入登录模块
from HRXT.uidriver.location import Student
from HRXT.uidriver.loggin import Log

log = Log()
#读取配置文件
con_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir+"\\config"))
config_path = os.path.join(con_path, "config.ini")
config = configparser.ConfigParser()
config.read(config_path,encoding="utf-8-sig")
username = config.get('driverLogin','admin')  # 账户
password = config.get('driverLogin', 'adpassword')  # 密码
URL = config.get('testServer','URL')  # URL
user = config.get('testuser', 'username')  # 用户新增账号
DowPath = config.get('chromedriver', 'DowPath')


class test_case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log.info("------用户信息管理模块测试用例------")
        # 只需要修改download.default_directory：路径，谷歌默认下载路径，而且不弹窗。1弹框，0不弹窗
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\GoogleFile'}
        options.add_experimental_option('prefs', prefs)
        cls.driver = webdriver.Chrome(executable_path='D:\\python36\\chromedriver.exe', chrome_options=options)  # 谷歌

        # 无界面执行自动化
        # cls.driver = webdriver.PhantomJS()
        cls.driver.get(URL)
        global dr
        title1 = cls.driver.title
        dr = Student(cls.driver)   # 实例化二次开发定位方法
        login = Login_HR           # 实例化登录方法
        try:
            assert title1 in '登录'
            log.info("------进入网站------")
        except:
            print('进入网站失败，请检查服务是否启动')
        login(cls.driver).login(username,password)   # 调用登录方法
        cls.driver.maximize_window()

        # 进入页面操作
        dr.click("xpath", "//*[@id='_easyui_tree_7']/span[3]")   # 展开用户角色管理 列表
        dr.click("xpath", "//*[@id='_easyui_tree_8']/span[4]/a/span")   # 点击用户信息管理
        cls.driver.switch_to.frame("161")
    def test_01(self):
        """用户新增"""
        log.info("------测试用户新增------")

        UserManage(self.driver,user).UserAdd()   # 调用用户信息新增方法
    def test_02(self):
        """查询用户"""
        log.info("-----测试查询用户------")
        UserManage(self.driver,user).UserQuert()
        lis = dr.elements("xpath", "//*[@id='tt']/div[1]/div/div[1]/div[2]/div[2]/table/tbody/tr")
        x = 1
        while True:
            li = len(lis)+1
            for x in range(1,li):
                i = dr.element("xpath", "//*[@id='tt']/div[1]/div/div[1]/div[2]/div[2]/table/tbody/tr[%d]/td[2]/div" % x).text
                if i == user:
                    try:
                        dr.click("xpath", "//*[@id='datagrid-row-r1-2-0']/td[10]/div/a[3]/img")
                        log.info("------删除账户为：%s的信息------" % user)
                        dr.click("link_text", "确定")  # 删除数据
                    except Exception:
                        log.warning("------无法定位到删除按钮，请检查截图------" )
                        files_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
                        files_path = files_path + "\\Warehouse\\screenshot"
                        times = time.strftime("%Y-%d-%m %H%M%S")
                        files = os.path.join(files_path, "用户数据删除异常%s.jpg" % times)
                        self.driver.get_screenshot_as_file(files)
                    break
                elif i != user:
                    x += 1
                elif i <= 11:
                    break
            return x
    def test_03(self):
        """导出所选项"""
        log.info("------测试导出所选项，默认勾选第一页全部------")
        UserManage(self.driver).UserExportOptions()   # 调用导出所选项封装方法
        lis = dr.elements("xpath", "//*[@id='tt']/div[1]/div/div[1]/div[2]/div[2]/table/tbody/tr")
        log.info("------有%d条信息,即将导出------" % len(lis))
        # 检查导出文件以及excel
        new_file = dr.new_file('d:\\GoogleFile')
        excelfile = xlrd.open_workbook(new_file)
        sheet = excelfile.sheet_by_index(0)  # 读取第一个sheet
        Choices = sheet.nrows - 1   # 读取excel行数
        lia = len(lis)
        if lia == Choices:
            log.info("------导出所选项excel行数与列表数量一致------")
        else:
            log.info("导出的页面数量有%d,excel的行数有%d"%lia,Choices)
    def test_04(self):
        log.info("------测试导出全部------")
        UserManage(self.driver).UserExportWhole()  # 调用导出所选项封装方法
        Number = dr.element("xpath", "//*[@id='tt']/div[1]/div/div[2]/div[1]").text
        Number = Number[8:]
        Number = Number[:-2]
        time.sleep(2)
        new_file = dr.new_file('d:\\GoogleFile')
        excelfile = xlrd.open_workbook(new_file)
        sheet = excelfile.sheet_by_index(0)
        excels = sheet.nrows - 1
        Number = int(Number)
        if Number == excels:
            log.info("------导出全部excel行数与列表数量一致------")
        else:
            log.info("导出全部的页面数量有%d,excel的行数有%d" % Number, excels)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        log.info("------测试用例结束------")
        log.info("------清理下载的附件所有附件------")
        for i in os.listdir(DowPath):
            path_file = os.path.join(DowPath,i)
            log.info("------清理下载的附件%s------" % path_file)
            os.remove(path_file)

if __name__ == '__main__':
    unittest.main()

