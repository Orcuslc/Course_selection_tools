# Login
# coding:utf-8
import urllib.request
import urllib.response
import urllib.parse
# import http.client
import http.cookiejar
import http.cookies
# import io
# import sys
import re
from get_user_info import idnum, password

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')

def login():
	login_url = 'https://uis2.fudan.edu.cn/amserver/UI/Login'
	data_url = 'http://jwfw.fudan.edu.cn/eams/home.action'
	cookiejar = http.cookiejar.CookieJar()
	cookie_support = urllib.request.HTTPCookieProcessor(cookiejar)
	opener = urllib.request.build_opener(cookie_support)
	headers = {
		'Host':'uis1.fudan.edu.cn',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
		# 'Accept-Encoding':'gzip, deflate',
		'Referer':'https://uis1.fudan.edu.cn/amserver/UI/Login?gx_charset=UTF-8&goto=http://jwfw.fudan.edu.cn/eams/home.action',
		'Cookie':'JSESSIONID=AD5513B6D9AB37245AA85180352EE842; AMAuthCookie=AQIC5wM2LY4SfcxpBvZV%2BYAg26ahMLmALC1XflYqVOL%2BXYw%3D%40AAJTSQACMDI%3D%23; JROUTE=2gpe; amlbcookie=02',
		'Content-Type':'application/x-www-form-urlencoded',
		'Content-Length':177
		}

	for key in headers:
		opener.addheaders = [(key, headers[key])]

	post_values = {
		'IDToken0':'',
		'IDToken1':idnum,
		'IDToken2':password,
		'IDButton':'Submit',
		'goto':'aHR0cDovL2p3ZncuZnVkYW4uZWR1LmNuL2VhbXMvaG9tZS5hY3Rpb24=',
		'encoded':'true',
		'inputCode':'',
		'gx_charset':'UTF-8'
		}

	post_data = urllib.parse.urlencode(post_values).encode(encoding = 'utf-8')
	op = opener.open(login_url, post_data)
	req = urllib.request.Request(data_url)
	response = urllib.request.urlopen(req)
	info = response.read().decode('utf-8')
	get_info = op.read().decode('utf-8')
	result = re.match(r'复旦教务系统', get_info)
	if result != []:
		return True
	else:
		return False

if __name__ == '__main__':
	a = login()
	print(a)