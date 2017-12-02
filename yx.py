# author:valleygtc 2017/3/11
# copyright:随便copy

import os
import time
import configparser
from selenium import webdriver

# 读取配置
# （1）实例化一个configparser实例
# （2）从yixun.cfg中读取配置（路由器、翼讯的账号与密码）
config = configparser.ConfigParser()

with open("yixun.cfg") as cfgfile:
    config.read_file(cfgfile)
rou_acc = config.get('router', 'acc')
rou_psw = config.get('router', 'psw')
yx_acc = config.get('yixun', 'acc')
yx_psw = config.get('yixun', 'psw')

# 浏览器自动化操作
browser = webdriver.Chrome()
browser.get('http://{0}:{1}@192.168.1.1'.format(rou_acc, rou_psw))
# （1）点入设置界面
'''
1.有iframe的话，必须要先选入该frame才可以选择其中的element否则会报错显示无该element
2.switch到一个frame后，必须返回来才能switch到另一个frame和另一个frame中的东西
'''
browser.switch_to.frame("bottomLeftFrame")
ele = browser.find_element_by_id('a3')
ele.click()

browser.switch_to.default_content()
browser.switch_to.frame("mainFrame")
# （2）填入密码
ele = browser.find_element_by_name('psw')
ele.clear()
ele.send_keys(yx_psw)

ele = browser.find_element_by_name('confirm')
ele.clear()
ele.send_keys(yx_psw)

# （3）修改HTML
browser.execute_script(
    '''
    var input=document.querySelectorAll("input[name=acc]")[0];
    var parent=document.querySelectorAll("form \
    table tbody tr td table tbody tr td table tbody tr td")[7];
    var textarea=document.createElement("textarea");
    textarea.name="acc";
    parent.removeChild(input);
    parent.appendChild(textarea);''')
# （4）获取并填入加密账号
yx_acc_enc = '\r\n' + yx_acc
ele = browser.find_element_by_name('acc')
ele.clear()
ele.send_keys(yx_acc_enc)

# （5）click button

button = browser.find_element_by_name("Connect")
button.click()
