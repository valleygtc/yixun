import os,time
import configparser
from selenium import webdriver
#实例化一个configparser实例
config=configparser.ConfigParser()
#从yixun.cfg中读取配置（账号与密码）
with open("yixun.cfg") as cfgfile:
    config.read_file(cfgfile)
acc=config.get('info','acc')
psw=config.get('info','pwd')

browser=webdriver.Chrome()
browser.get('http://admin:admin@192.168.1.1')
#点入设置界面
'''
1.有iframe的话，必须要先选入该frame才可以选择其中的element否则会报错显示无该element
2.switch到一个frame后，必须返回来才能switch到另一个frame和另一个frame中的东西
'''
browser.switch_to.frame("bottomLeftFrame")
ele=browser.find_element_by_id('a3')
ele.click()

browser.switch_to.default_content()
browser.switch_to.frame("mainFrame")
#填入密码
ele=browser.find_element_by_name('psw')
ele.clear()
ele.send_keys(psw)

ele=browser.find_element_by_name('confirm')
ele.clear()
ele.send_keys(psw)

#修改HTML
browser.execute_script(    
    '''
    var input=document.querySelectorAll("form table tbody tr td table tbody tr td table tbody tr td input")[1];
    var parent=document.querySelectorAll("form table tbody tr td table tbody tr td table tbody tr td")[7];
    var textarea=document.createElement("textarea");
    textarea.name="acc";
    parent.removeChild(input);
    parent.appendChild(textarea);''')
#获取并填入加密账号
pipe=os.popen('yixun.exe '+acc)
acc_enc='\r\n'+pipe.read()
pipe.close()
ele=browser.find_element_by_name('acc')
ele.clear()
ele.send_keys(acc_enc)

#click button

button=browser.find_element_by_name("Connect")
button.click()



