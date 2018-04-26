#conding= utf-8
'''
记录功能
logging.debug（'此功能提供详细信息'）
logging.warning（'意外发生'）
logging.error（'用于存储异常跟踪'）
logging.info（'确认事情正在按计划进行）'
logging.critical（'要执行的主要操作失败）

日志记录级别
Info是最低级别，即如果我们配置了“WARNING”的日志，
我们的日志文件将包含WARNING，ERROR＆CRITICAL的日志。默认日志消息是WARNING
DEBUG
INFO（信息 ）
WARNING（警告）
ERROR（错误）
CRITICAL（危急）
'''
from selenium import webdriver
import logging
import unittest
import os
import time



# log_path= os.path.join(os.path.dirname(),"log")
# log_path = os.path.dirname(os.getcwd())+"\log"
log_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
log_path = log_path+"\\Warehouse\\log"

class Log:
    def __init__(self):
        #文件的命名
        self.logname = os.path.join(log_path, '%s.log' %time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        #日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')
    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        # fh = logging.FileHandler(self.logname, 'a')# 追加模式
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')# 这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level =='info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level =='warning':
            self.logger.warning(message)
        elif level =='error':
            self.logger.error(message)
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        #关闭打开的文件
        fh.close()
    def debug(self, message):
        self.__console('debug', message)
    def info(self, message):
        self.__console('info', message)
    def warning(self, message):
        self.__console('warning', message)
    def error(self, message):
        self.__console('error', message)
if __name__ == '__main__':
    log = Log()
    log.info("---测试开始---")
    log.info('输入密码')
    log.warning("---测试结束---")
