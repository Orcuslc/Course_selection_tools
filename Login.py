# Login
# coding:utf-8
import urllib.request
import urllib.response
import urllib.parse
import io
import sys
from get_login_data import idnum, password

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')
url = 'https://uis1.fudan.edu.cn/amserver/UI/Login?gx_charset=UTF-8&goto=http://jwfw.fudan.edu.cn/eams/home.action'

values = {
	'IDToken0':'',
	'IDToken1':idnum,
	'IDToken2':password,
	'IDButton':'Submit',
	'goto':'aHR0cDovL2p3ZncuZnVkYW4uZWR1LmNuL2VhbXMvaG9tZS5hY3Rpb24=',
	'encoded':'true',
	'inputCode':'',
	'gx_charset':'UTF-8'
	}

data = urllib.parse.urlencode(values).encode('utf-8')
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
info = response.read().decode('utf-8')
print(info)