#conding=utf-8
from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
#二次开发定位方法
class Student():
    def __init__(self,driver):
        self.driver = driver
        if driver == 'firefox' or driver == 'Firefox' or driver == 'f' or driver == 'F':

            self.driver = webdriver.Firefox()

        elif driver == 'Ie' or driver == 'ie' or driver == 'i' or driver == 'I':

            self.driver = webdriver.Ie()

        elif driver == 'Chrome' or driver == 'chrome' or driver == 'Ch' or driver == 'ch':

            self.driver = webdriver.Chrome()

        else:

            raise NameError('只能输入firefox,Ie,Chrome')


    # def element_wait(self, fangfa, dingwei, wati=6):  # 等待
    #
    #     if fangfa == "id":
    #         try:
    #             WebDriverWait(self.driver, wati,1).until(EC.presence_of_element_located((By.ID, dingwei)))
    #             return self.driver.find_element(By.ID,dingwei)
    #         except Exception :
    #             return  print("页面元素未找到%s元素"%(dingwei))
    #     else:
    #         raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css'.")
    def element(self,fangfa,dingwei):#定位
        if fangfa=='id':
            element=self.driver.find_element_by_id(dingwei)
        elif fangfa == "name":
            element = self.driver.find_element_by_name(dingwei)
        elif fangfa == "class":
            element = self.driver.find_element_by_class_name(dingwei)
        elif fangfa == "link_text" or fangfa == "text":
            element = self.driver.find_element_by_link_text(dingwei)
        elif fangfa == "xpath":
            element = self.driver.find_element_by_xpath(dingwei)
        elif fangfa == "tag":
            element = self.driver.find_element_by_tag_name(dingwei)
        elif fangfa == "css":
            element = self.driver.find_element_by_css_selector(dingwei)
        else:
            raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")
        return element
    def element_wait(self, fangfa, dingwei, wati=10 ,time=0.5):  # 封装显性等待

        if fangfa == "id":

            element = WebDriverWait(self.driver, wati, time).until(EC.visibility_of_element_located((By.ID, dingwei)))
            return element
        elif fangfa == "name":

            element = WebDriverWait(self.driver, wati, time).until(EC.visibility_of_element_located((By.NAME, dingwei)))
            return element
        elif fangfa == "class":

            element = WebDriverWait(self.driver, wati, time).until(EC.visibility_of_element_located((By.CLASS_NAME, dingwei)))
            return element
        elif fangfa == "link_text" or fangfa == "text":

            element = WebDriverWait(self.driver, wati, time).until(EC.visibility_of_element_located((By.LINK_TEXT, dingwei)))
            return element
        elif fangfa == "xpath":

            element = WebDriverWait(self.driver, wati, time).until(EC.visibility_of_element_located((By.XPATH, dingwei)))
            return element
        elif fangfa == "css":

            element = WebDriverWait(self.driver, wati, time).until(EC.visibility_of_element_located((By.CSS_SELECTOR, dingwei)))
            return element
        else:

            raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css'.")

    def elements(self, fangfa, dingwei):  # 组定位

        if fangfa == 'id':

            elements = self.driver.find_elements_by_id(dingwei)

        elif fangfa == "name":

            elements = self.driver.find_elements_by_name(dingwei)

        elif fangfa == "class":

            elements = self.driver.find_elements_by_class_name(dingwei)

        elif fangfa == "link_text" or fangfa == "text":

            elements = self.driver.find_elements_by_link_text(dingwei)

        elif fangfa == "xpath":

            elements = self.driver.find_elements_by_xpath(dingwei)

        elif fangfa == "tag":

            elements = self.driver.find_elements_by_tag_name(dingwei)

        elif fangfa == "css":

            elements = self.driver.find_elements_by_css_selector(dingwei)

        else:

            raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")

        return elements

    def send_ke(self, fangfa, dingwei, text):  # 发送内容
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        e1.clear()
        e1.send_keys(text)

    def click(self, fangfa, dingwei):  # 单击
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        e1.click()

    def new_file(self,test_report):
        try:
            lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
            lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))  # 按时间排序
            file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
            return file_new
        except IndexError :
            print("请检查文件是否下载成功")
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.get("http://www.baidu.com")
#     driver_n = Student(driver)
#     # 去掉元素的readonly属性
#     # js = 'document.getElementById("_easyui_textbox_input14").removeAttribute("readonly");'
#     # driver.execute_script(js)
#     # driver_n.click("id", "kw")
#     driver_n.send_ke("id", "kw",123456)
#     print("上面异常了，但我还是会执行")