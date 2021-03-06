#!/usr/bin/python  
#-*- coding: UTF-8 -*-

"""登录北理工校园网

Usage:
    BIT_Log_In_CLI  <ID> <password>

Options:
    -h,--help        显示帮助菜单

Example:
    python BIT_Log_In_CLI.py 1120101111 123456
"""

import urllib
import urllib2
import cookielib
from docopt import docopt

arguments = docopt(__doc__)
ID = arguments['<ID>']
password = arguments['<password>']

# 登录页面，用于获取cookie
hosturl = 'http://10.0.0.55:803/srun_portal_pc.php?ac_id=1&'

# Post地址
posturl = 'http://10.0.0.55:803/include/auth_action.php'


# 处理cookie，在校园网登录中不需要
# filename = 'FileCookieJar.txt'

# cj = cookielib.LWPCookieJar(filename)
# cj.save();
# cookie_support = urllib2.HTTPCookieProcessor(cj)
# opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
# urllib2.install_opener(opener)

# h = urllib2.urlopen(hosturl)

# header数据，通过抓包获得
headers = {'Referer' : 'http://10.0.0.55:803/srun_portal_pc.php?ac_id=1&',
		   'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
		   }

# 构造Post数据，通过抓包获得
data = {'action' : 'login',  
            'username' : ID, 
            'password' : password, 
            'ac_id' : '1',  
            'save_me' : '1',
            'ajax' : '1'
            }

# 对Post数据编码
data = urllib.urlencode(data)

request = urllib2.Request(posturl, data, headers)
response = urllib2.urlopen(request)
text = response.read()
if text[0:8] == 'login_ok':
    text = '登录成功'
print text.decode('UTF-8')