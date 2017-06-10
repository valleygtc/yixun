# 西安翼讯网络破解程序（TP-Link）

## 写在前面:
1. 依赖：chrome浏览器的webdriver（想用其他浏览器可以自行更改yx.py文件）
2. 运行目录中的exe文件是在win10下使用gcc（Code Block）编译的，其他平台请自行编译source目录中的my_yixun.c->yixun.exe


## 使用方法：
1. 下载chrome浏览器及其webdriver，并把webdriver加入环境变量
2. 下载此处的运行目录
3. 设置yixun.cfg（填入翼讯账号和密码）
4. 运行yx.exe即可


## 文件说明：
- 运行：
 - yixun.cfg:设置文件（翼讯账号密码）
 - yixun.exe:获取加密后的账号（源：my_yixun.c+md5lib.h）
 - yx.exe:读取cfg，与yixun.exe通信获取加密账号，控制浏览器自动操作完成路由器拨号上网（源：yx.py）
- source：.exe文件的源代码


## 实现原理：
1. 获取加密账号
2. 使用selenium模拟浏览器自动化操作


### 注：
获取加密算法的程序yixun.exe（source:my_yixun.c+md5lib.h）来自https://github.com/lanhao34/yixun


我只是进行了一点修改，并使用python+selenium进行包装
