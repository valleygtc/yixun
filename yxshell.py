import requests
acc='23801002202'
pwd='658572'
site = "http://192.168.1.1/userRpm/PPPoECfgRpm.htm\
?wan=0&wantype=2&acc=%0D%0A"+acc+"&psw="+pwd+"&confirm="+pwd+"\
&specialDial=100&SecType=0&sta_ip=0.0.0.0&sta_mask=0.0.0.0\
&linktype=4&&waittime2=0&Connect=%C1%AC+%BD%D3"
cookies={'traffic_warning_NaN':'2016.8:1'}
