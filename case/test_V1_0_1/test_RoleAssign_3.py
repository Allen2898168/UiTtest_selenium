# -!- coding: utf-8 -!-
import configparser  # 配置文件
import os
import time
import unittest

from selenium import webdriver

from HRXT.case.object_common.UserManage.roleassign import RloeAssig
from HRXT.case.object_common.login.Login import Login_HR  #导入登录模块
from HRXT.uidriver.location import Student
from HRXT.uidriver.loggin import Log

log = Log()
log.
#读取配置文件
con_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir+"\\config"))
config_path = os.path.join(con_path, "config.ini")
config = configparser.ConfigParser()
config.read(config_path,encoding="utf-8-sig")
username = config.get('driverLogin','admin')  # 账户
password = config.get('driverLogin', 'adpassword')  # 密码
URL = config.get('testServer','URL')  # URL
role = config.get('testuser', 'rolename')  # 角色
DowPath = config.get('chromedriver', 'DowPath')  # 下载文件的路径

class test_case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log.info("------角色功能分配模块测试用例------")
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
        dr.click("xpath", "//*[@id='_easyui_tree_10']/span[4]/a/span")   # 点击用户信息管理
    def test_01(self):
        """角色功能分配"""
        log.info("------测试角色功能分配------")
        self.driver.switch_to.frame("152")
        RloeAssig(self.driver,role).RloeQuert()  # 调用角色功能分配方法
        time.sleep(0.5)
        cant = dr.element_wait("xpath","/html/body/div[5]/div[2]").text
        if cant == "提交成功":
            log.info("------角色功能分配成功------")
        else:
            log.warning("------角色功能分配异常，请检查截图------")
            files_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
            files_path = files_path + "\\Warehouse\\screenshot"
            times = time.strftime("%Y-%d-%m %H%M%S")
            files = os.path.join(files_path, "角色功能分配异常%s.jpg" % times)
            self.driver.get_screenshot_as_file(files)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()

