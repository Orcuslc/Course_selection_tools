#login_beta

import urllib.request
import urllib.response
import urllib.parse
import urllib.error
import http.cookiejar
import http.cookies
# import http.client
# import requests
import io
import sys
import re
import json
import time
import codecs
from get_user_info import idnum, password

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')

class HttpRedirect_Handler(urllib.request.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        pass

class login_client:
	def __init__(self):
		self.uis_status = False
		self.login_status = False
		self.data_status = False
		self.opener = None
		self.cookie = None
		self.data_route = 'data.json'
		self.course_data = None
		self.course_status = False

	def _login_uis(self):
		url = 'https://uis2.fudan.edu.cn/amserver/UI/Login'
		self.cookie = http.cookiejar.CookieJar()
		cookie_support = urllib.request.HTTPCookieProcessor(self.cookie)
		self.opener = urllib.request.build_opener(cookie_support)
		headers = {
			'Host':'uis1.fudan.edu.cn',
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
			# 'Accept-Encoding':'gzip, deflate',
			'Referer':'https://uis1.fudan.edu.cn/amserver/UI/Login?gx_charset=UTF-8&goto=http://jwfw.fudan.edu.cn/eams/home.action',
			'Cookie':'JSESSIONID=AD5513B6D9AB37245AA85180352EE842; AMAuthCookie=AQIC5wM2LY4SfcxpBvZV%2BYAg26ahMLmALC1XflYqVOL%2BXYw%3D%40AAJTSQACMDI%3D%23; JROUTE=2gpe; amlbcookie=02',
			'Content-Type':'application/x-www-form-urlencoded',
			'Content-Length':177,
			'Connection':'close'
			}
		for key in headers:
			self.opener.addheaders = [(key, headers[key])]
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
		try:
			op = self.opener.open(url, post_data).read().decode('utf-8')
		except urllib.error.HTTPError:
			op = self.opener.open(url, post_data).read().decode('utf-8')
		except urllib.error.HTTPError:
			op = self.opener.open(url, post_data).read().decode('utf-8')
		result = re.findall(r'logout.action', op)
		if result != []:
			self.uis_status = True

	def _login_page(self):
		if self.uis_status != True:
			print('Login Failed, Please Try Again')
			return
		page_url = 'http://jwfw.fudan.edu.cn/eams/stdElectCourse!defaultPage.action?electionProfile.id=141'
		request = urllib.request.Request(page_url)
		page = self.opener.open(request).read().decode('utf-8')
		page_result = re.findall(r'courseTable', page)
		if page_result != []:
			self.login_status = True
		# requests.get(page_url, cookies = self.cookie)

	def _get_data(self):
		if self.login_status != True:
			print('Login Failed, Please Try Again')
			return
		course_data_url = 'http://jwfw.fudan.edu.cn/eams/stdElectCourse!data.action?profileId=141'
		data_op = self.opener.open(course_data_url).read()
		f = open(self.data_route, 'wb')
		f.write(data_op)
		f.close()
		self.data_status = True
		# requests.get(course_data_url, cookies = self.cookie)

	def _course_data_analysis(self):
		if self.data_status != True:
			print('Failed to get data, please try again')
			return 
		data = codecs.open(self.data_route, 'r', 'utf-8').read()
		data = str(data)
		courses = re.findall(r"id:\d{6},no:'\w{4}\d{6}.\d\d'", data)
		self.course_data = {}
		for data in courses:
			course_id = re.findall(r'\d{6}', data)[0]
			course_no = re.findall(r'\w{4}\d{6}.\d\d', data)[0]
			self.course_data[course_no] = course_id
		self.course_status = True

	def login(self):
		self._login_uis()
		self._login_page()
		self._get_data()
		self._course_data_analysis()
		print('data complete')



if __name__ == '__main__':
	client = login_client()
	client.login()
	print(client.course_status)
	# print(client.course_data)
