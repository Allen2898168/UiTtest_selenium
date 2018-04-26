# -!- coding: utf-8 -!-
import configparser  # 配置文件
import os
import time
import unittest

from selenium import webdriver
from PIL import Image
from HRXT.case.object_common.UserManage.dataassign import DataAssig
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
sname = config.get('testuser', 'sname')  # 角色
DowPath = config.get('chromedriver', 'DowPath')  # 下载文件的路径

class test_case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log.info("------用户数据权限分配模块测试用例------")
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
            log.warning("------进入网站失败，请检查服务是否启动------")
        login(cls.driver).login(username,password)   # 调用登录方法
        cls.driver.maximize_window()

        # 进入页面操作
        dr.click("xpath", "//*[@id='_easyui_tree_7']/span[3]")   # 展开用户角色管理 列表
        dr.click("xpath", "//*[@id='_easyui_tree_11']/span[4]/a/span")   # 点击用户信息管理
        cls.driver.switch_to.frame("223")

    def test_01(self):
        """用户数据权限分配-查询"""
        log.info("------测试用户数据功能分配-查询------")
        DataAssig(self.driver,sname).DataQuert()  # 调用用户数据权限查询方法
        time.sleep(0.5)
        lis = dr.elements("xpath", "/html/body/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/table/tbody/tr")
        log.info("------搜索用户账户为：{0}，共有{1}条数据------".format(sname, len(lis)))

        # 循环列表选择
        x = 1
        while True:
            li = len(lis) + 1
            for x in range(1, li):
                i = dr.element("xpath","/html/body/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/table/tbody/tr[%s]/td[2]/div" % x).text
                if i == sname:
                    dr.click("xpath","/html/body/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/table/tbody/tr[%s]/td/div/input" % x)
                    break
                elif i != sname:
                    x += 1
                elif i <= 11:
                    break
            return x
    def test_02(self):
        """用户数据权限分配-分配"""
        log.info("------测试用户数据功能分配-分配------")
        time.sleep(0.4)
        DataAssig(self.driver).DataAss()  # 调用用户数据权限分配方法

        self.driver.save_screenshot('button.png')
        element = self.driver.find_element_by_xpath("//*[@id='dept']/li/div/span[3]")
        print(element.location)  # 打印元素坐标
        print(element.size)  # 打印元素大小
        left = element.location['x']
        top = element.location['y']
        right = element.location['x'] + element.size['width']
        bottom = element.location['y'] + element.size['height']
        im = Image.open('button.png')
        im = im.crop((left, top, right, bottom))
        im.save('button.png')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()

