 # push_course
import urllib.parse
import urllib.request
import urllib.response
import urllib.error
import io
import sys
import re
from login import login_client
from get_user_info import courseid

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')

class post_client(login_client):
	def __init__(self):
		super().__init__()
		super().login()
		self.course_id = self.course_data[courseid]
		self.post_status = False
		self.select_ststus = False

	def _select(self):
		'''
		剩下一个问题尚未解决：在向post_url提交表单时，服务器自动将其重定向至main页。
		如何向此地址提交表单？
		'''
		post_url = 'http://jwfw.fudan.edu.cn/eams/stdElectCourse!batchOperator.action?Profile.id=141'
		post_values = {
			'optype':'true',
			'operator0':self.course_id.join(':true:0')
		}
		post_data = urllib.parse.urlencode(post_values).encode(encoding = 'utf-8')
		headers = {
			'POST': '/eams/stdElectCourse!batchOperator.action?profileId=141 HTTP/1.1',
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Accept': 'text/html, */*; q=0.01',
			'X-Requested-With': 'XMLHttpRequest',
			'Referer': 'http://jwfw.fudan.edu.cn/eams/stdElectCourse!defaultPage.action?electionProfile.id=141',
			'Accept-Language': 'zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3',
			# 'Accept-Encoding': 'gzip, deflate',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.11082',
			'Content-Length': '39',
			'Host': 'jwfw.fudan.edu.cn',
			'Connection': 'Keep-Alive',
			'Pragma': 'no-cache',
			# 'Cookie': 'semester.id=182; JSESSIONID=; amlbcookie=01; iPlanetDirectoryPro=AQIC5wM2LY4SfcwIXJ%2BM5po2KR3riijkoaA9oqAzbzpBc9w%3D%40AAJTSQACMDE%3D%23'
				}
		request = urllib.request.Request(url = post_url, headers = headers, data = post_data)
		# for key in headers:
		# 	self.opener.addheaders = [(key, headers[key])]
		info = self.opener.open(request).read().decode('utf-8')
		# info = self.opener.open(post_url, post_data).read().decode('utf-8')
		self.post_status = True
		return info

	def post(self):
		info = self._select()
		result1 = re.findall(r'选课成功', info)
		result2 = re.findall(r'人数已满', info)
		if result1 != []:
			self.select_status = 'Succeed'
		elif result2 != []:
			self.select_status = 'No vancacy'
		else:
			self.select_status = False
		print(info)
		print(self.select_status)


if __name__ == '__main__':
	client = post_client()
	client.post()