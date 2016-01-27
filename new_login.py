#rewrote the login module with requests
import requests
import re
import io
import sys
import codecs
from get_user_info import idnum, password, courseid

data_route = 'data.json'
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')

class login_client:
	def __init__(self):
		self._login_status = False
		self._session = requests.Session()
		self._course_data = None
		self._course_status = False

	def _login_uis(self):
		url = 'https://uis2.fudan.edu.cn/amserver/UI/Login'
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
		req = self._session.post(url, data = post_values, headers = headers, verify = False)
		
	def _reach_page(self):
		page_url = 'http://jwfw.fudan.edu.cn/eams/stdElectCourse!defaultPage.action?electionProfile.id=141'
		page = self._session.get(page_url, verify = False)
		result = re.findall(r'courseTable', page.text)
		print(result)
		if result != []:
			self._login_status = True
		else:
			raise Exception('Login Failed, Please Try Again')

	def handle_data(self):
		course_data_url = 'http://jwfw.fudan.edu.cn/eams/stdElectCourse!data.action?profileId=141'
		req = self._session.get(course_data_url, verify = False)
		with open(data_route, 'wb') as fp:
			for data in req.iter_content():
				fp.write(data)
		data = str(codecs.open(data_route, 'r', 'utf-8').read())
		courses = re.findall(r"id:\d{6},no:'\w{4}\d{6}.\d\d'", data)
		self._course_data = {}
		for data in courses:
			course_id = re.findall(r'\d{6}', data)
			course_no = re.findall(r'\w{4}\d{6}.\d\d', data)[0]
			self._course_data[course_no] = course_id
		if self._course_data != {}:
			self._course_status = True
		else:
			raise Exception('Failed to get data, Please Try Again')

	def login(self):
		self._login_uis()
		self._reach_page()
		self.handle_data()

if __name__ == '__main__':
	cclient = login_client()
	cclient.login()