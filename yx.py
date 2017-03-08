import os
import requests
import configparser
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
print(acc_enc_url)


'''路由器使用的是http协议中的Basic认证。通过认证的方法：
1.在HTTP header中加入Authentication字段,value貌似为username:password的base64编码
2.URL中直接使用：http://username:password@...
3.requests module中直接使用requests.get('url',auth=(username,password))
'''

'''URL参数解释：
wantype:form中的拨号选择字段的name，value:2为PPPOE
acc:form中的账号字段的name（%0D%0A是ASCII码中的\r\n）
'''
payload={
    'wan':'0',
    'wantype':'2',
    'acc':acc_enc_url,
    'psw':pwd,
    'confirm':pwd,
    'specialDial':'100',
    'SecType':'0',
    'sta_ip':'0.0.0.0',
    'sta_mask':'0.0.0.0',
    'linktype':'4',
    'waittime2':'0',
    'Connect':'连 接'
}
headers={
    'wan':'0',
    'wantype':'2',
    'acc':acc_enc_headers,
    'psw':pwd,
    'confirm':pwd,
    'specialDial':'100',
    'SecType':'0',
    'sta_ip':'0.0.0.0',
    'sta_mask':'0.0.0.0',
    'linktype':'4',
    'waittime2':'0'
}
cookies={'traffic_warning_NaN':'2016.8:1'}#这个cookie是从chrome开发者工具中查到的
resp=requests.get('http://192.168.1.1',auth=('admin','admin'),cookies=cookies,
    params=payload,headers=headers)
print(resp.text)
print(resp.url)
print(resp.request.headers)
os.system('pause')

'''此为一个成功上了网的url（method:GET）（使用chrome开发者工具捕获）
yixun.exe中：

'TR8; 9323801002202

http://192.168.1.1/userRpm/PPPoECfgRpm.htm?
wan=0
&wantype=2
&acc=%0D%0A%27TR8%3B+9323801002202
&psw=658572
&confirm=658572
&specialDial=100
&SecType=0
&sta_ip=0.0.0.0
&sta_mask=0.0.0.0
&linktype=4
&waittime2=0
&Connect=%C1%AC+%BD%D3
'''



#cookie:traffic_warning_NaN=2016.8:1





