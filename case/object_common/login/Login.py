import unittest
from selenium import webdriver
import time

from HRXT.uidriver.loggin import Log
log = Log()

class Login_HR():
    def __init__(self,driver):
         self.driver = driver
    def input_user(self,username):
        '''输入用户名'''
        log.info("------输入登录用户名------")
        self.driver.find_element_by_id("useraccount").clear()
        self.driver.find_element_by_id("useraccount").send_keys(username)

    def input_pasw(self,psw):
        '''输入密码'''
        log.info("------输入登录密码------")
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id('password').send_keys(psw)
    def click(self):
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/a").click()  # 点击

    def login(self,username,psw):
        '''登录公共方法'''
        self.input_user(username)
        self.input_pasw(psw)
        self.click()
