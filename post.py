 # push_course
import urllib.parse
import urllib.request
import urllib.response
import urllib.error
import io
import sys
from login import login_client
from get_user_info import courseid

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')

class post_client(login_client):
	def __init__(self):
		super().__init__()
		self.login()
		self.course_id = self.course_data[courseid]
		self.post_status = False
		self.select_ststus = False

	def _select(self):
		post_url = 'http://jwfw.fudan.edu.cn/eams/stdElectCourse!batchOperator.action?profileId=141'
		post_values = {
			'optype':'true',
			'operator0':self.course_id.join(':true:0')
		}
		post_data = urllib.parse.urlencode(post_values).encode(encoding = 'utf-8')
		headers = {
			# (Request-Line)	POST /eams/stdElectCourse!batchOperator.action?profileId=141 HTTP/1.1
				'Host':'jwfw.fudan.edu.cn',
				'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
				'Accept':'text/html, */*; q=0.01',
				'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
				# 'Accept-Encoding':'gzip, deflate',
				'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
				'X-Requested-With':'XMLHttpRequest',
				'Referer':'http://jwfw.fudan.edu.cn/eams/stdElectCourse!defaultPage.action?electionProfile.id=141',
				'Content-Length':39,
				'Cookie':'JSESSIONID=F25E5CB856612C0581A140B56879CA82.82-; amlbcookie=02; iPlanetDirectoryPro=AQIC5wM2LY4Sfcyt%2FiriP%2B3bhCnyrqZk5Nr6EmukiXClpWk%3D%40AAJTSQACMDI%3D%23',
				'Connection':'keep-alive',
				}
		request = urllib.request.Request(post_url, headers = headers, data = post_data)
		info = self.opener.open(request).read().decode('utf-8')
		print(info)

	def post(self):
		self._select()

if __name__ == '__main__':
	client = post_client()
	client.post()