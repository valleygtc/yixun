import os
import configparser
from selenium import webdriver
#实例化一个configparser实例
config=configparser.ConfigParser()
#从yixun.cfg中读取配置（账号与密码）
with open("yixun.cfg") as cfgfile:
    config.read_file(cfgfile)
acc=config.get('info','acc')
pwd=config.get('info','pwd')


pipe=os.popen('yixun.exe '+acc)
acc_enc_headers=pipe.read()
acc_enc_url='\r\n'+acc_enc_headers
pipe.close()


browser=webdriver.Chrome()
browser.get('http://admin:admin@192.168.1.1')




