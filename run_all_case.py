# coding:utf-8
from selenium import  webdriver
import unittest
import os
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from HRXT.uidriver.loggin import Log
import smtplib
import time
log = Log()
#==============定义发送邮件==========
def send_mail(file_new):
    log.info("------获取邮箱账户密码------")
    _user = '1024547862@qq.com'  # 发件地址
    _pwd="lfwwfjridtiqbdid"     # 服务器授权码
    _to="1620596776@qq.com"

    with open(file_new, "rb") as f:
        mail_body = f.read()
    msg = MIMEMultipart()
    body = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    msg['From'] = _user
    msg['To'] = _to
    msg.attach(body)
    #
    #
    #添加附件
    log.info("------添加测试报告附件------")
    att=MIMEText(open(report_file,"rb").read(),"base64","utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "testcase.html"'
    msg.attach(att)

    #
    #
    #发送邮件
    s = smtplib.SMTP_SSL("smtp.qq.com")
    # s.set_debuglevel(1)
    s.login(_user,_pwd)  # 登录邮箱的账户和密码
    s.sendmail(_user,_to, msg.as_string())

    s.quit()

    log.info("------发送邮件------")
    print('自动化邮件已发送')

#======查找测试目录，找到最新生成的测试报告文件======
def new_report(test_report):
    lists = os.listdir(test_report)                                    #列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn:os.path.getmtime(test_report + "\\" + fn))#按时间排序
    file_new = os.path.join(test_report,lists[-1])                     #获取最新的文件保存到file_new
    print(file_new)
    return file_new
if __name__ == "__main__":
    # unittest.TextTestRunner()

    test_report=os.path.join(os.getcwd(),"Warehouse\\report")   # 报告存放路径

    case_path =os.path.join(os.getcwd(),"case\\test_V1_0_1")  #用例路径

    report_file = new_report(test_report)# 获取最新的测试报告

    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern="test_UserInfo_1.py",  # 匹配test*.py
                                                   top_level_dir=None)
    print(discover)
    # return discover
#======================测试报告============================
    # html报告文件内容
    now=time.strftime("%Y-%m-%d-%H-%M-%S")   #加时间戳
    report_abspath = os.path.join(test_report, "result"+now+".html")
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner(stream=fp,title='自动化测试报告,测试结果如下：',description='用例执行情况：',verbosity=2)

    # 调用函数返回值
    runner.run(discover)
    fp.close()
    new_report = new_report(test_report)
    send_mail(new_report)  # 发送测试报告

#通过主函数执行用例
#从注册到发布信息
#执行完成发生邮件，生成测试报告